
This is a template for you to use to make your own website.
It's called "myapp" 

Your pictures go into the static directory. 

Your pages go into the templates directory

Currently the following pages exist:

index.html
keyboards.html

Currently the following images exist:

homebrew.png
teletype.jpg

You will change index.html to be the home page you want. 
First you will need to change the functional tests.

The functional tests look like this: 


(excerpt from functional_tests.py)

    def test_home_page(self):
        """

        Put your description of the purpose of your web site here.

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('The Title of my Web Site',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('homebrew.png',m.get_attribute('src'))

        # We check here for the title of your home page.
        # uncomment the next lines and change the text when you set your title.
        # put your title in place of "The Title of My Home Page"

        h=self.browser.find_element_by_css_selector('h1')
        self.assertIn("The Title of My Home Page",h.text)

        # There is an area specified around the computer keyboard.
        # the 'id' of this area is 'keyboard'

        # this is how we find that area.
        a=self.browser.find_element_by_id('keyboard')

        # this is how we click on it.
        a.click()

        # after clicking on it, we should see the next page.
        e=self.browser.find_element_by_css_selector("h1")
        self.assertIn('Keyboards',e.text)

        # The page should have a picture of a teletype machine. 
        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('teletype.jpg',m.get_attribute('src'))
    

