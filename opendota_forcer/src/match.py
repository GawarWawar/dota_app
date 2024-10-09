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
        self.player_stats:None|list[dict[str, str]] = None
        
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
            self.check_parsed_status()
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
        else:
            self._is_parsed = True
        return self._is_parsed
        
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

    def collect_match_stats(self) -> list[dict[str, str]]:
        MATCH_SIDES= ["radiant", "dire"]
        PLAYER_TEXT_KEYS ={
            "complex": ["level", "nick_name", "lane", "lane_result", "stats"],
            "simple": ["level", "nick_name", "stats"],
            "anonimus": ["level", "stats"],
        }
        KEYS_FOR_STATS = [
            "kills",
            "deaths",
            "assists",
            "net_worth",
            "last_hits",
            "denies",
            "gold_per_minute",
            "xp_per_minute",
            "damage",
            "heal",
            "damage_to_buildings",
            "wards",
        ]
        WARDS = ["observers", "sentries"]

        self.driver.get(f"https://www.dotabuff.com/matches/{self.MATCH_ID}")
        match_results = self.driver.find_element(By.CLASS_NAME, "team-results")
        
        self.players_stats = []
        for side in MATCH_SIDES:
            side_results = match_results.find_elements(By.CLASS_NAME, f"faction-{side}")
            for player in side_results:
                keys_for_stats = KEYS_FOR_STATS.copy()
                dict_about_player = {}
                
                dict_about_player["side"] = side
                links = player.find_elements(By.TAG_NAME, "a")  
                for link in links:
                    link_href = link.get_attribute("href")
                    if "player" in link_href:
                        dict_about_player["player_id"] = link_href.removeprefix("https://www.dotabuff.com/players/")
                    elif "heroes" in link_href:
                        dict_about_player["hero_choice"] = link_href.removeprefix("https://www.dotabuff.com/heroes/")
                    
                    
                role = player.find_elements(By.CLASS_NAME, "support-icon")
                if len(role) > 0:
                    dict_about_player["role"] = "support"
                else:
                    dict_about_player["role"] = "core"
                        
                player_info = player.text.split("\n")
                if len(player_info) <= 2:
                    text_key_variant = "anonimus"
                    keys_for_stats.insert(0, "nick_name")
                elif len(player_info) <= 3:
                    text_key_variant = "simple"
                else:
                    text_key_variant = "complex"
                    
                for key_number, key in enumerate(PLAYER_TEXT_KEYS[text_key_variant]):
                    if key == "stats":    
                        player_stats:str = player_info[key_number]
                        stats:list[str] = player_stats.split(" ")
                    else:
                        dict_about_player[key] = player_info[key_number]
                        
                for stat_number, stat in enumerate(keys_for_stats):
                    if stat == "wards":
                        if text_key_variant == "complex":
                            player_wards = stats[stat_number].split("/")
                            for list_position, ward_type in enumerate(WARDS):
                                dict_about_player[ward_type] = player_wards[list_position]
                        else:
                            for list_position, ward_type in enumerate(WARDS):
                                dict_about_player[ward_type] = "0"
                    else:
                        dict_about_player[stat] = stats[stat_number]
                        
                if dict_about_player["nick_name"] == "Anonymous":
                    dict_about_player["player_id"] = None
                self.players_stats.append(dict_about_player)    
        
        return self.players_stats






