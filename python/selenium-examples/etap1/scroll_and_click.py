from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # GIVEN
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    # 2. Find all menu items matching the CSS selector
    menu_items = driver.find_elements(By.CSS_SELECTOR, '.standing-table-mini .place-5')

    # 3. Loop through each menu item
    
    # Scroll the menu item into view
    driver.execute_script("arguments[0].scrollIntoView();", menu_items[1])

    # 4. Wait for 2 seconds before clicking the menu item
    time.sleep(2)

    # WHEN
    # 5. Click on the menu item
    menu_items[1].click()

    time.sleep(4)

    driver.save_screenshot("czarni.png")  # The screenshot will be saved in the same directory as the script

    # (Optional) After clicking, navigate back to the previous page if needed
    # driver.back()

    # THEN (asercja! Assert)
    current_url = driver.current_url
    expected_url = "https://czarnijaslo.pl/club/czarni-jaslo/"  # Replace with your expected URL
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

finally:
    # 6. Close the driver after everything is done
    driver.quit()
