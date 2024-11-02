from selenium import webdriver
from selenium.webdriver.common.by import By












class CzarniJasloPl:

# Set up the driver (use Chrome in this case)
    driver = webdriver.Chrome()
    
    def __init__(self , menu_gorne , sponsorzy , media_spolecznosciowe , tabela ):
        self.menu_gorne = menu_gorne
        self.sponsorzy = sponsorzy
        self.media_spolecznosciowe = media_spolecznosciowe
        self.tabela = tabela
        
    def kliknij_na_druzyny():
        print("boo")
        
    def kliknij_na_media():
        print("boo")
    
    def rozwin_rozgrywki(self):
        self.driver.get("www.czarnijaslo.pl")

        
        
        
        














menuGorne = "MenuGorne"
sponsorzy="sponsorzy"
media = "media"
tabela="table"







# BLACK BOX 
czarniJasloStronka = CzarniJasloPl(menuGorne, sponsorzy, media, tabela)

czarniJasloStronka.kliknij_na_media()

czarniJasloStronka.kliknij_na_druzyny()


# TC -> rozwin menu rozgrywki, kliknij na IV liga i zaznacz lidera, sprawdz czy Jaroslaw
def test_lidera():
    obiektNowyDlaTestu = CzarniJasloPl("", "", "", "")
    obiektNowyDlaTestu.rozwin_rozgrywki()
    obiektNowyDlaTestu.kliknij_na_4_liga()
    obiektNowyDlaTestu.zaznacz_lidera()
    obiektNowyDlaTestu.czyLiderTo("Jaroslaw")
    
    





