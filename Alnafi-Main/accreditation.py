from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://alnafi.com/auth/signin")
driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")
sleep(5)
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
sleep(5)
driver.find_element(By.CLASS_NAME, 'px-6').click()
# accreditation
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
driver.get("https://alnafi.com/accreditation")
driver.find_element(By.CLASS_NAME, 'mt-6').click()
driver.find_element(By.CLASS_NAME, 'btn-primary').click()
sleep(20)
# driver.find_element(By.XPATH, "//a[normalize-space()='Click to navigate']").click()

sleep(20)
driver.close()
driver.quit()
print("test-Completed")
