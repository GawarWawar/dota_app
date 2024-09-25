from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time

from . import utils

class DotaMatch:
    def __init__(
        self, 
        MATCH_ID: int, 
        driver: WebDriver|None = None,
        driver_options: Options|None = None
    ) -> None:
        self.MATCH_ID = MATCH_ID
        if driver is None:
            self.driver = utils.set_up_driver(driver_options)
        else:
            self.driver = driver
    
    def check_parsed_status(self) -> bool:
        self._is_parsed = self._is_parsed_()
        return self._is_parsed
        
    def _is_parsed_(self) -> bool:
        self.driver.get(f"https://www.opendota.com/matches/{self.MATCH_ID}")
        assert "OpenDota" in self.driver.title

        text_indicator = "The replay for this match has not yet been parsed. Not all data may be available."
        time.sleep(2)
        body = self.driver.find_element(By.TAG_NAME, "body")

        if text_indicator in body.text:
            return False
        else:
            return True
        
    def parse_match(self) -> str:
        if self._is_parsed: return "Already parsed"
        
        self.driver.get(f"https://www.opendota.com/request#{self.MATCH_ID}")
        text_indicator = "Request a Parse"
        time.sleep(2)
        while True:
                body = self.driver.find_element(By.TAG_NAME, "body")
                if text_indicator not in body.text:
                    break
        
        return "Parse request successful"






