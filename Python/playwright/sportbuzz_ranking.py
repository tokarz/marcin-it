from logowanie_meczyki import Logowanie
import re
from playwright.sync_api import sync_playwright

class Sportbuzz:
    def __init__(self):
         self.logowanie = Logowanie()

    def sprawdzenie_rankingu(self , driver , username):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Sportbuzz").first.click()
        nazwa_uzytkownika = page.locator(".sportbuzz-ranking-user-image-wrapper .picture-wrapper").first
        nazwa_uzytkownika.first.click()
        sprawdzenie_nazwy_uzytkownika = page.locator(".username")
        sprawdzenie_nazwy_uzytkownika.inner_text() 
        print("Nazwa Uzytkownika : ", sprawdzenie_nazwy_uzytkownika )
        if sprawdzenie_nazwy_uzytkownika == username :
            print("Nazwa uzytkownika jest poprawna!")
        else:
            print("Nazwa uzytkownika jest niepoprawna!")
        page.close()

    def sprawdzenie_rankingu_miejsce(self , driver , miejsce , username):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Sportbuzz").first.click()
        nazwa_uzytkownika = page.locator(".sportbuzz-ranking-user-image-wrapper .picture-wrapper").nth(miejsce)
        nazwa_uzytkownika.first.click()
        sprawdzenie_nazwy_uzytkownika = page.locator(".username")
        sprawdzenie_nazwy_uzytkownika.inner_text() 
        print("Nazwa Uzytkownika : ", sprawdzenie_nazwy_uzytkownika )
        if sprawdzenie_nazwy_uzytkownika == username :
            print("Nazwa uzytkownika jest poprawna!")
        else:
            print("Nazwa uzytkownika jest niepoprawna!")
        page.close()

