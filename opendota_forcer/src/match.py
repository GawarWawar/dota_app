from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time

from . import utils

class DotaMatch:
    """ Class which responsibukuty is to manage match of Dota  
    """
    
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
        """ Checked parsed status by _is_parsed_() and assign _is_parsed atribute

        Returns:
            bool: If match was already Parsed, it will return True, othervise False
        """
        self._is_parsed = self._is_parsed_()
        return self._is_parsed
        
    def _is_parsed_(self) -> bool:
        """ Underling method that goes to the site of the match and checks if there is a text that stayts "match has not yet been parsed".

        Returns:
            bool: If text is on the page, then return False, that indicates "match is not parsed", othervise True
        """
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
        """First check _is_parsed status. If it is assigned and False, proceed to request parse by MATCH_ID, using OpenDota link

        Returns:
            str: Description of what happened.
            If _is_parsed was no assigned by check_parsed_status -> "Parsed status is not defined."
            If _is_parsed was True -> "Match was already parsed"
            If parse was sucsessful -> "Parse request successful"
        """
        try:
            if self._is_parsed: return "Match was already parsed"
        except AttributeError:
            return "Parsed status is not defined."
        
        self.driver.get(f"https://www.opendota.com/request#{self.MATCH_ID}")
        text_indicator = "Request a Parse"
        time.sleep(2)
        while True:
                body = self.driver.find_element(By.TAG_NAME, "body")
                if text_indicator not in body.text:
                    break
        
        return "Parse request successful"






