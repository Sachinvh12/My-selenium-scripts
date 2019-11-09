'''
Created on 26-Mar-2019

@author: My PC
'''

from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")
driver.refresh()
driver.forward()
driver.get("https://www.bing.com")
driver.refresh()
driver.back()
driver.get("https://www.ask.com")
print("all websites visited!")