from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize chrome
driver = webdriver.Chrome("C:\drivers\chromedriver.exe")

# url launch
driver.get("http://automationpractice.com/index.php")
time.sleep(2)

# maximize window
driver.maximize_window()

#tag name
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
#close the window
driver.close()