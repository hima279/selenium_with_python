from selenium import webdriver
from selenium.webdriver.common.by import By


#initialize chrome driver
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

driver.implicitly_wait(10)

#open url
driver.get("https://www.google.com/")

#maximize the window
driver.maximize_window()

search_bar=driver.find_element(By.NAME,"q")
search_bar.send_keys("selenium")
search_bar.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

#close the windows
driver.quit()