'''
Created on 26-Mar-2019

@author: My PC
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usernameStr = 'sachin.hiremath121999@gmail.com'
passwordStr = 'qwerty@123'

browser = webdriver.Chrome(executable_path="C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))


username = browser.find_element_by_id('Email')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('next')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_id('signIn')
signInButton.click()
