from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://itera-qa.azurewebsites.net/home/automation")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working with dropdown
dropdown=Select(driver.find_element(By.XPATH,"//select[@class='custom-select']"))

#total no of options available
alloptions=dropdown.options
print(len(alloptions))

#printing the text of all options
for opt in alloptions:
    print(opt.text)

#dropdown.select_by_visible_text("Spain")

dropdown.select_by_value("1")
time.sleep(2)

#dropdown.select_by_index(2)

for opt in alloptions:
    if opt.text=='Italy':
        opt.click()
        break

#close the window
driver.close()