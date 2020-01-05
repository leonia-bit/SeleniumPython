"""File name:
    test1.py
    Description:
        a. Adding different types of drivers to project
        b. Running selenium simple test from pycharm and cli
        c. Running diff types of browsers for google.com
           with simple selenium functionality
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("../drivers/chromedriver.exe")
# driver  = webdriver.Firefox()
# driver = webdriver.Ie("../drivers/IEDriverServer.exe")
#
driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_xpath("//*[@id=\"tsf\"]/div[2]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
driver.maximize_window()
driver.refresh()
print("Test Completed Successfully")
time.sleep(4)
driver.quit()

