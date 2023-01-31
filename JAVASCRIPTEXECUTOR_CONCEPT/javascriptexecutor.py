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

#Clicking the specific element by using javascript
best_sellers=driver.find_element(By.XPATH,"//a[@class='nav-a  '][2]")
driver.execute_script("arguments[0].click();",best_sellers)

#refresh the page
driver.execute_script("history.go(0);")

#get the title of the page
title=driver.execute_script("return document.title;")
print(title)

#alert
driver.execute_script("alert('hello selenium');")

#quit the window
driver.quit()