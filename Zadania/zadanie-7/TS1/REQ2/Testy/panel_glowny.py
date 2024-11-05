from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class PanelGlowny:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.id = "panel glowny"

    def click_aktualnosci(self): 
        wszystkie_aktualnosci = self.driver.find_elements(By.CSS_SELECTOR, ".td-thumb-css")
        aktualnosci1 = wszystkie_aktualnosci[1]
        aktualnosci1.click()
        time.sleep(3)


    def click_klub(self): 
        pass
    def click_druzyny(self): 
        pass
    def click_rozgrywki(self): 
        pass
    def click_kibice(self): 
        pass
    def click_klub100(self): 
        wszystkie_klub100 = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-626")
        klub100 = wszystkie_klub100[1]
        klub100.click()
        time.sleep(1)


    def click_sponsoring(self): 
        pass
    def click_akademia(self): 
        pass
    def czy_na_stronie(self , url):
        return self.driver.current_url == url
    def otworz_strone(self):
        self.driver.get("https://czarnijaslo.pl/") 

    def kliknij_na(self, podstrona):
        if podstrona == "historia":
             wszystkie_historia = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-844")
             historia = wszystkie_historia[1]
             historia.click()
        if podstrona == "sztab":
             wszystkie_sztab = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-20646")
             sztab = wszystkie_sztab[1]
             sztab.click()




            