from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#maximize the window
driver.maximize_window()
time.sleep(2)

#working with dropdown
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Ind")
time.sleep(2)
dropdown=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
print(len(dropdown))

#printing the all options
for country in dropdown:
    print(country.text)
    if country == 'India':
        country.click()
        break


time.sleep(2)

# extract the dynamically typed data
print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.XPATH,"//input[@id='autosuggest']") == 'India'
#close the window
driver.close()