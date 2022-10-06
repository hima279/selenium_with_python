from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize chrome
driver = webdriver.Chrome("C:\drivers\chromedriver.exe")

# url launch
driver.get("http://automationpractice.com/index.php")
time.sleep(2)

# maximize window
driver.maximize_window()

''' CSS structure

 tagname[attribute='value']  

 '''

# locating searchbar method 1
#search_bar=driver.find_element_by_css_selector("input[id='search_query_top']").click()

# method 2
#search_bar=driver.find_element(By.CSS_SELECTOR, "input[id='search_query_top']").click()
time.sleep(2)

'''
css selector structure
#value - when we have id
'''
#logo=driver.find_element_by_css_selector("#header_logo").click()
time.sleep(2)

'''
css selector structure
.value - when we have class
'''
signin=driver.find_element_by_css_selector(".login").click()
time.sleep(2)

# close the page
driver.close()