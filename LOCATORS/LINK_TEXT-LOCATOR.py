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

#locating the element using linktext-method1
#contact=driver.find_element_by_link_text("Contact us").click()
#time.sleep(2)

#method2
contact=driver.find_element(By.LINK_TEXT,"Contact us").click()
time.sleep(2)


#close the window
driver.close()