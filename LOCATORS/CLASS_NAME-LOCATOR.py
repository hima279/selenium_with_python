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



#if we have more than one element then we use classname - method1
slider=driver.find_elements_by_class_name("homeslider-container")
print(len(slider))
time.sleep(2)

#method 2
#slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
#print(len(slider))

# close the page
driver.close()