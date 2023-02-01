from selenium import webdriver
import time
import os

# initialize chrome
driver = webdriver.Chrome("C:\drivers\chromedriver.exe")

# url launch
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

driver.save_screenshot(os.getcwd()+"\\homepage.png")
# maximize window
driver.maximize_window()

#close the window
driver.close()