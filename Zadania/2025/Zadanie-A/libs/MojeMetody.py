from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
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
            seleniumlib.wait_until_element_is_visible(selector2, timeout=5)
            seleniumlib.click_element(selector2)
        except Exception as e:
    # This block will handle the ZeroDivisionError exception
            print(f"Error occurred: {e}")

    def custom_click(self, locator):
        try:
            seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")

        # Wait for the element to be visible and interactable
            seleniumlib.wait_until_element_is_visible("a[href='/newsy']", timeout=5)
            

        # Now click the element using the locator directly
            seleniumlib.click_element("a[href='/newsy']")
            time.sleep(3)

        except Exception as e:
        # This block will handle any exceptions and print the error
            print(f"Error occurred: {e}")


        