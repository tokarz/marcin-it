from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


    
driver.get("https://czarnijaslo.pl/") 

    
wszystkie_aktualnosci = driver.find_elements(By.CSS_SELECTOR, ".td-thumb-css")
aktualnosci1 = wszystkie_aktualnosci[1]
aktualnosci1.click()



time.sleep(3)

driver.quit()