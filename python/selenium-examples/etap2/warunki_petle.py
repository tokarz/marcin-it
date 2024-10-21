
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def wejdz_na_strone(adres_www):
     driver.get(adres_www)
     time.sleep(3)


driver = webdriver.Chrome()

# instruckje warunkowe

wejdz_na_strone("https://czarnijaslo.pl/")

elementy_menu =  driver.find_elements(By.CSS_SELECTOR, ".menu-item")  # 2 elementy

# dlugosc_tablicy = len(elementy_menu)  # 2

# if dlugosc_tablicy == 2:
#     element_do_zaznaczenia = elementy_menu[1]  # Error
#     element_do_zaznaczenia.click()
# else:
#     print("Blad! nie znaleziono 2 elementow")


opcje_menu = ["Menu1", "Menu2"]

def kliknijNa(menu):
    elementy_menu =  driver.find_elements(By.CSS_SELECTOR, menu)  # 2 elementy
    elementy_menu[1].click()


for opcja_menu in opcje_menu:
    kliknijNa(opcja_menu)




driver.quit()






# petle