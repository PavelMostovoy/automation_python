# open wikipedia
# find page for First world war
# Find Verden apearanc on page
# additional Find on page 11.11.18
# additionally find time

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import page_obj


expected_url = f'{page_obj.url}'

driver = webdriver.Chrome()
driver.get(expected_url)

search_filed = driver.find_element(By.ID, page_obj.search_field_id)
search_filed.send_keys(page_obj.info)
# search_filed.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, page_obj.search_button_id).click()
time.sleep(100)
