from selenium import webdriver
from selenium.webdriver.common.by import By


#initialize chrome driver
driver=webdriver.Chrome("C:\drivers\chromedriver.exe")

driver.implicitly_wait(10)

#open url
driver.get("https://demo.nopcommerce.com/")

#maximize the window
driver.maximize_window()

# click on link
#driver.find_element_by_link_text("Digital downloads ").click()
driver.find_element_by_partial_link_text("Digital").click()

links=driver.find_elements(By.XPATH,"//a")

#total no of links
print(len(links))

#print all the link names
for link in links:
    print(link.text)

#close the windows
driver.quit()