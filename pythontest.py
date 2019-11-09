'''
Created on 26-Mar-2019

@author: My PC
'''
import unittest 
from selenium import webdriver



class Traditionalway(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\My PC\\Downloads\\Compressed\\chromedriver")

    def test_google_search_page(self):
        driver=self.driver
        driver.get("https://www.google.com")


if __name__=="__main__":
    unittest.main()