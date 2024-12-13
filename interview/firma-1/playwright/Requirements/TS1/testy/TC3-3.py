from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_druzyny = driver.find_elements(By.CSS_SELECTOR, ".menu-item-10460")
druzyny = wszystkie_druzyny[1]
druzyny.click()

wszystkie_opcje_klub = driver.find_elements(By.CSS_SELECTOR, ".menu-item-545")
o_klubie = wszystkie_opcje_klub[1]
o_klubie.click()



WebDriverWait(driver, 10).until(EC.url_to_be("https://czarnijaslo.pl/kadra-seniorow/"))

   
current_url = driver.current_url
expected_url = "https://czarnijaslo.pl/kadra-seniorow/"  
if current_url == expected_url:
    print("URL verification passed!")
else:
    print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")



driver.quit()

