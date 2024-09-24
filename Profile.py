from DotaMatch import DotaMatch

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

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
        else:
            self.driver = driver
        
    def get_last_match(self) -> DotaMatch|None:
        self.driver.get(f"https://www.opendota.com/players/{self.PROFILE_ID}")
        
        time.sleep(2)
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
        
        time.sleep(2)
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
            
    def get_matches(
        self,
        amount_of_matches_to_get: int = 20
    ):
        self.driver.get(f"https://www.opendota.com/players/{self.PROFILE_ID}/matches")
        
        time.sleep(2)
        

        link_text = "https://www.opendota.com/matches/"
        id_of_matches = []
        n_of_button = 1
        while len(id_of_matches) < amount_of_matches_to_get:

            
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == str(n_of_button):
                    try:
                        button.click()
                    except ElementClickInterceptedException:
                        break
                    else:
                        break
            n_of_button += 1
            body = self.driver.find_elements(By.TAG_NAME, "a")
            
            for el in body:
                link = el.get_attribute("href")
                if link_text in link:
                    match_id = int(link.removeprefix(link_text))
                    if (
                        len(id_of_matches) < amount_of_matches_to_get
                        and match_id not in id_of_matches
                    ):    
                        id_of_matches.append(
                            match_id
                        )
        
        matches = []
        for id in id_of_matches:    
            matches.append(DotaMatch(id, driver=self.driver))
                
        return matches
            
        
        
if __name__ == "__main__":
    driver = utils.set_up_driver(debug=True)
    profile = DotaProfile(167230743, driver=driver)
    
    matches = profile.get_matches(39)
    for d_match in matches:
        print(d_match.MATCH_ID)
    print(len(matches))