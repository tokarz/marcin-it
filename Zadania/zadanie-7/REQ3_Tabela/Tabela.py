from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# druzyna - adres www

# czarni jaslo ->


# typ zlozony
mojezespoly = ["czarni", "zieloni"]

# typy  zlozone  {}, []
druzynaDoAdresuWWW = {
    "czarni jaslo": "https://czarnijaslo.pl/club/czarni-jaslo/",
    "sokol nisko":  "https://czarnijaslo.pl/club/sokol-nisko/",
    "strug tyczyn": "https://czarnijaslo.pl/club/strug-tyczyn/"
}
    
# typy proste     
liczba = 7
napis = "Lala"

class Tabela :
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.id = "tabela"
    
    def otworz_strone(self):
        self.driver.get("https://czarnijaslo.pl/") 
    
    def pierwsze_miejsce_kolor(self) -> bool:
        selektor_pierwszego_miejsca = self.driver.find_element(By.CSS_SELECTOR , ".anwp-bg-success-light")
        color1 = selektor_pierwszego_miejsca.value_of_css_property("color")
        print(" Kolor : " , color1)
        return (color1 == "#65aa78") # true/false

    def drugie_miejsce_kolor(self):
        selektor_drugiego_miejsca = self.driver.find_element(By.CSS_SELECTOR , ".anwp-bg-primary-light")
        color2 = selektor_drugiego_miejsca.value_of_css_property("color")
        print(" Kolor : " , color2)

    def ostatnie_miejsce_kolor(self) -> bool:
        wszystkie_selektory_ostatniego = self.driver.find_elements(By.CSS_SELECTOR , ".anwp-bg-danger-light")
        selektor_ostatniego = wszystkie_selektory_ostatniego[4]
        color3 = selektor_ostatniego.value_of_css_property("color")
        print(" Kolor : " , color3)
        return (color3 == "#65aa78") # true/false

    def kliknij_w_zespol(self , zespol):
        selektor = self.driver.find_element(By.CSS_SELECTOR , druzynaDoAdresuWWW[zespol])
        selektor.click()

    def czy_na_stronie(self , url):
        return self.driver.current_url == url


    


