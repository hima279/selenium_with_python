from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

#open url
driver.get("https://mypage.rediff.com/login/dologin")

#maximize the window
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(2)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

