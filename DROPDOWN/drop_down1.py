from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://testautomationpractice.blogspot.com/")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working on dropdown

files=Select(driver.find_element(By.XPATH,"//select[@id='files']"))
alloptions=files.options
print(len(alloptions))

files.select_by_index(1)

#close the window
driver.close()


