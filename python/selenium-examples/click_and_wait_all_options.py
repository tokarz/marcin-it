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
    menu_items = driver.find_elements(By.CSS_SELECTOR, '#menu-menu-3 .menu-item i.tdb-sub-menu-icon')

    # 3. Loop through each menu item
    for index, item in enumerate(menu_items):
        print(f"Clicking on menu item {index + 1}")

        # Scroll the menu item into view if necessary (optional, in case of hidden elements)
        # driver.execute_script("arguments[0].scrollIntoView();", item)

        # 4. Wait for 2 seconds before clicking the menu item
        time.sleep(2)

        # 5. Click on the menu item
        item.click()

        time.sleep(1)

        driver.save_screenshot(f"screenshot_{index + 1}.png")

        # (Optional) After clicking, you could navigate back to the previous page if needed:
        # driver.back()  # Uncomment if you need to navigate back to click the next item

finally:
    # 6. Close the driver after everything is done
    driver.quit()
