from playwright.sync_api import Page


class Aktualnosci:
    def __init__(self, page: Page):
        self.page = page
       

    def click_aktualnosci(self):
        self.page.goto("https://czarnijaslo.pl/")
        self.page.locator("#menu-menu-3").get_by_role("link", name="Aktualności").click()
        self.page.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
        assert self.page.url == "https://czarnijaslo.pl/category/wydarzenia/"
        print ("OK")
        
        
    
        
    