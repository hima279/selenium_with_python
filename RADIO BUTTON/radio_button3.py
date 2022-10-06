from selenium import webdriver
from selenium.webdriver.common.by import By

#initialize the window
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#maximize the window
driver.maximize_window()



radio_buttons=driver.find_elements(By.XPATH, "//input[@name='radioButton']")
radio_buttons[2].click()

#close the window
driver.close()


