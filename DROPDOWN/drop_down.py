from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")


#open url
driver.get("https://www.opencart.com/index.php?route=account/register")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working with dropdown
country=driver.find_element(By.XPATH,"//select[@id='input-country']")
country_ele=Select(country)

#or
country=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select option from the dropdown

#country.select_by_index(13)
#country.select_by_value("10")
country.select_by_visible_text("India")



#select all options
options=country.options
print("Total number of options:",len(options))

for opt in options:
    print(opt.text)

#select the option without using select

for opt in options:
    if opt.text=="India":
        opt.click()
        break

#close the window
driver.close()