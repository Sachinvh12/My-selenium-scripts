'''
Created on 26-Mar-2019

@author: My PC
'''


from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://www.google.com")
print("first nav is completed")
driver.save_screenshot("C:\Users\My PC\Pictures\screenshot.png")
print("screenshot captured")