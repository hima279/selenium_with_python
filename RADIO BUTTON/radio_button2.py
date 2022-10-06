from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize Chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#maximize the window
driver.maximize_window()
time.sleep(2)

#radio button
driver.find_element(By.XPATH,"//input[@value='radio1']").click()
time.sleep(2)

#close the window
driver.close()


