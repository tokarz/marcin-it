from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def wejdz_na_strone(adres_www):
     driver.get(adres_www)
     poczekaj(3)

def kliknij_na(selektor):
     foundElement = driver.find_element(By.CSS_SELECTOR, selektor) 
     foundElement.click()
     poczekaj(3)

def wpisz_tekst_do_pola(selektor , jaki_tekst):
     pole = driver.find_element(By.CSS_SELECTOR, selektor)
     pole.send_keys(jaki_tekst)
     poczekaj(3)

def wyswietl_napis(tekst):
     print(tekst)
     poczekaj(3)

def wyszukaj(tekst):
     wpisz_tekst_do_pola(selektor , tekst )
     kliknij_na(selektor)
     poczekaj(3)

def wyszukaj_1(tekst):
     wpisz_tekst_do_pola('.tdb-head-search-form-input' , tekst )
     kliknij_na('.tdc-font-tdmp-arrow-cut-right')
     poczekaj(3)




#'.tdb-head-search-form-input'
#.tdc-font-tdmp-arrow-cut-right

def poczekaj(czas):
    time.sleep(czas)


def cosmos(tekst):
    wejdz_na_strone("https://czarnijaslo.pl/")
    kliknij_na('.tdb-search-icon')
    wyszukaj_1(tekst)
    driver.quit()

#####Funkcja wyszukiwania cosmosu####
cosmos("Cosmos")
#####Funkcja wyszukiwania cosmosu####

















