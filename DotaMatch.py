from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

import time

import utils

class DotaMatch:
    def __init__(
        self, 
        MATCH_ID, 
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
        if self._is_parsed: return "Match is already parsed"
        
        self.driver.get(f"https://www.opendota.com/request#{MATCH_ID}")
        text_indicator = "Request a Parse"
        time.sleep(2)
        while True:
                body = self.driver.find_element(By.TAG_NAME, "body")
                if text_indicator not in body.text:
                    break
        
        return "Match has been parsed sucsessfully"

    
if __name__ == "__main__":
    MATCH_ID = 7904861993
    d_match = DotaMatch(MATCH_ID)
    d_match.check_parsed_status()
    print(d_match.parse_match())
    print(d_match.check_parsed_status())






