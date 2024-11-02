class Meczyki:
    #  self.
    
    URL = "www.meczyki.pl"
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def zaloguj(self):
        print("Zaloguj do" + self.URL) 
        
    def wyloguj():
        print("wyloguj")
    
    def otworz(self):
        self.driver.get("www.meczyki.pl")  # Replace with the actual URL
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


class MeczykiSkroty(Meczyki):
    def kliknij_na_skrot(self):
        self.zaloguj()
        
        
class Auto:
    kola = 4
    silnik="silnik"
    def go():
        print("Going!")
        
class Ciezarowka(Auto):
    naczepa="5t"
    def cbradio():
        print("CB")
        

star = Ciezarowka()
star.go()
        
        
        
        
def wejdzNaMeczyki(meczyki :Meczyki):
    meczyki.zaloguj()
    
def wejdzNaMeczyki2(meczyki):
    print(meczyki)



wejdzNaMeczyki("www.meczyki.pl")



