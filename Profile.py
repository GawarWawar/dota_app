from DotaMatch import DotaMatch

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

import time
import utils

# PLATER_ID = 167230743

class DotaProfile:
    def __init__(
        self,
        PROFILE_ID,
        driver: WebDriver|None = None,
        driver_options: Options = None
    ) -> None:
        self.PROFILE_ID = PROFILE_ID
        if driver is None:
            self.driver = utils.set_up_driver(driver_options)
        self._is_processed = False
        
    def get_last_match(self) -> DotaMatch|None:
        self.driver.get(f"https://www.opendota.com/players/{self.PROFILE_ID}")
        self._is_processed = True
        
        time.sleep(2)
        with open("test.html", "w") as f:
            f.write(self.driver.page_source)
        body = self.driver.find_elements(By.TAG_NAME, "a")
        
        link_text = "https://www.opendota.com/matches/"
        for el in body:
            link = el.get_attribute("href")
            if link_text in link:
                match_id = int(link.removeprefix(link_text))
                return DotaMatch(match_id, driver=self.driver)
            
        return None
    
    def get_resent_matches(self) -> list[DotaMatch]:
        self.driver.get(f"https://www.opendota.com/players/{self.PROFILE_ID}")
        self._is_processed = True
        
        time.sleep(2)
        with open("test.html", "w") as f:
            f.write(self.driver.page_source)
        body = self.driver.find_elements(By.TAG_NAME, "a")
        
        link_text = "https://www.opendota.com/matches/"
        matches = []
        for el in body:
            link = el.get_attribute("href")
            if link_text in link:
                match_id = int(link.removeprefix(link_text))
                matches.append(
                    DotaMatch(match_id, driver=self.driver)
                )
        return matches
            
            
        
        
if __name__ == "__main__":
    profile = DotaProfile(167230743)
    
    profile.driver = utils.set_up_driver(debug=True)
    profile.get_last_match()