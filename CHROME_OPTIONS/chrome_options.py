from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

#initialize the chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/anguarpractice/")

print(driver.title)