'''
Created on 26-Mar-2019

@author: My PC
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

DesiredCapabilities={}
DesiredCapabilities['Platform']='Windows'
DesiredCapabilities['BrowserName']='Firefox'
DesiredCapabilities['BrowserName']='Chrome'

driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")

driver2=webdriver.Firefox(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\geckodriver")
driver2.get("http://www.google.com")