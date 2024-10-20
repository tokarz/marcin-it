from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

def poczekaj(czas):
    time.sleep(czas)

def wejdz_na_strone(adres_www):
     driver.get(adres_www)
     poczekaj(3)

def znajdz_element(selektor):
    menu_items = driver.find_elements(By.CSS_SELECTOR, selektor) 
    target_menu_item = menu_items[1]
    target_menu_item.click()
    poczekaj(3)

def pierwsza_druzyna(druzyna):
    lider = driver.find_element('link text', druzyna)
    lider.click()
    poczekaj(5)

def lider(druzyna):
    wejdz_na_strone('https://czarnijaslo.pl')
    znajdz_element('.menu-item-10461')
    znajdz_element('.menu-item-10357')
    pierwsza_druzyna(druzyna)
    driver.quit()
     










     


######################
lider("JKS Jarosław")