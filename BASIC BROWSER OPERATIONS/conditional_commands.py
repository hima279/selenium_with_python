from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#url launch
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
time.sleep(2)

#These  commands will return true/false and are accessed only through web element.

#is_displayed() is to check particular element is available on particular webpage or not.
# is_enabled() is to check particular element is available or not.

searchbox=driver.find_element(By.XPATH,'//input[@id="small-searchterms"]')
print(searchbox.is_displayed())
print("Enable status:",searchbox.is_enabled())
time.sleep(2)

#is_selected() is used for radio buttons, check boxes
rd_male=driver.find_element(By.XPATH,'//input[@id="gender-male"]')
rd_female=driver.find_element(By.XPATH,'//input[@id="gender-female"]')
print(rd_male.is_selected())
print(rd_female.is_selected())

#select the male radio button
rd_male.click()
time.sleep(2)

print("After selecting male radio button:", rd_male.is_selected())
print(rd_female.is_selected())

#close the webpage
driver.close()



