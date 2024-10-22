from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

try:
    # 1. Open the target webpage
    driver.get("https://czarnijaslo.pl/")  # Replace with the actual URL

    # 2. Wait until the element with CSS selector '.menu-item-10460' (Drużyny) is visible
    druzyny = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.menu-item-10460'))
    )
    druzyny.click()

    # 3. Wait until the next menu option '.menu-item-10362' (Juniorzy Młodsi) is visible
    juniorzymlodsi = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.menu-item-10362'))
    )
    juniorzymlodsi.click()

    # 4. Wait until the URL changes to the expected one
    WebDriverWait(driver, 10).until(EC.url_to_be("https://czarnijaslo.pl/juniorzy-mlodsi/"))

    # 5. Verify the current URL
    current_url = driver.current_url
    expected_url = "https://czarnijaslo.pl/juniorzy-mlodsi/"  # Replace with your expected URL
    if current_url == expected_url:
        print("URL verification passed!")
    else:
        print(f"URL verification failed! Expected: {expected_url}, but got: {current_url}")

finally:
    # 6. Close the driver after everything is done
    driver.quit()