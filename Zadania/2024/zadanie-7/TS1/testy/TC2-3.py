from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_sociale = driver.find_elements(By.CSS_SELECTOR, '.tdm-social-item')
social = wszystkie_sociale[2]
social.click()

WebDriverWait(driver, 10).until(EC.url_to_be("https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910"))

   
current_url = driver.current_url
expected_url = "https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910"  
if current_url == expected_url:
    print("URL verification passed!")
else:
    print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")



driver.quit()
