from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    time.sleep(3)

    # 2. Click on the menu with class '.menu'
    menu_items = driver.find_elements(By.CSS_SELECTOR, '#menu-menu-3 .menu-item') # Corrected XPath without extra parenthesis
    target_menu_item = menu_items[5]
    target_menu_item.click()

    # 3. Wait for 2 seconds
    
    time.sleep(5)

    # 6. Take a screenshot
    driver.save_screenshot("screenshot.png")  # The screenshot will be saved in the same directory as the script

finally:
    # Close the driver after everything is done
    driver.quit()
