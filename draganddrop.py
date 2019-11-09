'''
Created on 26-Mar-2019

@author: My PC
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyodbc import drivers
driver=webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
driver.get("http://jqueryui.com/droppable/")

driver.implicitly_wait(3)
driver.switch_to_frame(0)

source=driver.find_element_by_id("draggable")
target=driver.find_element_by_id("droppable")
ActionChains(driver).drag_and_drop(source, target).perform()

print("drag and drop completed!")