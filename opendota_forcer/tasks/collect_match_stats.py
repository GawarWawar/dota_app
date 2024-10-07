from selenium.webdriver.common.by import By
from opendota_forcer.src.utils import set_up_driver

def collect_match_stats(match_id):
    MATCH_SIDES= ["radiant", "dire"]
    PLAYER_TEXT_KEYS = ["level", "nick_name", "lane", "lane_result", "stats"]
    STATS_TEXT_KEYS = [
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
    WARDS = ["observer","sentry"]

    driver = set_up_driver()
    driver.get(f"https://www.dotabuff.com/matches/{match_id}")
    
    match_results = driver.find_element(By.CLASS_NAME, "team-results")
    players = []
    for side in MATCH_SIDES:
        side_results = match_results.find_elements(By.CLASS_NAME, f"faction-{side}")
        for player in side_results:
            dict_about_player = {}
            links = player.find_elements(By.TAG_NAME, "a")  
            for link in links:
                link_href = link.get_attribute("href")
                if "heroes" in link_href:
                    dict_about_player["hero_choice"] = link_href.removeprefix("https://www.dotabuff.com/heroes/")
                
            player_info = player.text.split("\n")
            for key_number, key in enumerate(PLAYER_TEXT_KEYS):
                if key == "stats":    
                    player_stats:str = player_info[key_number]
                    stats:list[str] = player_stats.split(" ")
                else:
                    dict_about_player[key] = player_info[key_number]
                    
            for stat_number, stat in enumerate(STATS_TEXT_KEYS):
                if stat == "heal" and stats[stat_number] == "-":
                    dict_about_player[stat] = "0"
                elif stat == "wards":
                    player_wards = stats[stat_number].split("/")
                    for list_position, ward_type in enumerate(WARDS):
                        if player_wards[list_position] == "-":
                            dict_about_player[ward_type] = "0"
                        else:
                            dict_about_player[ward_type] = player_wards[list_position]
                else:
                    dict_about_player[stat] = stats[stat_number]
            players.append(dict_about_player)    
    
    return players