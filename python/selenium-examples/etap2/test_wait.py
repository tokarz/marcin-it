from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time



class Ciasto:
    # self <--- worek na zmienne w klasie
    def __init__(self, maka, jajka, woda, jablka):
        self.maka = maka
        self.jajka=jajka
        self.woda=woda
        self.jablka = jablka


# Pieczątka
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie  # Atrybuty obiektu
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def przedstaw_sie(self):
        opis = "Witaj " + self.imie + " " + self.nazwisko + " , masz " + self.wiek + " lat!"
        print(opis)


# konkretna osoba
Marcin = Osoba("Marcin", "Iskrzycki", "25")

Jablecznik = Ciasto("Babuni", "2", "5l", "Jonagold")





driver = webdriver.Chrome()
        

wait = WebDriverWait(driver, 10)


elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'common-class')))


# Page-Object-Model


class CzarniJasloPl:
    menu=["menu-item-327", "menu-item-10440"]
    


def click():
    driver.find_elements(By.CSS_SELECTOR, CzarniJasloPl.menu[0])



        











osoba = Osoba("Marcin", "Iskrzycki", "25")
osoba = Osoba("Maciej", "Tokarz", "39")











def dupa():
    print("dupa")













def opiszOsobe():
    osoba = Osoba("Marcin", "Iskrzycki", "25")
    
    osoba.przedstaw_sie()
    
    time.sleep(5)

















# try:
    # driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL
    # wait = WebDriverWait(driver, 10)

    # druzyny = driver.find_elements(By.CSS_SELECTOR, '.menu-item-10460')[1]
    # time.sleep(2)

    # druzyny = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.menu-item-10460')))
    # druzyny[1].click()

    # time.sleep(4)

opiszOsobe()


