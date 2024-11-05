from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_klub = driver.find_elements(By.CSS_SELECTOR, ".menu-item-656")
klub = wszystkie_klub[1]
klub.click()

time.sleep(3)




driver.quit()

