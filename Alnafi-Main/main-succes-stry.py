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
driver.maximize_window()
driver.get("https://alnafi.com/auth/signin")
sleep(2)
driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")

driver.find_element(By.ID, 'Password').send_keys("123456789@aA")

driver.find_element(By.CLASS_NAME, 'px-6').click()
sleep(5)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
# driver.find_element(By.CLASS_NAME, 'py-4').click()
driver.find_element(By.XPATH, "//a[normalize-space()='Success Stories']").click()
sleep(10)
# driver.find_element(By.CLASS_NAME, 'carousel__icon').click()
# driver.find_element(By.XPATH, 'arrowRight').click()
# driver.find_element(By.XPATH, "//*[contains(text(), 'arrowRight')]").click()
sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(), 'View More')]").click()
sleep(5)
driver.execute_script("window.history.go(-1)")
driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div[3]/div/div/div/a').click()
time.sleep(2)
driver.close()
driver.quit()
print("test-Completed")
