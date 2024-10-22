from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    # 2. Wait until the element with CSS selector '.menu-item-626' (Klub 100) is visible
    klub100 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.menu-item-626'))
    )
    klub100.click()

    # 3. Wait until the URL changes to the expected one
    WebDriverWait(driver, 10).until(EC.url_to_be("https://czarnijaslo.pl/category/klub-100/"))

    # 4. Verify the current URL
    current_url = driver.current_url
    expected_url = "https://czarnijaslo.pl/category/klub-100/"  # Replace with your expected URL
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

finally:
    # 5. Close the driver after everything is done
    driver.quit()