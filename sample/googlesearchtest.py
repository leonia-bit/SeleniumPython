"""File name:
        googlesearchtest.py
   Description:
        * play 2 selenium simple scenario on google search page
        * tests scenario's results using python unittest functionality
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  unittest import TestCase
import time


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation_stepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)

    def test_search_automation_stepbystep_jenkins(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step Jenkins")
        self.driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed Successfully")


if __name__ == '__main__':
    unittest.main()