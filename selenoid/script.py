import time

from selenium import webdriver

capabilities = {
    "browserName": "firefox",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities=capabilities)



driver.get("https://www.wikipedia.org/")

time.sleep(3)

driver.get("https://adv.wiki")

time.sleep(3)

driver.close()


