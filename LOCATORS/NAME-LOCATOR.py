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

#locating the element by using id
search_bar=driver.find_element_by_id( "search_query_top").send_keys("Tshirt")


#locating the element by using name- method1
#submit=driver.find_element_by_name( "submit_search").click()
time.sleep(2)

#method2
submit=driver.find_element(By.NAME,"submit_search").click()

#close the page
driver.close()