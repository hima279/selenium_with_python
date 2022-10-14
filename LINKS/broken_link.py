from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests


#initialize chrome driver
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

driver.implicitly_wait(10)

#open url
driver.get("http://www.deadlinkcity.com/")

#maximize the window
driver.maximize_window()


links=driver.find_elements(By.XPATH,"//a")
count=0

#total no of links
#print(len(links))

#print all the link names
#for link in links:
 #   print(link.text)


for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"is broken link")
        count +=1
    else:
        print(url,"is valid link")

print("Total no of broken links:",count)

#close the windows
driver.quit()