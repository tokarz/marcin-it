from selenium import webdriver
from selenium.webdriver.common.by import By
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


 
    # ######################################### TUTAJ PISZ TESTY ###########################################################
def kliknij_na_selektor_wyloguj(selektor):
        wszystkie_opcje = driver.find_elements(By.CSS_SELECTOR, selektor)
        przycisk_wyloguj = wszystkie_opcje[2]
        przycisk_wyloguj.click()
        time.sleep(5)



def wyloguj():
    kliknij_na_selektor('.user-buttons')
    kliknij_na_selektor_wyloguj('.router-link-exact-active')


zaloguj_na_meczykach()
wyloguj()



















    # Close the driver after everything is done
driver.quit()





def doSomething(self):
    self.x = 'abc'
    
    return 'foo'
    



myValue = doSomething()