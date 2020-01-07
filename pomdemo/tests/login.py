from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtUsername").send_keys("Admin")

driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()
time.sleep(1)
driver.find_element_by_id("welcome").click()

driver.find_element_by_link_text("Logout").click()

time.sleep(4)
driver.close()
driver.quit()
print("Test Completed Successfully")




