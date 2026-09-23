# # # from appium import webdriver
# # # from appium.options.android import UiAutomator2Options
# # # import time

# # # options = UiAutomator2Options()
# # # options.platform_name = "Android"
# # # options.device_name = "emulator-5554"
# # # options.automation_name = "UiAutomator2"
# # # options.app_package = "com.ffsteel.hrms_dashboard"
# # # options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"

# # # appium_server_url = "http://127.0.0.1:4723"
# # # driver = webdriver.Remote(appium_server_url, options=options)

# # # try:
# # #     print("App opened, waiting for it to load...")
# # #     time.sleep(8)

# # #     driver.save_screenshot("current_screen.png")
# # #     print("Screenshot saved as current_screen.png")

# # # finally:
# # #     driver.quit()
# # #     print("App/session band ho gayi.")

# # from appium import webdriver
# # from appium.options.android import UiAutomator2Options
# # from appium.webdriver.common.appiumby import AppiumBy
# # import time

# # # ========== CAPABILITIES ==========
# # options = UiAutomator2Options()
# # options.platform_name = "Android"
# # options.device_name = "emulator-5554"
# # options.automation_name = "UiAutomator2"
# # options.app_package = "com.ffsteel.hrms_dashboard"
# # options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"

# # appium_server_url = "http://127.0.0.1:4723"

# # # ========== DRIVER START ==========
# # driver = webdriver.Remote(appium_server_url, options=options)

# # try:
# #     print("App opened, waiting for it to load...")
# #     time.sleep(8)

# #     # ---------- Employee ID field ----------
# #     print("Employee ID field dhoond raha hoon...")
# #     emp_field = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
# #     emp_field.click()
# #     emp_field.send_keys("52225")   # <-- yahan apna Employee ID daalo
# #     print("Employee ID type ho gayi.")

# #     # ---------- Password field ----------
# #     print("Password field dhoond raha hoon...")
# #     all_fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
# #     print(f"Total {len(all_fields)} fields mili.")

# #     if len(all_fields) >= 2:
# #         pwd_field = all_fields[1]   # doosra EditText = Password
# #         pwd_field.click()
# #         pwd_field.send_keys("your_password_here")   # <-- yahan apna password daalo
# #         print("Password type ho gaya.")
# #     else:
# #         print("Password field nahi mili! Sirf 1 field mili.")

# #     # ---------- Screenshot before login ----------
# #     driver.save_screenshot("before_login.png")
# #     print("before_login.png save ho gayi.")

# #     # ---------- Login button click ----------
# #     print("Login button dhoond raha hoon...")
# #     login_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
# #                                     'new UiSelector().text("Login")')
# #     login_btn.click()
# #     print("Login button click ho gaya.")

# #     # ---------- Wait for dashboard ----------
# #     time.sleep(8)
# #     driver.save_screenshot("after_login.png")
# #     print("after_login.png save ho gayi.")

# # finally:
# #     driver.quit()
# #     print("Session band ho gayi.")

# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# import time

# # ========== CAPABILITIES ==========
# options = UiAutomator2Options()
# options.platform_name = "Android"
# options.device_name = "emulator-5554"
# options.automation_name = "UiAutomator2"
# options.app_package = "com.ffsteel.hrms_dashboard"
# options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"
# options.auto_grant_permissions = True
# options.no_reset = True

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


# def click_if_exists(text_options, wait=2):
#     """Click on whichever text is found first."""
#     for text in text_options:
#         try:
#             btn = driver.find_element(
#                 AppiumBy.ANDROID_UIAUTOMATOR,
#                 f'new UiSelector().textContains("{text}")'
#             )
#             btn.click()
#             print(f"Clicked: {text}")
#             time.sleep(wait)
#             return True
#         except Exception:
#             continue
#     return False


# try:
#     print("App is opening, please wait...")
#     time.sleep(6)

#     # ---------- Handle popups ----------
#     print("Checking for popups...")
#     click_if_exists(["WHILE USING", "ALLOW", "Allow"], wait=3)
#     click_if_exists(["ALLOW", "Allow"], wait=3)
#     time.sleep(2)

#     driver.save_screenshot("1_login_screen.png")
#     print("Login screen ready.")

#     # ---------- Enter Employee ID and Password ----------
#     fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
#     print(f"Found {len(fields)} input fields.")

#     if len(fields) >= 2:
#         # Employee ID
#         fields[0].click()
#         time.sleep(1)
#         fields[0].clear()
#         fields[0].send_keys("3639")
#         print("Employee ID entered: 3639")

#         # Password
#         fields[1].click()
#         time.sleep(1)
#         fields[1].clear()
#         fields[1].send_keys("12345")
#         print("Password entered.")

#     else:
#         print("Login fields not found!")
#         driver.save_screenshot("error_no_fields.png")
#         raise Exception("Login fields not found")

#     time.sleep(2)
#     driver.save_screenshot("2_filled.png")
#     print("Filled form screenshot saved.")

#     # ---------- Click Login button ----------
#     print("Clicking Login button...")
#     try:
#         login = driver.find_element(
#             AppiumBy.ANDROID_UIAUTOMATOR,
#             'new UiSelector().textContains("Login")'
#         )
#         login.click()
#         print("Login button clicked.")
#     except Exception as e:
#         print(f"Login button not found: {e}")
#         driver.tap([(180, 500)])
#         print("Clicked using coordinates as fallback.")

#     time.sleep(12)
#     driver.save_screenshot("3_after_login.png")
#     print("After login screenshot saved.")

#     # ---------- Find Loan module ----------
#     print("\nLooking for Loan module...")
#     loan_found = False
#     for loan_text in ["Loan", "LOAN", "Loans", "Advance", "Salary Advance", "Apply Loan"]:
#         try:
#             loan = driver.find_element(
#                 AppiumBy.ANDROID_UIAUTOMATOR,
#                 f'new UiSelector().textContains("{loan_text}")'
#             )
#             loan.click()
#             print(f"Loan module found and clicked: {loan_text}")
#             loan_found = True
#             break
#         except Exception:
#             continue

#     if loan_found:
#         time.sleep(10)
#         driver.save_screenshot("4_loan_module.png")
#         print("Loan module screenshot saved.")
#     else:
#         print("Loan module not found directly.")
#         driver.save_screenshot("4_dashboard.png")
#         print("Dashboard screenshot saved - check what options are available.")

#     # ---------- Keep app open ----------
#     print("\n>>> App is still open on the emulator. Take a look.")
#     print(">>> Press Enter in the terminal to close the app and end session.")
#     input()

# finally:
#     driver.quit()
#     print("Session ended.")

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# ========== CAPABILITIES ==========
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.ffsteel.hrms_dashboard"
options.app_activity = "com.ffsteel.hrms_dashboard.MainActivity"
options.auto_grant_permissions = True
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


def click_by_desc(desc, wait=2):
    """Click element by content-desc"""
    try:
        el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, desc)
        el.click()
        print(f"Clicked: {desc}")
        time.sleep(wait)
        return True
    except Exception:
        print(f"Not found: {desc}")
        return False


def click_if_exists(text_options, wait=2):
    """Click by text (fallback)"""
    for text in text_options:
        try:
            btn = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{text}")'
            )
            btn.click()
            print(f"Clicked: {text}")
            time.sleep(wait)
            return True
        except Exception:
            continue
    return False


try:
    print("=" * 50)
    print("STEP 1: App launching...")
    print("=" * 50)
    time.sleep(6)

    # ---------- Popups ----------
    click_if_exists(["WHILE USING", "ALLOW", "Allow"], wait=3)
    click_if_exists(["ALLOW", "Allow"], wait=3)
    time.sleep(2)

    driver.save_screenshot("1_login_screen.png")
    print("Login screen ready.\n")

    # ==========================================
    # STEP 2: LOGIN
    # ==========================================
    print("=" * 50)
    print("STEP 2: Logging in...")
    print("=" * 50)

    fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    print(f"Found {len(fields)} input fields")

    if len(fields) >= 2:
        fields[0].click()
        time.sleep(1)
        fields[0].clear()
        fields[0].send_keys("3639")
        print("Employee ID: 3639")

        fields[1].click()
        time.sleep(1)
        fields[1].clear()
        fields[1].send_keys("12345")
        print("Password: 12345")
    else:
        raise Exception("Login fields not found!")

    time.sleep(2)
    driver.save_screenshot("2_filled.png")

    # ---------- Login button ----------
    print("Clicking Login...")
    buttons = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
    print(f"Found {len(buttons)} buttons")

    login_clicked = False
    for b in buttons:
        txt = (b.get_attribute('text') or "").lower()
        if "login" in txt:
            b.click()
            print(f"Clicked Login button")
            login_clicked = True
            break

    if not login_clicked and len(buttons) > 0:
        buttons[-1].click()
        print("Clicked last button (Login)")
        login_clicked = True

    time.sleep(12)
    driver.save_screenshot("3_after_login.png")
    print("Logged in successfully!\n")

    # ==========================================
    # STEP 3: OPEN LOAN MENU
    # ==========================================
    print("=" * 50)
    print("STEP 3: Opening Loan menu...")
    print("=" * 50)

    # Hamburger menu / side menu open karo (agar band ho)
    # Pehle check karo Loan menu dikh raha hai ya nahi
    if click_by_desc("Loan, Expanded", wait=2):
        print("Loan menu was already expanded")
    else:
        # Menu icon click karo (top-left hamburger)
        try:
            menu_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Open navigation menu")
            menu_btn.click()
            print("Opened navigation menu")
            time.sleep(2)
        except Exception:
            print("Menu icon not found, trying 'Loan' text")
            click_by_desc("Loan", wait=2)

    driver.save_screenshot("4_loan_menu.png")

    # ==========================================
    # STEP 4: CLICK "Apply For Loan"
    # ==========================================
    print("=" * 50)
    print("STEP 4: Clicking 'Apply For Loan'...")
    print("=" * 50)

    if not click_by_desc("Apply For Loan", wait=5):
        raise Exception("'Apply For Loan' not found!")

    time.sleep(5)
    driver.save_screenshot("5_apply_loan_screen.png")
    print("Apply For Loan screen opened\n")

    # ==========================================
    # STEP 5: VERIFY LOAN APPLICATION SCREEN
    # ==========================================
    print("=" * 50)
    print("STEP 5: Verifying loan application screen...")
    print("=" * 50)

    # Screen pe ye elements hone chahiye:
    expected_elements = [
        "Ayesha Aqeel",
        "3639",
        "Permanent",
        "Loans",
        "Approvals",
        "Personal Loan",
        "Official Loan",
        "Select Loan Type",
        "Allowed Limit",
        "Guarantor 1",
        "Guarantor 2"
    ]

    print("\nChecking for expected elements:")
    for elem in expected_elements:
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, elem)
            print(f"  [FOUND]   {elem}")
        except Exception:
            print(f"  [MISSING] {elem}")

    # ==========================================
    # STEP 6: SELECT LOAN TYPE (optional)
    # ==========================================
    print("\n" + "=" * 50)
    print("STEP 6: Opening 'Select Loan Type' dropdown...")
    print("=" * 50)

    if click_by_desc("Select Loan Type", wait=3):
        driver.save_screenshot("6_loan_type_dropdown.png")
        print("Dropdown opened")
        time.sleep(2)

    # ---------- Keep app open ----------
    print("\n" + "=" * 50)
    print(">>> TEST COMPLETE")
    print(">>> App is still open. Press Enter to close.")
    print("=" * 50)
    input()

finally:
    driver.quit()
    print("\nSession ended.")