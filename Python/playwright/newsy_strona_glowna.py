import re
from playwright.sync_api import sync_playwright
from logowanie_meczyki import Logowanie


class SprawdzNaglowekNewsa:
    def __init__(self):
        self.logowanie = Logowanie()

    def sprawdz_naglowek_newsa(self, driver):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        
        
        naglowek_strona_glowna = page.locator(".hero .hero-title").inner_text() 
        print("Nagłówek na stronie głównej:", naglowek_strona_glowna)
        page.locator(".hero .hero-title").click()
        
        
        page.wait_for_selector(".news-top-section .news-title")
        naglowek_po_wejsciu = page.locator(".news-top-section .news-title").inner_text()
        print("Nagłówek po wejsciu na strone:", naglowek_po_wejsciu) 
        
        if naglowek_strona_glowna == naglowek_po_wejsciu:
            print("Nagłówki są takie same!")
        else:
            print("Nagłówki się różnią!")




