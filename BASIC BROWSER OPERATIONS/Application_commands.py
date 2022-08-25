from selenium import webdriver
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#url launch
driver.get("https://www.amazon.com")
time.sleep(2)

#These commands are accessed only through driver instance.

#captures the title of the current webpage
print(driver.title)

#captures the current url of the webpage
print(driver.current_url)

#returns the html page of the application
print(driver.page_source)

#It will close all the browsers
driver.quit()
