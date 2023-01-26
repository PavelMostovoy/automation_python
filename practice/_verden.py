# open wikipedia
# find page for First world war
# Find Verden apearanc on page
# additional Find on page 11.11.18
# additionally find time
import logging
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from page_obj import Config, Wikipedia

# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler("test.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handlerh
ch.setFormatter(formatter)

# add file_handlerh to logger
logger.addHandler(ch)


expected = Wikipedia(Config.url)

driver = webdriver.Chrome()
driver.get(expected.url)


search_filed = driver.find_element(By.ID, expected.search_field_id)
logger.debug(search_filed)
search_filed.send_keys(expected.info)
# search_filed.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, expected.search_button_id).click()