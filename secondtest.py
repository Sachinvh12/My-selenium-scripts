'''
Created on 26-Mar-2019

@author: My PC
'''
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")
print("first nav is completed")

driver.get("https://www.facebook.com")

print("second nav is completed")

driver.get("https://www.twitter.com")

print("third nav is completed")