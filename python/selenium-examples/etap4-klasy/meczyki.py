from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Meczyki:
    #  self.
    
    URL = "www.meczyki.pl"
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def zaloguj(self):
        print("Zaloguj do" + self.URL) 
        
    def wyloguj():
        print("wyloguj")
    
    def otworz(self):
        self.driver.get("www.meczyki.pl")  # Replace with the actual URL
        



















        
meczyki=Meczyki()
meczyki.otworz()







czarniJaslo=CzarniJaslo()
meczyki.otworz()




