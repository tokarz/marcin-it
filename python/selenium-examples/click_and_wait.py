from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # GIVEN
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    # driver.zrob() <--- funkcja - coś robi  , click(), scroll(), return()
    # driver.strona <--- zmienna - zawiera wartosc

    time.sleep(3) # sekundy

    # WHEN
    menu_items = driver.find_elements(By.CSS_SELECTOR, '.menu-item-10460') # tu sa 2 elementy, musze wziac [1]!!!
    target_menu_item = menu_items[1]
    target_menu_item.click()

    # 3. Wait for 2 seconds
    
    time.sleep(5)

    # 6. Take a screenshot
    driver.save_screenshot("strona_glowna.png")  # The screenshot will be saved in the same directory as the script

    # Sprawdz, czy strona sie zaladowala
    # BDD
    # G W T

finally:
    # Close the driver after everything is done
    driver.quit()
