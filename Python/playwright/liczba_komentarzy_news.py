import re
from playwright.sync_api import sync_playwright
from logowanie_meczyki import Logowanie


class LiczbaKomentarzyNews:
    def __init__(self):
        self.logowanie = Logowanie()

    def sprawdz_liczbe_komentarzy_newsa(self, driver):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        
        
        strona_glowna_news_liczba_komentarzy = page.locator(".news-hero .counter").inner_text() 
        print("Liczba komentarzy strona glowna:", strona_glowna_news_liczba_komentarzy)
        page.locator(".news-hero .counter").click()
        
        
        page.wait_for_selector(".sub-title.wrap ")
        liczba_komentarzy_po_wejsciu = page.locator(".sub-title.wrap ").inner_text()
        print("Liczba komentarzy po wejsciu w news:", liczba_komentarzy_po_wejsciu) 
        
        if strona_glowna_news_liczba_komentarzy == liczba_komentarzy_po_wejsciu:
            print("Liczba komentarzy jest taka sama!")
        else:
            print("Liczba komentarzy rozni sie!")



