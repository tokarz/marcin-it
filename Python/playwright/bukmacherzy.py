import re
from playwright.sync_api import sync_playwright
from logowanie_meczyki import Logowanie


class Bukmacherzy:
    def __init__(self):
        self.logowanie = Logowanie()

    def sprawdz_bukmachera(self, driver):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Bukmacherzy").click()
        page.locator(".bookie-frame-button .label").first.click()
        page.wait_for_timeout(3000)
        expected_url = "https://www.sts.pl/rejestracja?btag=3ietsOrz5FuK-yzxn_Qe02Nd7ZgqdRLk&aff=36&promoCode=MECZYKI&campaign=MECZYKI&utm_campaign=MECZYKI&utm_medium=meczyki&source=aff&utm_content=text&utm_source=aff"
        assert page.url == expected_url, f"URL nie pasuje! Oczekiwano: {expected_url}, znaleziono: {page.url}"
        page.close()

    def sprawdz_bukmachera_2(self, driver):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Bukmacherzy").click()
        page.locator(".bookie-frame-button .label").nth(1).click()
        page.wait_for_timeout(3000)
        expected_url2 = "https://superbet.pl/rejestracja?bonus=MECZYKI"
        assert page.url == expected_url2, f"URL nie pasuje! Oczekiwano: {expected_url2}, znaleziono: {page.url}"
        page.close()

    def sprawdz_bukmachera_3(self, driver ):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Bukmacherzy").click()
        page.locator(".bookie-frame-button .label").nth(2).click()
        page.wait_for_timeout(3000)
        expected_url3 = "https://account.efortuna.pl/register?clienttype=sportsbook&promocode=MECZYKI&%3Futm_source=meczyki&utm_medium=affiliate&utm_campaign=SPB_ACQ_Meczyki_rejestracja"
        assert page.url ==  expected_url3 , f"URL nie pasuje! Oczekiwano: {expected_url3}, znaleziono: {page.url}"
        page.close()
    
    def sprawdz_bukmachera_4(self, driver):
        page = self.logowanie.otworz_strone(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Bukmacherzy").click()
        page.locator(".bookie-frame-button .label").nth(3).click()
        page.wait_for_timeout(3000)
        expected_url4 = "https://www.betclic.pl/rejestracja"
        assert page.url == expected_url4 , f"URL nie pasuje! Oczekiwano: {expected_url4}, znaleziono: {page.url}"
        page.close()

