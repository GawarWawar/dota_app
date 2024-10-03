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
        self._is_parsed = None
        
        if driver is None:
            self.driver = utils.set_up_driver(driver_options)
        else:
            self.driver = driver
    
    @property
    def is_parsed(self) -> bool:
        """ Parse status of the DotaMatch. 
        After __init__ set to be None. If checked_parsed_status was not used to set is_parsed, uses it to determine status

        Returns:
            bool: False if match is not parsed yet, True othervise
        """
        if self._is_parsed is None:
            self._is_parsed = self.check_parsed_status()
        return self._is_parsed
    
    @is_parsed.setter
    def is_parsed(self, _):
        """ Doesnt allow to set any value to the is_parsed directly and redirects to the check_parsed_status

        Args:
            _ (Any): Setter doesnt allow to set this element on its own, so doesnt matter what type of the argument is

        Raises:
            AttributeError: Can not set this attribute directly. Use check_parsed_status instead
        """
        raise AttributeError("Can not set this attribute directly. Use check_parsed_status")
    
    def check_parsed_status(self) -> bool:
        """  Checked parsed status by going to the site of the match (opendota.com/matches/MATCH_ID) and check if there is a text that stayts "The replay for this match has not yet been parsed. Not all data may be available".

        Returns:
            bool: If text is on the page, then return False, that indicates "match is not parsed", othervise True
        """
        self.driver.get(f"https://www.opendota.com/matches/{self.MATCH_ID}")
        assert "OpenDota" in self.driver.title

        text_indicator = "The replay for this match has not yet been parsed. Not all data may be available."
        time.sleep(2)
        body = self.driver.find_element(By.TAG_NAME, "body")

        if text_indicator in body.text:
            self._is_parsed = False
            return False
        else:
            self._is_parsed = True
            return True
        
    def parse_match(self) -> str:
        """First check _is_parsed status. If it is assigned and False, proceed to request parse by MATCH_ID, using OpenDota link
        If _is_parsed was no assigned by check_parsed_status -> self.is_parsed will do it in the check

        Returns:
            str: Description of what happened.
            If _is_parsed was True -> "Match was already parsed"
            If parse was sucsessful -> "Parse request successful"
        """
        if self.is_parsed: return "Match was already parsed"
        
        self.driver.get(f"https://www.opendota.com/request#{self.MATCH_ID}")
        text_indicator = "Request a Parse"
        time.sleep(2)
        while True:
                body = self.driver.find_element(By.TAG_NAME, "body")
                if text_indicator not in body.text:
                    break
        
        return "Parse request successful"






