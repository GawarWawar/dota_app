import logging    
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

def set_up_driver(
    driver_options: webdriver.IeOptions|None = None,
    debug: bool = False
) -> WebDriver:

    if driver_options is None:
        driver_options = Options()
        if not debug:
            driver_options.add_argument("--headless")
        driver_options.add_argument("--enable-javascript")
    return webdriver.Chrome(options=driver_options)


# Create logger to make logs
def get_logger (
    logger_name: str,
    log_level: str = "INFO",
):     
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    
    return logger
                
def assign_filehandler_to_logger (
    logger: logging.Logger,
    file_location: tuple = ('data', 'actions.log')
):       
    file_handler = logging.FileHandler(
        os.path.join(
            file_location
        )
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return file_handler