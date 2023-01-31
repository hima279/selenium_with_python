from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize the chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

#url launch
driver.get("https://opensource-demo.orangehrmlive.com/")

#maximize the window
driver.maximize_window()

#
username=driver.find_element(By.XPATH,"//input[@name='username']")
time.sleep(2)
username.click()
username.clear()


driver.execute_script("arguments[0].style.border='3px solid red'",username)

password=driver.find_element(By.XPATH,'//input[@name="password"]')
password.click()
password.clear()
driver.execute_script("arguments[0].style.border='3px solid red'",password)

LoginButton=driver.find_element(By.XPATH,"//button[@type='submit']")
driver.execute_script("arguments[0].style.border='3px solid red'",LoginButton)

driver.execute_script("arguments[0].setAttribute('value','Admin')",username)
driver.execute_script("arguments[0].setAttribute('value','admin123')",password)
driver.execute_script("arguments[0].click();",LoginButton)



