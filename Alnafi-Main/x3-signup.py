from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
# driver = webdriver.Chrome(executable_path="C:/Users/DELL")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://alnafi.com/sign-up")

driver.find_element(By.ID, 'userName').send_keys("ali101")
driver.find_element(By.ID, 'firstName').send_keys("ali")
driver.find_element(By.ID, 'lastName').send_keys("khan")
driver.find_element(By.ID, 'email').send_keys("xyz@@gmail.com")
driver.find_element(By.ID, 'password').send_keys("123456789@aA")
driver.find_element(By.ID, 'confirmPassword').send_keys("123456789@aA")
driver.find_element(By.ID, 'contact').send_keys("03030213155")
driver.find_element(By.ID, 'address').send_keys("karachi")
driver.find_element(By.CLASS_NAME, 'submit-btn').click()

sleep(10)
driver.close()
driver.quit()
print("test-Completed")

