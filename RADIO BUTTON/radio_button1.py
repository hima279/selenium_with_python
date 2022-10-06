from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://demo.nopcommerce.com/register")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working with radio button
male_button=driver.find_element_by_id("gender-male").click()
male_button=driver.find_element_by_id("gender-male").is_selected()
time.sleep(3)
print(male_button)

#close the window
driver.close()




