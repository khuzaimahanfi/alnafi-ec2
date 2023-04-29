import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

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
sleep(3)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)
# driver.get("https://alnafi.com/events")

# driver.find_element(By.XPATH, "//*[contains(text(), 'View Details')]").click()

# driver.find_element(By.ID, "enrollmentBtn").click()
sleep(3)
driver.find_element(By.ID, "Age").send_keys("20")
# driver.find_element(By.CLASS_NAME, "py-4 px-2").click()
# driver.find_element(By.CLASS_NAME, "Easypaisa").click()
# driver.find_element(By.ID, "Profession/ Student").send_keys("student")
dropdown = driver.find_elements(By.XPATH, "//select[@class='form-select border rounded-md shadow form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(dropdown)
select.select_by_value('easypaisa')
driver.find_element(By.ID, "Profession/ Student").send_keys("student")
driver.find_element(By.ID, "Institute Company").send_keys("kips")

driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()
sleep(10)
time.sleep(2)
driver.close()
driver.quit()
print("test Completed")
