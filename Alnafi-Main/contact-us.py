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
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
sleep(5)
driver.find_element(By.CLASS_NAME, 'px-6').click()
sleep(10)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
driver.get("https://alnafi.com/contact")
sleep(5)
driver.find_element(By.ID, 'firstName').send_keys("khuzaima")
driver.find_element(By.ID, 'lastName').send_keys("fanfic")
driver.find_element(By.ID, 'email').send_keys("hanfi.k99@gmail.com")
driver.find_element(By.XPATH, "//input[@id= 'contactNo']").send_keys("03030213157")
driver.find_element(By.ID, 'message').send_keys("You can use these text message marketing examples to easily put together your own templates and send ready-to-use messages to your customers.")
driver.find_element(By.ID, 'checkPolicy').click()
sleep(5)
driver.find_element(By.XPATH, "//button[normalize-space()='Send Message']").click()
sleep(15)
time.sleep(2)
driver.close()
driver.quit()
print("test Completed")
