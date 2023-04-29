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
# driver.find_element(By.XPATH, "//a[normalize-space()='Qarz-E-Hasna']").click()
driver.get("https://alnafi.com/qarz-e-hasna")
sleep(5)
driver.find_element(By.XPATH, "//button[normalize-space()='Enroll / Renew']").click()

sleep(2)
driver.find_element(By.ID, "Guarantor's Full Name").send_keys("123456789@aA")
driver.find_element(By.ID, "Guarantor's Contact no").send_keys("123456789@aA")
driver.find_element(By.ID, "Temporary address").send_keys("123456789@aA")
driver.find_element(By.ID, "Permanent address").send_keys("123456789@aA")
driver.find_element(By.ID, "City").send_keys("123456789@aA")
driver.find_element(By.ID, "Select Career Track").send_keys("123456789@aA")
driver.find_element(By.ID, 'National ID Card').send_keys("123456789@aA")
driver.find_element(By.XPATH, "//*[contains(text(), 'Career Advancement Track for Qarz e Hasna')]").click()
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'Apply')]").click()
sleep(10)
time.sleep(2)
driver.close()
driver.quit()
print("test Completed")
