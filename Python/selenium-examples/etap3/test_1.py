from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wejdz_na_strone(link_do_strony):
    driver.get(link_do_strony)  # Replace with the actual URL
    poczekaj(1)

def kliknij_na_selektor(selektor):
    foundElement = driver.find_element(By.CSS_SELECTOR, selektor) 
    foundElement.click()

def poczekaj(tyle_masz_czekac):
    time.sleep(tyle_masz_czekac)

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

def wpiszTekst(selektor, tekst):
    pole = driver.find_element(By.CSS_SELECTOR, selektor)
    pole.send_keys(tekst)
    time.sleep(1)

def kliknij_zaloguj():
    button = driver.find_elements(By.CSS_SELECTOR, '.login-button')
    pierwszy_znaleziony_element = button[0]
    pierwszy_znaleziony_element.click()
    

def kliknij_zaakceptuj():
    iframe = driver.find_elements(By.CSS_SELECTOR, "iframe")
    ourIframe = iframe[1]
    driver.switch_to.frame(ourIframe)
    button = driver.find_element(By.CSS_SELECTOR, '[title*="Zaakceptuj i zamknij"]')
    button.click()
    driver.switch_to.default_content()
    
def zaloguj_na_meczykach():
    wejdz_na_strone("https://www.meczyki.pl/")
    poczekaj(5)
    kliknij_zaakceptuj()
    poczekaj(2)
    kliknij_na_selektor('[href*="logowanie"]')
    poczekaj(2)
    wpiszTekst('[placeholder*="Login lub adres e-mail"]', "czarny-python")
    poczekaj(2)
    wpiszTekst('[placeholder*="Hasł"]', "Tester#!Tester#!")
    kliknij_zaloguj()
    poczekaj(10)


def kliknij_na_selektor_wyloguj(selektor):
    wszystkie_opcje = driver.find_elements(By.CSS_SELECTOR, selektor)
    przycisk_wyloguj = wszystkie_opcje[2]
    przycisk_wyloguj.click()
    poczekaj(3)


def wyloguj():
    kliknij_na_selektor('.user-buttons')
    kliknij_na_selektor_wyloguj('.router-link-exact-active')
    poczekaj(3)

def go_to_champions_league_and_click_leader():
    champions_league_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Liga Mistrzów')]"))
    )
    champions_league_link.click()
    poczekaj(5)
    leader = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table//tr[1]//a"))  
    )
    leader.click()
        
    driver.quit()
   




zaloguj_na_meczykach()
wyloguj()
go_to_champions_league_and_click_leader()
