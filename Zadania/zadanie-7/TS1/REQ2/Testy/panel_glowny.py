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
        wszystkie_klub = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-656")
        klub = wszystkie_klub[1]
        klub.click()

    def click_druzyny(self): 
        wszystkie_druzyny = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-10460")
        druzyny = wszystkie_druzyny[1]
        druzyny.click()
    
    def click_rozgrywki(self): 
        wszystkie_rozgrywki = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-10461")
        rozgrywki = wszystkie_rozgrywki[1]
        rozgrywki.click()
    
    def click_kibice(self): 
        wszystkie_kibice = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-975")
        kibice = wszystkie_kibice[1]
        kibice.click()
   
    def click_klub100(self): 
        wszystkie_klub100 = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-626")
        klub100 = wszystkie_klub100[1]
        klub100.click()
        time.sleep(1)


    def click_sponsoring(self): 
        wszystkie_sponsoring = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-267")
        sponsoring = wszystkie_sponsoring[1]
        sponsoring.click()
    
    def click_akademia(self): 
        wszystkie_akademia = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-20775")
        akademia = wszystkie_akademia[1]
        akademia.click()

    
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
        if podstrona == "Bilety":
            wszystkie_opcje_kibice = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-862")
            bilety = wszystkie_opcje_kibice[1]
            bilety.click()
        if podstrona == "IV liga":
            wszystkie_opcje_IV_liga = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-10357")
            IV_liga = wszystkie_opcje_IV_liga[1]
            IV_liga.click()
        if podstrona == "seniorzy":
            wszystkie_opcje_druzyny = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-545")
            seniorzy = wszystkie_opcje_druzyny[1]
            seniorzy.click()
        if podstrona == "o klubie":
            wszystkie_opcje_klub = self.driver.find_elements(By.CSS_SELECTOR, ".menu-item-696")
            o_klubie = wszystkie_opcje_klub[1]
            o_klubie.click()





            