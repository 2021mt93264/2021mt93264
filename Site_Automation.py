from selenium import webdriver

# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path='D:\\Roja Ramani\\Education\\BITS WILP\\1-2 Sem\\Introduction to DevOps\\Selenium\\chromedriver_win32\\chromedriver.exe')

# URL of the website
#url = "https://www.geeksforgeeks.org/"

# opening link in the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()