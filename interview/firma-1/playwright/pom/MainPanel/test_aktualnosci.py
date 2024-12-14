import time;
from playwright.sync_api import Page

class Aktualnosci:
    def __init__(self, page: Page):
        self.id='Test-Aktualnosci'
        self.page = page
        
    def test_click(self):
        self.page.goto("https://czarnijaslo.pl/")
        time.sleep(5)
        aktualnosci = self.page.locator("#menu-menu-3 .menu-item-327")
        aktualnosci.click()
        self.page.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
        assert self.page.url =="https://czarnijaslo.pl/category/wydarzeniax/"
        
        
    
        
    