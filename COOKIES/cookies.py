from selenium import webdriver
from selenium.webdriver.common.by import By



#initialize the chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

#capture cookies from the browser
cookies=driver.get_cookies()


print("size of cookies:",len(cookies))

#print details of all cookies

for c in cookies:
    print(c)
    print(c.get('name'))
    print(c.get('name'),":",c.get('value'))

#Adding new cookie to the browser
cookie={'name':'Mycookie','value':'12345'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()

#print no of cookies after adding new cookie
print(len(cookies))

#print all the cookie pairs
print(cookies)


#Deleting cookie

driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()

#print no of cookies after deleting the cookie
print(len(cookies))

#Deleting all the cookies
driver.delete_all_cookies()

#capture all the cookies after deleting all cookies
cookies=driver.get_cookies()

print(len(cookies))

print(driver.title)