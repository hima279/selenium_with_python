from selenium import webdriver
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#url launch
driver.get("https://www.amazon.com")

#refresh website
driver.refresh()
time.sleep(2)

#maximize window
driver.maximize_window()
time.sleep(2)

#get page title
print('The current URL is: ' + driver.title)

#minimize window
driver.minimize_window()

#go forward
driver.forward()
time.sleep(2)

#go back
driver.back()
time.sleep(2)

#close the page
driver.close()
print('The page was closed successfully')
