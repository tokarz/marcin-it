from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()


def wejdz_na_strone(link_do_strony):
    driver.get(link_do_strony)  
    poczekaj(3)

def poczekaj(tyle_masz_czekac):
    time.sleep(tyle_masz_czekac)


def kliknij_zaakceptuj():
    iframe = driver.find_elements(By.CSS_SELECTOR, "iframe")
    ourIframe = iframe[1]
    driver.switch_to.frame(ourIframe)
    button = driver.find_element(By.CSS_SELECTOR, '[title*="Zaakceptuj i zamknij"]')
    button.click()
    driver.switch_to.default_content()
    poczekaj(5)

def go_to_ekstraklasa_and_click_leader():
    ekstraklasa_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Ekstraklasa')]"))
        )
        
    ekstraklasa_link.click()
    poczekaj(5)
    leader = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table//tr[1]//a"))  
    )
    leader.click()
    poczekaj(5)




wejdz_na_strone("https://www.meczyki.pl/")
kliknij_zaakceptuj()
go_to_ekstraklasa_and_click_leader()