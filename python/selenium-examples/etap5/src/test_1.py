# # tutaj importuje do mojego pliku wszystko czego potrzebuje
# from ..libs.driver_provider import CoolDriver
# import time


# class TestMainPage():
#     coolDriver = CoolDriver("My custom driver")
    
#     def __init__(self):
#         self.name="MainPage"
        
#     def openMainPage(self):
#         time.sleep(2)
#         self.coolDriver.open_web_page("www.czarnijaslo.pl")
        
        








def pokaz_poslady():
    print("ABC")


#Kontekst pliku/ globalny

imie = "Wazne imie spoza klasy"

dzisiejsza_data = "29.10.2024"

abc = "ABC"

class OsobaZPosladami():
    imie=""
    abc = "ABC"
    # Ma
    def __init__(self, podaneImie):
        self.imie = podaneImie
    
    
    def zmienInie(self, nowe_imie):
        self.imie = nowe_imie
    
    # kontekst klasy!
    # Potrafi
    def pokaz_poslady(self):
        print("dupa2 " +self.imie)
        
        
    def mojaFunkcja(self):
        pokaz_poslady()
        self.abc
        
        
maciek = OsobaZPosladami("Maciek")

maciek.pokaz_poslady()

maciek.zmienInie("Janek")

maciek.pokaz_poslady()




















        

