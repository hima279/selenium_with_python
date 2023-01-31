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

#scroll  to bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
#scroll to top of the page
#driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

#scroll to top of the page
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")


#Clicking the specific element by using javascript
#best_sellers=driver.find_element(By.XPATH,"//a[@class='nav-a  '][2]")
#driver.execute_script("arguments[0].click();",best_sellers)

#scroll to particular element
#driver.execute_script("arguments[0].scrollIntoView(true);",best_sellers)

#close the window
driver.close()