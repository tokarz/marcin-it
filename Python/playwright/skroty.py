from logowanie_meczyki import Logowanie
import re
from playwright.sync_api import sync_playwright



class Skroty:

    def __init__(self) -> None:
        self.logowanie = Logowanie()
        

    def click_england(self , driver ):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="Anglia Anglia").click()
   

    def click_lider_ekstraklasa(self , driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.locator(".competition-wrapper").first.click()
        page.get_by_role("link", name="Lech Poznań").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/lech-poznan/1653")
        assert page.url == "https://www.meczyki.pl/druzyna/lech-poznan/1653"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/lech-poznan/1653")
        

    def clicl_lider_premierLeague(self, driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="Premier League", exact=True).click()
        page.get_by_role("row", name="Liverpool FC 11 9 28").get_by_role("link").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/liverpool-fc/663")
        assert page.url == "https://www.meczyki.pl/druzyna/liverpool-fc/663"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/liverpool-fc/663")
    
    def click_lider_laLiga(self , driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="La Liga", exact=True).click()
        page.get_by_role("row", name="FC Barcelona 13 11 33").get_by_role("link").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/fc-barcelona/2017")
        assert page.url == "https://www.meczyki.pl/druzyna/fc-barcelona/2017"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/fc-barcelona/2017")

    def click_lider_bundesliga(self , driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="Bundesliga", exact=True).click()
        page.get_by_role("row", name="Bayern Monachium 10 8 26").get_by_role("link").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/bayern-monachium/961")
        assert page.url == "https://www.meczyki.pl/druzyna/bayern-monachium/961"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/bayern-monachium/961")

    def click_lider_serieA(self , driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="Serie A", exact=True).click()
        page.get_by_role("row", name="Napoli 12 8 26").get_by_role("link").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/napoli/1270")
        assert page.url == "https://www.meczyki.pl/druzyna/napoli/1270"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/napoli/1270")

    def click_lider_ligue1(self , driver):
        page = self.logowanie.test_open_page_and_click(driver)
        self.logowanie.login(page)
        page.get_by_role("link", name="Skróty").click()
        page.get_by_role("link", name="Ligue 1", exact=True).click()
        page.get_by_role("row", name="PSG 11 9 29").get_by_role("link").click()
        page.wait_for_url("https://www.meczyki.pl/druzyna/psg/886")
        assert page.url == "https://www.meczyki.pl/druzyna/psg/886"
        page.close()
        print("Asercja przebiegła pomyślnie: URL jest zgodny z oczekiwanym: https://www.meczyki.pl/druzyna/psg/886")






with sync_playwright() as driver:

    skroty = Skroty()
    #skroty.click_england(driver)
    skroty.click_lider_ekstraklasa(driver)
    skroty.clicl_lider_premierLeague(driver)
    skroty.click_lider_ligue1(driver)
    skroty.click_lider_bundesliga(driver)
    skroty.click_lider_ligue1(driver)
    skroty.click_lider_serieA(driver)