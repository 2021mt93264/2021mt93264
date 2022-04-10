from selenium import webdriver
import time

# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path='D:\\Roja Ramani\\Education\\BITS WILP\\1-2 Sem\\Introduction to DevOps\\Selenium\\chromedriver_win32\\chromedriver.exe')

# URL of the website

# opening link in the browser
driver.get("https://www.facebook.com/")
driver.maximize_window()

time.sleep(5)
driver.find_element_by_name("email").send_keys("roja.rose.16@gmail.com")
driver.find_element_by_name("pass").send_keys("abc")
driver.find_element_by_name("login").click()

logout=driver.find_element_by_class_name("j83agx80 l9j0dhe7")
logout.click()

time.sleep(5)
# driver.close()