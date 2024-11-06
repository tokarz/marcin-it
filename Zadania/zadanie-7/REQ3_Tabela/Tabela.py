from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Tabela :
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.id = "tabela"
    
    def otworz_strone(self):
        self.driver.get("https://czarnijaslo.pl/") 
    
    def pierwsze_miejsce_kolor(self):
        selektor_pierwszego_miejsca = self.driver.find_element(By.CSS_SELECTOR , ".anwp-bg-success-light")
        color1 = selektor_pierwszego_miejsca.value_of_css_property("color")
        print(" Kolor : " , color1)

    def drugie_miejsce_kolor(self):
        selektor_drugiego_miejsca = self.driver.find_element(By.CSS_SELECTOR , ".anwp-bg-primary-light")
        color2 = selektor_drugiego_miejsca.value_of_css_property("color")
        print(" Kolor : " , color2)

    def ostatnie_miejsce_kolor(self):
        wszystkie_selektory_ostatniego = self.driver.find_elements(By.CSS_SELECTOR , ".anwp-bg-danger-light")
        selektor_ostatniego = wszystkie_selektory_ostatniego[4]
        color3 = selektor_ostatniego.value_of_css_property("color")
        print(" Kolor : " , color3)

    def kliknij_w_zespol(self , zespol):
        if zespol == "czarni jaslo":
            selektor = self.driver.find_element(By.CSS_SELECTOR , 'a[href*="https://czarnijaslo.pl/club/czarni-jaslo/"]')
            selektor.click()
        if zespol == "sokol nisko":
            selektor = self.driver.find_element(By.CSS_SELECTOR , 'a[href*="https://czarnijaslo.pl/club/sokol-nisko/"]')
            selektor.click()

        if zespol == "strug tyczyn":
            selektor = self.driver.find_element(By.CSS_SELECTOR , 'a[href*="https://czarnijaslo.pl/club/strug-tyczyn/"]')
            selektor.click()

    def czy_na_stronie(self , url):
        return self.driver.current_url == url


    


