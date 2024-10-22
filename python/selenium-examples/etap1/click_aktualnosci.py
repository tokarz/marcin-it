from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    # 2. Wait until the element with CSS selector '.menu-item-327' is present
    wszystkie_opcje = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.menu-item-327'))
    )
    
    # 3. Find the second element and click it
    aktualnosci = wszystkie_opcje[1]
    aktualnosci.click()
    
    # 4. Wait until the navigation to the new page has completed
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    
    # 5. Verify the current URL
    current_url = driver.current_url
    expected_url = "https://czarnijaslo.pl/category/wydarzenia/"  # Replace with your expected URL
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

finally:
    # 6. Close the driver after everything is done
    driver.quit()