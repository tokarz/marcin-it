from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_akademia = driver.find_elements(By.CSS_SELECTOR, ".menu-item-20775")
akademia = wszystkie_akademia[1]
akademia.click()



WebDriverWait(driver, 10).until(EC.url_to_be("https://www.facebook.com/APCzarniJaslo"))

   
current_url = driver.current_url
expected_url = "https://www.facebook.com/APCzarniJaslo"  
if current_url == expected_url:
    print("URL verification passed!")
else:
    print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")



driver.quit()