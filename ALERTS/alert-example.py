from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
#initialize the chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

#open url
driver.get("http://www.dummypoint.com/Windows.html")

#maximize the window
driver.maximize_window()
'''
#alert-1
driver.find_element_by_name("alertbutton").click()
alert_button=driver.switch_to.alert
print(alert_button.text)
alert_button.accept()
'''

'''
#alert2 (confirm alert)
driver.find_element_by_name("confirmalertb").click()
alert_button=driver.switch_to.alert
print(alert_button.text)
alert_button.dismiss()

'''

#alert3 (promt alert)
driver.find_element_by_name("promtalertb").click()
confirm_promt_button=Alert(driver)
time.sleep(4)
confirm_promt_button.send_keys("I love Selenium")
time.sleep(5)
confirm_promt_button.accept()
time.sleep(4)

#close the window
driver.close()
