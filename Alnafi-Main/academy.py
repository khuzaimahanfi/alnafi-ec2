from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
# driver = webdriver.Chrome(executable_path="C:/Users")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://alnafi.com/auth/signin")
driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")
sleep(5)
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
sleep(5)
driver.find_element(By.CLASS_NAME, 'px-6').click()
sleep(10)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
driver.get("https://alnafi.com/academy")
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Add to Cart')]").click()
sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(), 'Go to Cart')]").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'Checkout')]").click()
sleep(10)
driver.find_element(By.ID, 'easypaisa_number_input').send_keys("03162772106")
sleep(10)
driver.find_element(By.XPATH, "//*[contains(text(), 'Pay')]").click()
sleep(10)
time.sleep(2)
driver.close()
driver.quit()
print("test Completed")
