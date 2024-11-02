from selenium import webdriver

class CoolDriver():
    driver = webdriver.Chrome()
    
    def __init__(self, name):
        self.name = name
        
    def open_web_page(self, url):
        print("Wchodze na " + url)
        self.driver.get(url)