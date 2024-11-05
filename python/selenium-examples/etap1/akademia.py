from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
  
    driver.get("https://czarnijaslo.pl/")


    wszystkie_elementy_akademia = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.menu-item-18804'))
    )
    
    drugi_element = wszystkie_elementy_akademia[1]
    drugi_element.click()
   
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    
   
    current_url = driver.current_url
    expected_url = "https://www.facebook.com/APCzarniJaslo"  
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

finally:
    
    driver.quit()