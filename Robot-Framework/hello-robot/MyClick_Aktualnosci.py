from SeleniumLibrary import SeleniumLibrary

class MyClick_Aktualnosci(SeleniumLibrary):
    def Kliknij_Na_Aktualnosci(self):
        """Clicks on an element with the given class name."""
        locator = f"css:#menu-menu-3 .meni-item-327"
        self.click_element(locator)