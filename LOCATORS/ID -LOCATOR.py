from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#url launch
driver.get("http://automationpractice.com/index.php")
time.sleep(2)

#maximize window
driver.maximize_window()

#locating searchbar by using id
# method 1
#search_bar=driver.find_element(By.ID,"search_query_top").click()
#time.sleep(2)

#method 2
search_bar=driver.find_element_by_id( "search_query_top").click()
time.sleep(2)

#close the page
driver.close()