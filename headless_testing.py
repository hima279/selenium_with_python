from selenium import webdriver

#headless mode by using chrome
options=webdriver.ChromeOptions()

#method 1
options.headless=True

#method 2
#options.add_argument('--headless')

# incognito mode
#options.add_argument('--incognito')

#initialize the browser
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe",options=options)


#open url
driver.get("https://www.amazon.com/")

print(driver.title)

#close the window
driver.close()
