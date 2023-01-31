from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize the chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

#url launch
driver.get("https://www.amazon.in/")


#maximize the window
driver.maximize_window()
time.sleep(2)

#locating an element
#best_sellers=driver.find_element(By.XPATH,"//a[@class='nav-a  '][2]")
fashion=driver.find_element(By.LINK_TEXT,"Fashion")


#creating a border
driver.execute_script("arguments[0].style.border='3px solid red'",fashion)
time.sleep(2)

#close the window
#driver.close()