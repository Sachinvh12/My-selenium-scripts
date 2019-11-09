'''
Created on 26-Mar-2019

@author: My PC
'''
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")
driver.execute_script("window.open('https://www.amazon.in','new window')")
print("amazon opened in new window")