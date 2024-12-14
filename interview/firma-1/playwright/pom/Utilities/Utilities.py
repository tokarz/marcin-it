from playwright.sync_api import sync_playwright
import time
class Utilities:
    def __init__(self, page):
        self.id = "utilis"
        self.page = page
      
    def czarnijaslo(self, page):
        page.goto("https://czarnijaslo.pl/")
        return page
          

    ###PANEL GLOWNY###
    ####CLICK AKTUALCOSCI /KLUB100/SPONSORING/AKADEMIA####
    def click_panel_glowny_zwykly(self, page , nazwa , url ):
        selektor = page.locator("#menu-menu-3").get_by_role("link", name = nazwa)
        selektor.click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")

    #####CLICK KLUB/DRUZYNY/ROZGRYWKI/KIBICE#### ROZWIJANE !! ######

    def click_panel_glowny_rozwijany(self , driver , nazwa1 , nazwa2 , url ):
        page = self.czarnijaslo(driver)
        selektor1 = page.get_by_role("link", name = nazwa1)
        selektor1.click()
        selektor2 = page.locator("#menu-menu-3").get_by_role("link", name=nazwa2)
        selektor2.click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")

####SPRAWDZ DATE####   
    def sprawdz_date(self, page):
        page = self.czarnijaslo(page)
        element = page.locator(".tdb-head-date-txt")   #### NIE WIEM JAK ZCZYTAC POPRAWNIE DATE , Na podstawie jakiego selektora... 
        page.text_content = element.text_content()    ######BO po zczytaniu wyswietla cala sciezke selektora ...
        print(element)

#### ODNOSNIKI SOCIAL MEDIA###

    def sprawdz_odnosnik(self , nr_social , url):
        self.czarnijaslo(self.page)
        selektor = self.page.locator(".tdm-social-item")
        selektor.nth(nr_social).click()
        self.page.wait_for_url(url)
        # page.close()
        return self.page.url
        




#### SPRAWDZENIE POPRZEDNICH AKTUALNOSCI /GALERI na stronie glownej #####

    def przejdz_do_artykulu(self , driver , ktory_art , url):
        page = self.czarnijaslo(driver)
        selektor = page.locator(".td-thumb-css ")
        selektor.nth(ktory_art).click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")
        


        


  



  
