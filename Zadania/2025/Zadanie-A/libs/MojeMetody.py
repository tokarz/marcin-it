from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn


class MojeMetody:
    def custom_hover(self, locator):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        
        driver = seleniumlib.driver
        element = seleniumlib.find_element(locator)
        ActionChains(driver).move_to_element(element).perform()