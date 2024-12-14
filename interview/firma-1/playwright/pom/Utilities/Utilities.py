from playwright.sync_api import sync_playwright

class Utilities:
    def __init__(self):
        self.id = "utilis"
      
    def czarnijaslo(self, driver):
        browser = driver.chromium.launch(headless=False)
        page = browser.new_page()
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




 ###SPONSORZY###       

    def click_sponsorzy(self, driver):
        page = self.czarnijaslo(driver)
        sposnoring = page.locator(".td_spot_img_all")
        sposnoring.click()
        page.wait_for_url("https://czarnijaslo.pl/")
        assert page.url == ("https://czarnijaslo.pl/")
        page.close()
        print("OK")



###STOPKA###

    def click_stopka_mojejaslo(self , driver):
        page = self.czarnijaslo(driver)
        stopka_moje_jaslo = page.locator("aside").filter(has_text="Zaprzyjaźnione media").get_by_role("link")
        stopka_moje_jaslo.click()
        page.wait_for_url("https://mojejaslo.pl/")
        assert page.url == ("https://mojejaslo.pl/")
        page.close()
        print("OK")





###TABELA###

    def click_tabela(self , driver , Klub , url):
        page = self.czarnijaslo(driver)
        selektor = page.locator("#anwpfl-widget-standing-4 div").filter(has_text= Klub ).nth(2)
        selektor.click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")

####SPRAWDZ DATE####   
    def sprawdz_date(self, driver , ):
        page = self.czarnijaslo(driver)
        element = page.locator(".tdb-head-date-txt")   #### NIE WIEM JAK ZCZYTAC POPRAWNIE DATE , Na podstawie jakiego selektora... 
        page.text_content = element.text_content()    ######BO po zczytaniu wyswietla cala sciezke selektora ...
        print(element)

#### ODNOSNIKI SOCIAL MEDIA###

    def sprawdz_odnosnik(self , page , nr_social , url):
        selektor = page.locator(".tdm-social-item")
        selektor.nth(nr_social).click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")


#### SPRAWDZENIE ODNOSNIKA SPONSORA GLOWNEGO ####

    def sprawdz_sponsora_strategicznego(self , driver):
        page = self.czarnijaslo(driver)
        selektor = page.locator(".tdm-inline-image-wrap" )
        selektor.click()
        page.wait_for_url("https://alfaram.pl/")
        assert page.url == "https://alfaram.pl/"
        page.close()
        print("OK")

#### SPRAWDZENIE POPRZEDNICH AKTUALNOSCI /GALERI na stronie glownej #####

    def przejdz_do_artykulu(self , driver , ktory_art , url):
        page = self.czarnijaslo(driver)
        selektor = page.locator(".td-thumb-css ")
        selektor.nth(ktory_art).click()
        page.wait_for_url(url)
        assert page.url == url
        page.close()
        print("OK")
        


        


  



  
