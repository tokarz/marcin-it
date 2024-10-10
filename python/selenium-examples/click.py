from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver (this example uses Chrome; you need to have ChromeDriver installed)
driver = webdriver.Chrome()

# Open the target webpage
driver.get("https://www.example.com")  # Replace with the actual URL

# Find the button using an appropriate selector (e.g., ID, class name, or XPath)
button = driver.find_element(By.ID, "button-id")  # Replace with the actual button's ID or other selector

# Click the button
button.click()

# Close the driver after the action
driver.quit()
