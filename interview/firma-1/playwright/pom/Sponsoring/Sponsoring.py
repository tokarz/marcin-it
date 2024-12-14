# from playwright.sync_api import sync_playwright
# import pytest

# @pytest.fixture(scope="function")
# def przegladarka():  
#     with sync_playwright() as playwright:    
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield page 
#         browser.close()
    
# def test_click_sposnorzy(przegladarka):  
#     przegladarka.goto("https://czarnijaslo.pl/")
#     sposnoring = przegladarka.locator(".td_spot_img_all")
#     sposnoring.click()
#     przegladarka.wait_for_url("https://czarnijaslo.pl/")
#     assert przegladarka.url == "https://czarnijaslo.pl/"
#     print ("OK")


from playwright.sync_api import Page
class Sponsoring:
    def __init__(self , page : Page):
        self.page = page
        
    def test_click_sposnorzy(self):   
        self.page.goto("https://czarnijaslo.pl/")
        sposnoring = self.page.locator(".td_spot_img_all")
        sposnoring.click()
        self.page.wait_for_url("https://czarnijaslo.pl/")
        assert self.page.url == "https://czarnijaslo.pl/"
        print ("OK")
        