from selenium.common.exceptions import StaleElementReferenceException
from robot.libraries.BuiltIn import BuiltIn

class Clicker:
    def click_xpath(self , selektor):
        """Prints a message with a timestamp and returns it."""
        selenium_lib = BuiltIn().get_library_instance("SeleniumLibrary")
        driver = selenium_lib.driver
        element = driver.find_element("xpath", selektor)
        element.click()