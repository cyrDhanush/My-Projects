from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome("D:\GIT\Web Drivers\chromedriver.exe")
driver.get('https://classroom.google.com/u/0/h')

Email=driver.find_element_by_id('identifierId')
text = "av4764@srmist.edu.in"
for character in text:
    Email.send_keys(character)
    time.sleep(0.3)
time.sleep(2)
Next=driver.find_element_by_class_name('VfPpkd-vQzf8d')
ActionChains(driver).move_to_element(Next).click().click().perform()

