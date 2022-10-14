from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

#initialize chrome driver
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")


#open url
driver.get("https://www.google.com/")

#maximize the window
driver.maximize_window()

search_bar=driver.find_element(By.NAME,"q")
search_bar.send_keys("selenium")
search_bar.submit()

wait=WebDriverWait(driver,10)

searchlink=wait.until(Ec.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

searchlink.click()


#close all windows
driver.quit()


