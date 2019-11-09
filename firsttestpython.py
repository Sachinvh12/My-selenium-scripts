'''
Created on 25-Mar-2019

@author: My PC
'''
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")
print("first test is completed")                 