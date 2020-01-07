from selenium import webdriver
import time
import unittest


class LoginPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(1)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(4)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed Successfully")
