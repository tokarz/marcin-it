from playwright.sync_api import sync_playwright




class Utilities:
    def __init__(self):
        self.id = "utilis"
    
    def czarnijaslo(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://czarnijaslo.pl/")
    
    def wait_for_url(self, url):
        self.page.wait_for_url == url
            
        
    def asercja(self, url):
        assert self.page.url == url
        self.page.close()
        print("OK")

    def close(self):
        self.page.close()
    
    def click_aktualnosci(self):
        page = self.czarnijaslo()
        aktualnosci = page.locator("#menu-menu-3").get_by_role("link", name="Aktualności")
        aktualnosci.click()
        self.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
        self.asercja("https://czarnijaslo.pl/category/wydarzenia/")
        self.close()

    def click_sponsorzy(self):
        page = self.czarnijaslo()
        sposnoring = page.locator(".td_spot_img_all")
        sposnoring.click()
        self.wait_for_url("https://czarnijaslo.pl/")
        self.asercja("https://czarnijaslo.pl/")
        self.close()


    def click_stopka_mojejaslo(self):
        page = self.czarnijaslo()
        stopka_moje_jaslo = page.locator("aside").filter(has_text="Zaprzyjaźnione media").get_by_role("link")
        stopka_moje_jaslo.click()
        self.wait_for_url("https://mojejaslo.pl/")
        self.asercja("https://mojejaslo.pl/")
        self.close()


    def click_tabela_sokol_kolbuszowa(self):
        page = self.czarnijaslo()
        stopka_moje_jaslo = page.locator("aside").filter(has_text="Zaprzyjaźnione media").get_by_role("link")
        stopka_moje_jaslo.click()
        self.wait_for_url("https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/")
        self.asercja("https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/")
        self.close()


  



  


util = Utilities()

util.click_aktualnosci()

