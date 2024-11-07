
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver (use Chrome in this case)
driver = webdriver.Chrome()

input_selector = '.input-strobe'
enter_button_selector = '.enter-button'

success_class='.level-header.completed'


def openPage():
    driver.get("https://flukeout.github.io/")

def closePage():
    driver.quit()

def test(tekst):
    try:
        
        
        input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, input_selector))
        )
        input.send_keys(tekst)
        
        time.sleep(1)
        
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, enter_button_selector))
        )
        
        button.click()
        time.sleep(1)
        
        isCompleted = driver.find_elements(By.CSS_SELECTOR, success_class)
        
        if(isCompleted):
            print("Sukces")
            return 5
        else:
            print("Porazka")
            return 5
        
    finally:
        time.sleep(3)
        


openPage()
test("plate")
test("bento")
test("")


closePage()
