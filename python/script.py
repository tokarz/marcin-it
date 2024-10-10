from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get("http://czarnijaslo.pl")

# Select an element using a simple XPath like //a/b/c
element = driver.find_element(By.XPATH, "//div/ul/li/a")

# Perform an action with the selected element, e.g., click
element.click()

# Close the browser
driver.quit()