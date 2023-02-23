# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appActivity"] = ".NexusLauncherActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Messages").click()
time.sleep(3)

el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start chat")
el2.click()

el3 = driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.messaging:id/recipient_text_view")
el3.send_keys("some data")
assert el3.text == "some data"

# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(
#     interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(1342, 2769)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()

driver.quit()

