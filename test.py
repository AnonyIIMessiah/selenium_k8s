from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the Selenium Grid hub
grid_url = "https://selenium.recruitcrm.net/wd/hub"  # Replace with the actual host

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need a UI
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create a new session on the Selenium Grid
driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)

try:
    # Open a webpage
    driver.get("http://www.google.com")

    # Print page source for debugging
    print(driver.page_source)

    # Wait for the element to be present (increase wait time)
    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.presence_of_element_located((By.NAME, "q")))  # Adjust the selector as per the target website

    # Perform some actions (e.g., find an element and interact with it)
    element.send_keys("Selenium Grid")
    element.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(5)

    # Print the title of the current page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()
