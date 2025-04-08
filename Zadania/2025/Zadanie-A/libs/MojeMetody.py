from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MojeMetody:
    
    def custom_hover(self, locator):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        time.sleep(10)
        try:
    # Try to divide by zero to raise an exception
            driver = seleniumlib.driver
            element = seleniumlib.find_element(locator)
            ActionChains(driver).move_to_element(element).perform()
        except Exception as e:
    # This block will handle the ZeroDivisionError exception
            print(f"Error occurred: {e}")


    def hover_and_click(self, selector1 , selector2):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        
        try:
            driver = seleniumlib.driver
            element1 = seleniumlib.find_element(selector1)
            
            ActionChains(driver).move_to_element(element1).perform()
            
            wait = WebDriverWait(driver, 10)
            sub_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector2)))
            
            #seleniumlib.wait_until_element_is_visible(selector2, timeout=2)
            sub_item.click()
        except Exception as e:
    # This block will handle the ZeroDivisionError exception
            print(f"Error occurred: {e}")

    def custom_click(self, locator):
        try:
            seleniumLib = BuiltIn().get_library_instance("SeleniumLibrary")
            time.sleep(1)
            seleniumLib.click_element(locator)
        except Exception as e:
        # This block will handle any exceptions and print the error
            print(f"Error occurred: {e}")


        