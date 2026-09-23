from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.ffsteel.hrms_dashboard"
options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"

appium_server_url = "http://127.0.0.1:4723"
driver = webdriver.Remote(appium_server_url, options=options)

try:
    print("App opened, waiting for it to load...")
    time.sleep(8)

    driver.save_screenshot("current_screen.png")
    print("Screenshot saved as current_screen.png")

finally:
    driver.quit()
    print("App/session band ho gayi.")