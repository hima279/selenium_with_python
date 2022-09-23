from selenium import webdriver
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#url launch
driver.get("https://www.amazon.com")
time.sleep(2)

#maximize the window
driver.maximize_window()
print(driver.title)

#url launch
driver.get("https://www.facebook.com")
time.sleep(2)


#maximize the window
driver.maximize_window()
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

#quit the browser
driver.quit()

