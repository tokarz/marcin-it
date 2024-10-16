from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    time.sleep(3)

    # 2. Find all menu items matching the CSS selector
    wszystkie_opcje = driver.find_elements(By.CSS_SELECTOR, '.menu-item-10460')
    druzyny = wszystkie_opcje[1]
    druzyny.click()
    time.sleep(5)
    
    
    wszystkie_opcje = driver.find_elements(By.CSS_SELECTOR, '.menu-item-10362')
    juniorzymlodsi = wszystkie_opcje[1]
    juniorzymlodsi.click()
    time.sleep(5)



    current_url = driver.current_url
    expected_url = "https://czarnijaslo.pl/juniorzy-mlodsi/"  # Replace with your expected URL
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

   
finally:
    # 6. Close the driver after everything is done
    driver.quit()
