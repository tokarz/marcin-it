from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

class MojeMetody:

    def __init__(self):
        self.selenium = BuiltIn().get_library_instance("SeleniumLibrary")

    def hover_and_click(self, selector1 , selector2):
       
        driver = self.selenium.driver

        element1 = self.selenium.find_element(selector1)
        ActionChains(driver).move_to_element(element1).perform()

        self.selenium.wait_until_element_is_visible(selector2, timeout=5)
        self.selenium.click_element(selector2)

    
    def scroll_and_click(self, selector, timeout):
        driver = self.selenium.driver

        element = self.selenium.find_element(selector)
        
        driver.execute_script("arguments[0].scrollIntoView();", element)
        
        time.sleep(timeout)

        self.selenium.click_element(selector)
        





####CZARNI JASLO  bo na meczykach nie ma wyszukiwarki 
    def  search_and_select(self, text):
        
        search = self.selenium.find_element(".tdb-search-icon")
        search.click()

        search_field = self.selenium.find_element(".tdb-head-search-form-input")
        search_field.click()
        search_field.send_keys(text)

        time.sleep(3)
    
        wyszukane = self.selenium.find_elements(".td-category-pos-above .entry-title")
        wyszukany1 = wyszukane[0]
        wyszukany1.click()
