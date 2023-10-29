from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Drag:

    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

 # Access the Given url 

    def breach_into(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(10)
        except Exception as e:
            print("url erron: ",e)

# Access the iframe for getting the another part of the webpage 

    def iframe(self):
        try:
            self.breach_into()
            ifra = self.driver.find_element(by=By.CSS_SELECTOR,value='iframe[src="/resources/demos/droppable/default.html"]')
            self.driver.switch_to.frame(ifra)
        except Exception as f:
            print("iframe error on: ", f)

# Get the Draggable element and perform drag & drop 
        
    def drag_drop(self):
        try:
            self.iframe()
            dra_ele = self.driver.find_element(by=By.ID, value= "draggable")
            dro_ele = self.driver.find_element(by=By.ID, value= "droppable")
            action = ActionChains(self.driver)
            action.drag_and_drop(dra_ele, dro_ele).perform()
            sleep(5)

        except Exception as d:
            print("drag error on: ",d)

# Validate the Accessed Drag & Drop element  
        
    def validate(self):
        try:
            dro_tex = self.driver.find_element(by=By.CSS_SELECTOR, value='#droppable p').text
            if "Dropped!" in dro_tex:
                print("Verification successful. Text in droppable element: " + dro_tex)
            else:
                print("Verification failed. Text in droppable element: " + dro_tex)

        except Exception as v:
            print("Validation error: ", v)

        finally:
            self.driver.switch_to.default_content()
            self.driver.quit()

# Create a obj to call the methods from class 

url = "https://jqueryui.com/droppable/"
d = Drag(url)
d.drag_drop()
d.validate()