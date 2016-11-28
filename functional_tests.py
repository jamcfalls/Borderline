# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome("c:\Python34\chromedriver.exe")
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        It's difficult to have a healthy, loving relationships when living with borderline personality disorder.
        This website examines BPD in sisterhood and it's ups and downs. It explores the mental struggles of living with BDP and
        intertwines it's interactions in sisters. The main topics represented are BPD symptoms, such as impulsivity, black and white thinking,
        and depression, and sisterhood. Being sisters with someone with BDP is a hectic lifestyle, but ultimately ends in love. 
        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Loving With BPD',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('home.jpg',m.get_attribute('src'))

        a=self.browser.find_element_by_id('home')
        a.click()

        #around the girls there is a clickable area
        self.browser.get('http://localhost:8000/index.html')
        a=self.browser.find_element_by_id('home')
        #when I click on the girls, I get the handsup page
        a.click()
        

        self.assertIn('handsup',self.browser.title)

        h=self.browser.find_element_by_tag_name('h1')
        m=self.browser.find_element_by_tag_name('img')
        
        # the user goes back to the homepage
        self.browser.get('http://localhost:8000/index.html')
        # the user sees at the bottom of the page a link to credits
        l=self.browser.find_element_by_link_text('Credits')
        # the user clicks on the credits link
        l.click()

        # and sees the credits.html page
        a=self.browser.current_url
        self.assertIn("Credits",a)
       

if __name__=="__main__":
        unittest.main(warnings="ignore")
