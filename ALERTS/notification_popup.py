from selenium import webdriver


ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
#initialize chrome
driver=webdriver.Chrome("C:\drivers\chromedriver.exe",options=ops)

#open url
driver.get("https://whatmylocation.com/")

#maximize the window
driver.maximize_window()

#close the window
driver.close()


