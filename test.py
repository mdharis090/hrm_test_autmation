from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set the capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.ffsteel.hrms_dashboard"
options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"

# Appium server URL
appium_server_url = "http://127.0.0.1:4723"

# Create the driver (this connects to the emulator)
driver = webdriver.Remote(appium_server_url, options=options)

print("App opened, waiting for it to load...")
time.sleep(5)

# Find the element — same one you saw in Appium Inspector (using content-desc)
leave_item = driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "376205 Irfan  Ullah SL Short Leave Sep 14, 2026 0.33 day(s)"
)

# Click on it
leave_item.click()
print("Clicked on the leave item!")

# Wait for the details screen to load
time.sleep(3)

# Verify the details screen opened correctly (checking page content)
page_source = driver.page_source
if "Pending Leave Report" in page_source:
    print("✅ Test Passed: Details screen opened correctly!")
else:
    print("❌ Test Failed: Details screen did not open.")

# Close the session
driver.quit()