from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working with dropdown
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
alloptions=dropdown.options
print(len(alloptions))

#printing the all options
for opt in alloptions:
    print(opt.text)

#dropdown.select_by_index(1)
#dropdown.select_by_value('option1')
dropdown.select_by_visible_text("Option2")
time.sleep(2)

#close the window
driver.close()