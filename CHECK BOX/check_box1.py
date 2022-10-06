from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize chorme
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

#maximize the window
driver.maximize_window()
time.sleep(2)

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option1':
        checkbox.click()
        break


#close the window
driver.close()