from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://alnafi.com/auth/signin")

driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(20)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(20)
driver.get("https://alnafi.com/courses/hidden")
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Add to Cart')]").click()
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Go to Cart')]").click()
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Rs 1')]")
sleep(5)
driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[2]/aside/a').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="easypaisa_number_input"]').send_keys("03162772104")
sleep(5)
driver.find_element(By.CLASS_NAME, 'btn-primary').click()
sleep(120)
time.sleep(2)

assert "successful"

driver.quit()
print("test-Completed")
