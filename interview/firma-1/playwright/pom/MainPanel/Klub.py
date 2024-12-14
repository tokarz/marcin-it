import time;
from playwright.sync_api import Page

class Klub:
    def __init__(self, page: Page):
        self.id='Test-Aktualnosci'
        self.page = page
        
    def click_club(self):
        self.page.goto("https://czarnijaslo.pl/")
        aktualnosci = self.page.locator("#menu-menu-3 .menu-item-327")
        aktualnosci.click()
        self.page.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
        return self.page.url
        
    def click_wladze(self):
        self.page.goto("https://czarnijaslo.pl/")
        aktualnosci = self.page.locator("#menu-menu-3 .menu-item-327")
        aktualnosci.click()
        self.page.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
        assert self.page.url =="https://czarnijaslo.pl/category/wydarzenia/"
   
        
        
    
        
    