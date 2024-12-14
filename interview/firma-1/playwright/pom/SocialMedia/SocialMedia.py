from playwright.sync_api import Page


class SocialMedia:
    def __init__(self , page : Page):
        self.page = page


    def click_facebook(self):
        self.page.goto("https://czarnijaslo.pl/")
        selektor = self.page.locator(".tdm-social-item")
        selektor.nth(0).click()
        self.page.wait_for_url("https://www.facebook.com/czarnijaslo1910/")
        assert self.page.url == "https://www.facebook.com/czarnijaslo1910/"
        print("OK")


   
    def click_instagram(self): 
        self.page.goto("https://czarnijaslo.pl/")
        selektor = self.page.locator(".tdm-social-item")
        selektor.nth(1).click()
        self.page.wait_for_url("https://www.instagram.com/czarni_1910_jaslo/")
        assert self.page.url == "https://www.instagram.com/czarni_1910_jaslo/"
        print("OK")

    
    
    def click_x(self): 
        self.page.goto("https://czarnijaslo.pl/")
        selektor = self.page.locator(".tdm-social-item")
        selektor.nth(2).click()
        self.page.wait_for_url("https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910")
        assert self.page.url == "https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910"
        print("OK")

   
   
    def click_yt(self):
        self.page.goto("https://czarnijaslo.pl/")
        selektor = self.page.locator(".tdm-social-item")
        selektor.nth(3).click()
        self.page.wait_for_url("https://www.youtube.com/channel/UCrk8GobYCsKntXBQBUYK7Ww")
        assert self.page.url == "https://www.youtube.com/channel/UCrk8GobYCsKntXBQBUYK7Ww"
        print("OK")


        