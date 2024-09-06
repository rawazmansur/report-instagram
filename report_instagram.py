from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (no GUI) for automation
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to the ChromeDriver
service = Service(r'C:\Users\rawaz\OneDrive\Desktop\chromedriver-win64(1)\chromedriver-win64\chromedriver.exe')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram
driver.get('https://www.instagram.com')

# Wait for the page to load
time.sleep(5)

# Log in to Instagram
username_input = driver.find_element("name", "username")
password_input = driver.find_element("name", "password")

# Enter your Instagram credentials
username_input.send_keys("leo.private.kurdish")
password_input.send_keys("Barezmansur$1995")

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the login to complete
time.sleep(10)

# Navigate to the target user profile
target_user = "lanarebwar_"
driver.get(f'https://www.instagram.com/{target_user}/')

# Wait for the profile to load
time.sleep(5)

# Click on the three dots (menu) to open options
try:
    menu_button = driver.find_element("xpath", '//button[contains(@aria-label, "More options")]')
    menu_button.click()
except Exception as e:
    print("Failed to find the menu button:", e)

# Wait for the options to appear
time.sleep(2)

# Click the Report button
try:
    report_button = driver.find_element("xpath", '//button[contains(text(), "Report")]')
    report_button.click()
except Exception as e:
    print("Failed to find the Report button:", e)

# Wait for the report dialog to appear
time.sleep(2)

# Select the reason for reporting
try:
    reason_button = driver.find_element("xpath", '//button[contains(text(), "Spam")]')
    reason_button.click()
except Exception as e:
    print("Failed to find the reason button:", e)

# Confirm the report
try:
    confirm_button = driver.find_element("xpath", '//button[contains(text(), "Submit")]')
    confirm_button.click()
except Exception as e:
    print("Failed to find the Submit button:", e)

# Close the browser
driver.quit()
