from selenium import webdriver
import time


# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path='D:\\Roja Ramani\\Education\\BITS WILP\\1-2 Sem\\Introduction to DevOps\\Selenium\\chromedriver_win32\\chromedriver.exe')

# URL of the website
# opening link in the browser
driver.get("https://rahulshettyacademy.com/") #Navigate to the Website
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='login-btn']/a[@class='theme-btn register-btn']").click()#Identified webelement using Xpath
time.sleep(5)
#Login to Portal
driver.find_element_by_name("email").send_keys("2021mt93264@wilp.bits-pilani.ac.in")
driver.find_element_by_name("password").send_keys("oneIlmg@12")
driver.find_element_by_name("commit").click()
time.sleep(3)
driver.find_element_by_xpath("(//div[@class='navbar-collapse collapse clearfix']/ul/li/a[contains(text(),'Practice')])[1]").click()
driver.find_element_by_name("name").send_keys("Roja")
driver.find_element_by_name("email").send_keys("2021mt93264@wilp.bits-pilani.ac.in")
time.sleep(8)
driver.find_element_by_xpath("(//div[@class='form-group col-md-12 col-sm-12 col-xs-12']/button[contains(text(),'Submit')])[1]").click()#Identified webelement using Xpath
time.sleep(5)
driver.find_element_by_xpath("//div[@class='projects-item']/a[contains(text(),'Automation Practise - 2')]").click()#Identified webelement using Xpath
# driver.close()
time.sleep(8)
WebElement = driver.find_element_by_xpath("//*[(//table[@id='product'])[2]/tbody/tr[3]")
rowtext = WebElement.getText()
print("Third row of table : "+rowtext)
WebElement = driver.find_element_by_xpath("//*[(//table[@id='product'])[2]/tbody/tr/td[2]")
valueIneed = WebElement.getText()
print("Cell value is : " + valueIneed)