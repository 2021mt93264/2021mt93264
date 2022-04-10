from selenium import webdriver
import time

# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path='D:\\Roja Ramani\\Education\\BITS WILP\\1-2 Sem\\Introduction to DevOps\\Selenium\\chromedriver_win32\\chromedriver.exe')

# URL of the website

# opening link in the browser
driver.get("https://rahulshettyacademy.com/#/index") #Navigate to the Website
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='login-btn']/a[@class='theme-btn register-btn']").click()
time.sleep(5)

#Login to Portal
driver.find_element_by_name("email").send_keys("2021mt93264@wilp.bits-pilani.ac.in")
driver.find_element_by_name("password").send_keys("oneIlmg@12")
driver.find_element_by_name("commit").click()

time.sleep(3)

driver.find_element_by_xpath().click()

time.sleep(5)
# driver.close()