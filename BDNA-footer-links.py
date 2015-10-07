# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

links  = {
     'About BDNA' : 'About BDNA',
     'Blog': 'Blog',
     'Careers': 'Careers',
     'News and Events': 'News and Events',
     'Do IT Right': 'Do IT Right',
    }
    
    
class BDNALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.bdna.com/'
        self.verificationErrors = []    
        
        
    def test_BDNA_links(self):
        driver = self.driver

        for link in links:
            driver.get(self.base_url)
            driver.find_element_by_link_text(link).click()                          
            expected_title = links[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e)) 
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()        
            



            
        