from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_rozgrywki = driver.find_elements(By.CSS_SELECTOR, ".menu-item-10461")
rozgrywki = wszystkie_rozgrywki[1]
rozgrywki.click()

wszystkie_opcje_IV_liga = driver.find_elements(By.CSS_SELECTOR, ".menu-item-10357")
IV_liga = wszystkie_opcje_IV_liga[1]
IV_liga.click()



WebDriverWait(driver, 10).until(EC.url_to_be("https://czarnijaslo.pl/competition/4-liga-podkarpacka/"))

   
current_url = driver.current_url
expected_url = "https://czarnijaslo.pl/competition/4-liga-podkarpacka/"  
if current_url == expected_url:
    print("URL verification passed!")
else:
    print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")



driver.quit()
