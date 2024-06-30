import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)


class TestExamples(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-errors")

        self.driver  = webdriver.Remote(
		command_executor="https://selenium.recruitcrm.net/wd/hub",
		desired_capabilities={
            "browserName": "chrome",
            "platformName": "Linux"
        },
        options=options,)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_one(self):
        try:
            driver = self.driver
            driver.get("https://google.com")
            print(driver.title)
            
            time.sleep(30)
        finally:
           logging.info("Test One : " + driver.session_id)
		   
    def test_two(self):
        try:
            driver = self.driver
            driver.get("https://google.com")
            print(driver.title)
            
            time.sleep(30)
        finally:
           logging.info("Test two : " + driver.session_id)

    def test_three(self):
        try:
            driver = self.driver
            driver.get("https://google.com")
            print(driver.title)
           
            time.sleep(30)
        finally:
           logging.info("Test three : " + driver.session_id)
			
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()