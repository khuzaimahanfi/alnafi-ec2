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
driver.find_element(By.ID, "Username/ Email").send_keys("khuzaimakhan101")
sleep(5)
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
sleep(5)
driver.find_element(By.CLASS_NAME, 'px-6').click()
sleep(5)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)

driver.get("https://www.facebook.com/info.alnafi/")
sleep(4)
driver.get("https://twitter.com/AlNafi99")
sleep(4)
driver.get("https://www.tiktok.com/@alnafi00")
sleep(4)
driver.get("https://www.pinterest.com/AlNafi99/")
sleep(4)
driver.get("https://www.quora.com/profile/Al-Nafi-9")
sleep(4)
driver.get("https://www.youtube.com/c/AlNafi")
sleep(4)
driver.get("https://www.instagram.com/info.alnafi/")
sleep(4)
driver.get("https://www.linkedin.com/company/al-nafi/")
sleep(4)
time.sleep(2)
driver.close()
driver.quit()
print("test Completed")