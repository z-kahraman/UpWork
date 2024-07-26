from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Start the browser session
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the protected URL
driver.get("PROTECTED_URL")

# Perform necessary actions (e.g., logging in)
# driver.find_element(By.ID, "username").send_keys("USERNAME")
# driver.find_element(By.ID, "password").send_keys("PASSWORD")
# driver.find_element(By.ID, "login_button").click()

# Wait for the page to load
time.sleep(5)

# Retrieve cookies from the browser
cookies = driver.get_cookies()

# Combine cookies into a dictionary for use in requests
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

# Close the browser session
driver.quit()
