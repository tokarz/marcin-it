import re
from playwright.sync_api import sync_playwright

class Logowanie:
    def __init__(self): 
        self.id = "logowanie_meczyki"
    
    def otworz_strone(self , driver):
        browser = driver.chromium.launch(headless=False)  
        page = browser.new_page()
        page.goto("https://www.meczyki.pl")
        return page 
    
    def login(self , my_page):
        my_page.locator("iframe[title=\"Iframe title\"]").content_frame.locator("div").filter(has_text=re.compile(r"^Zaakceptuj i zamknijUstawienia$")).get_by_label("Zaakceptuj i zamknij").click()
        my_page.get_by_role("link", name="Zaloguj się").click()
        my_page.get_by_placeholder("Login lub adres e-mail").click()
        my_page.get_by_placeholder("Login lub adres e-mail").fill("czarny-python")
        my_page.get_by_placeholder("Hasło").click()
        my_page.get_by_placeholder("Hasło").fill("Tester#!Tester#!")
        my_page.locator("a").filter(has_text="Zaloguj się").click()
        

    def switch_mode(self , page):
        page.locator(".switch-wrapper > .switch").click()


    def click_news(self, page ):
        page.get_by_role("link", name="Newsy").click()


