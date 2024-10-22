from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


def wejdz_na_strone(link_do_strony):
    driver.get(link_do_strony)  
    poczekaj(3)

def poczekaj(tyle_masz_czekac):
    time.sleep(tyle_masz_czekac)

def zmien_tryb():
    wszystkie_znalezione_elementy = driver.find_element(By.CSS_SELECTOR,'.moon')
    pierwszy_znaleziony_element = wszystkie_znalezione_elementy[0]
    pierwszy_znaleziony_element.click()
    poczekaj(3)


def kliknij_zaakceptuj():
    iframe = driver.find_elements(By.CSS_SELECTOR, "iframe")
    ourIframe = iframe[1]
    driver.switch_to.frame(ourIframe)
    button = driver.find_element(By.CSS_SELECTOR, '[title*="Zaakceptuj i zamknij"]')
    button.click()
    driver.switch_to.default_content()
    poczekaj(3)


def zmiana_trybu():
    wejdz_na_strone("https://www.meczyki.pl/")
    kliknij_zaakceptuj()
    zmien_tryb()

zmiana_trybu()