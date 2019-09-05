'''
Created on Jul 31, 2019

@author: devac
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome('C:\\driver\\chromedriver.exe')
i=0
print(i)
while (i<=20):
    time.sleep(1)
    browser.get('http://msftconnecttest.com/redirect')
    i+=1
    UName=browser.find_element_by_name('username')#inspect element
    UName.send_keys(Keys.CONTROL,'a')
    UName.send_keys('ssbs',i)
    PWord=browser.find_element_by_name('password') #inspect element
    PWord.send_keys(Keys.CONTROL,'a')
    PWord.send_keys("ssbs",i)
    PWord.send_keys(Keys.ENTER)
print("connected to SSBS",i)
print("done")


