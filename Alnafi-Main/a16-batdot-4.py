from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.implicitly_wait(10)

# URL of the visiting site
driver.get("https://alnafi.com/auth/signin")

# AUTH Credentials
driver.find_element(By.ID, "Username/ Email").send_keys("hanfi.kh99@gmail.com")
driver.find_element(By.ID, 'Password').send_keys("123456789@aA")
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
sleep(5)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='flex item-center justify-end cursor-pointer absolute top-0 right-0 p-4 z-40']//*[name()='svg']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='tracks']").click()
time.sleep(5)

driver.get("https://alnafi.com/tracks/batdot")
# driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[2]/a[2]/div[1]/div[2]").click()
time.sleep(5)

# eighteen_month_price
eighteen_month_price = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[1]')
time.sleep(2)
eighteen_month_act_price = "Rs Rs 395,000"
time.sleep(2)
assert eighteen_month_act_price == eighteen_month_price.text, "Text not found in the element"
time.sleep(2)

# yearly price
yearly_price = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[2]')
time.sleep(2)
yearly_act_price = "Rs Rs 263,333"
time.sleep(2)
assert yearly_act_price == yearly_price.text, "Text not found in the element"
time.sleep(2)

# half-yearly price
half_yearly_price = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[2]/h3')
time.sleep(2)
half_yearly_act_price = "Rs 131,667"
time.sleep(2)
assert half_yearly_act_price == half_yearly_price.text, "Text not found in the element"
time.sleep(2)

# quarterly price
quarterly_price = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[3]/h3')
time.sleep(2)
quarterly_act_price = "Rs 65,833"
time.sleep(2)
assert quarterly_act_price == quarterly_price.text, "Text not found in the element"
time.sleep(2)

# monthly price
monthly_price = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[4]/h3')
time.sleep(2)
monthly_act_price = "Rs 24,000"
time.sleep(2)
assert monthly_act_price == monthly_price.text, "Text not found in the element"
time.sleep(2)

# Examination fees
# examination_fees = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section[1]/div/div[1]/div[2]/div[5]/span')
# time.sleep(2)
# exam_act_price = "300 Pound"
# time.sleep(2)
# assert exam_act_price == examination_fees.text, "Text not found in the element"
# time.sleep(2)

# add to cart process
for i in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
time.sleep(5)
# add to cart buttons
eighteen_month_btn = driver.find_element(By.XPATH, "(//button[contains(text(),'Choose plan')])[1]")
yearly_btn = driver.find_element(By.XPATH, "(//button[contains(text(),'Choose plan')])[2]")
half_yearly_btn = driver.find_element(By.XPATH, "(//button[@id='enrollmentBtn'])[3]")
quarterly_btn = driver.find_element(By.XPATH, "(//button[contains(text(),'Choose plan')])[4]")
monthly_btn = driver.find_element(By.XPATH, "(//button[contains(text(),'Choose plan')])[5]")

# eighteen months cart
eighteen_month_btn.click()
time.sleep(5)
lang_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select rounded-md form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(lang_dropdown)
select.select_by_index(0)
driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='bg-Bluish px-12 py-4 text-white rounded-lg'][normalize-space()='Go to cart'])[2]").click()
time.sleep(5)
eighteen_month_cart = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[1]/div[1]/div/div[1]/div[2]/div/p')
assert half_yearly_act_price == eighteen_month_cart.text, "Text not found in the element"
# empty cart
cross_prod_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[1]")
cross_prod_1.click()
cross_prod_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[2]")
cross_prod_2.click()
time.sleep(5)

driver.back()
# half-yearly cart
half_yearly_btn.click()
time.sleep(5)
lang_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select rounded-md form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(lang_dropdown)
select.select_by_index(0)
driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='bg-Bluish px-12 py-4 text-white rounded-lg'][normalize-space()='Go to cart'])[2]").click()
time.sleep(5)
half_yearly_cart = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[1]/div[1]/div/div[1]/div[2]/div/p')
assert half_yearly_act_price == half_yearly_cart.text, "Text not found in the element"
# empty cart
cross_prod_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[1]")
cross_prod_1.click()
cross_prod_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[2]")
cross_prod_2.click()
time.sleep(5)

driver.back()
# yearly cart
time.sleep(5)
yearly_btn.click()
time.sleep(5)
lang_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select rounded-md form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(lang_dropdown)
select.select_by_index(0)
driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='bg-Bluish px-12 py-4 text-white rounded-lg'][normalize-space()='Go to cart'])[2]").click()
time.sleep(5)
yearly_cart = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[1]/div[1]/div/div[1]/div[2]/div/p')
assert yearly_act_price == yearly_cart.text, "Text not found in the element"
# empty cart
cross_prod_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[1]")
cross_prod_1.click()
cross_prod_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[2]")
cross_prod_2.click()
time.sleep(5)

driver.back()
# quarterly cart
time.sleep(5)
quarterly_btn.click()
time.sleep(5)
lang_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select rounded-md form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(lang_dropdown)
select.select_by_index(0)
driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='bg-Bluish px-12 py-4 text-white rounded-lg'][normalize-space()='Go to cart'])[2]").click()
time.sleep(5)
quarterly_cart = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[1]/div[1]/div/div[1]/div[2]/div/p')
assert quarterly_act_price == quarterly_cart.text, "Text not found in the element"
# empty cart
cross_prod_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[1]")
cross_prod_1.click()
cross_prod_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[2]")
cross_prod_2.click()
time.sleep(5)

driver.back()
# monthly cart
monthly_btn.click()
time.sleep(5)
lang_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select rounded-md form-select-lg appearance-none block w-full py-4 px-2 text-xs font-light text-doveGrey bg-white bg-clip-padding bg-no-repeat transition ease-in-out m-0 focus:text-balticSea focus:bg-white focus:border-b focus:border-Bluish focus:outline-none']")
select = Select(lang_dropdown)
select.select_by_index(0)
driver.find_element(By.XPATH, "(//button[normalize-space()='Add to Cart'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "(//a[@class='bg-Bluish px-12 py-4 text-white rounded-lg'][normalize-space()='Go to cart'])[2]").click()
time.sleep(5)
monthly_cart = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/main/section[1]/div[1]/div/div[1]/div[2]/div/p')
assert monthly_act_price == monthly_cart.text, "Text not found in the element"
# empty cart
cross_prod_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[1]")
cross_prod_1.click()
cross_prod_2 = driver.find_element(By.XPATH, "(//span[contains(text(),'x')])[2]")
cross_prod_2.click()
time.sleep(5)

driver.quit()
