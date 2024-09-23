import selenium
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options


import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome(options=chrome_options)

MATCH_ID = 7952112098

driver.get(f"https://www.opendota.com/matches/{MATCH_ID}")
assert "OpenDota" in driver.title

target_text = "The replay for this match has not yet been parsed. Not all data may be available."
time.sleep(5)
    # Try to find the element containing the text
body = driver.find_element(By.TAG_NAME, "body")

if target_text in body.text:
    match_buttons = body.find_element(By.CLASS_NAME, "matchButtons")
    driver.get(f"https://www.opendota.com/request#{MATCH_ID}")
    target_text = "Requesxt a Parse"
    while True:
        body = driver.find_element(By.TAG_NAME, "body")
        if target_text not in body.text:
            break
    print("DONE!")
else:
    print("Text not found!")

driver.close()