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