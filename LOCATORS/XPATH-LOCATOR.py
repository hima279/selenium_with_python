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

'''xpath structure

 //tagname[@attribute='value']  
 
 '''

#locating searchbar method 1 - relative xpath
search_bar=driver.find_element_by_xpath('//input[@id="search_query_top"]').click()

#method 2 - relative xpath
#search_bar=driver.find_element(By.XPATH, '//input[@id="search_query_top"]').click()
#time.sleep(2)

#method 3 - absolute path
#search_bar=driver.find_element(By.XPATH,"html/body/div/div/header/div[3]/div/div/div[2]/form/input[4]")
#time.sleep(2)

#or - method
#search_bar=driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
#time.sleep(2)


# and - method
#submit=driver.find_element(By.XPATH,"//button[@name='submit_search' and @class='btn btn-default button-search']").click()
#time.sleep(2)


#close the page
driver.close()