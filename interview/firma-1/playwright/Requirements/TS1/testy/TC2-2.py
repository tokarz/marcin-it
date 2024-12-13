from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_sociale = driver.find_elements(By.CSS_SELECTOR, '.tdm-social-item')
social = wszystkie_sociale[1]
social.click()

WebDriverWait(driver, 10).until(EC.url_to_be("https://www.instagram.com/czarni_1910_jaslo/"))

   
current_url = driver.current_url
expected_url = "https://www.instagram.com/czarni_1910_jaslo/"  
if current_url == expected_url:
    print("URL verification passed!")
else:
    print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")



driver.quit()

