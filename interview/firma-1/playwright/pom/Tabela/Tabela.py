# from playwright.sync_api import sync_playwright
# import pytest

# @pytest.fixture(scope="function")
# def przegladarka():  
#     with sync_playwright() as playwright:    
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield page 
#         browser.close()
    
# def test_tabela_kolbuszowa(przegladarka):   
#     przegladarka.goto("https://czarnijaslo.pl/")
#     sokol_kolbuszowa = przegladarka.get_by_role("link", name="Sokół Kolbuszowa D.")
#     sokol_kolbuszowa.click()
#     przegladarka.wait_for_url("https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/")
#     assert przegladarka.url == "https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/"
#     print("OK")
from playwright.sync_api import Page


class Tabela:

    def __init__(self , page : Page):
        self.page = page

    def test_tabela_kolbuszowa(self):   
        self.page.goto("https://czarnijaslo.pl/")
        sokol_kolbuszowa = self.page.get_by_role("link", name="Sokół Kolbuszowa D.")
        sokol_kolbuszowa.click()
        self.page.wait_for_url("https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/")
        assert self.page.url == "https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/"
        print("OK")