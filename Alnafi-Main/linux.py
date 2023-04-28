from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")


# driver = webdriver.Chrome(executable_path="C:/Users/DELL")
driver.implicitly_wait(10)
# driver.maximize_window()
driver.get("https://alnafi.com/auth/signin")

driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
sleep(5)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='courses']").click()
sleep(5)
driver.find_element(By.XPATH, "//a[@href='/courses/linux']").click()
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Add to Cart')]").click()
sleep(1)
driver.find_element(By.XPATH, "//*[contains(text(), 'Go to Cart')]").click()
sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(), 'Rs 5000')]")
sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(), 'Rs 5000')]").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'Checkout')]").click()
sleep(5)
time.sleep(2)
driver.close()
driver.quit()
print("test-Completed")
