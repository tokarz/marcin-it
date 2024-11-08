
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
            return 3
        else:
            print("Porazka")
            return 4
        
    finally:
        time.sleep(3)
        


openPage()
test("plate")  #1
test("bento")  #2
test("#fancy")  #3
test("plate apple")  #4
test("#fancy pickle")  #5
test("apple.small")  #6
test("orange.small")  #7
test("bento orange.small")  #8
test("plate , bento")  #9
test("*")  #10
test("plate *")  #11
test("plate + apple")  #12
test("bento ~ pickle")  #13
test("plate > apple")  #14
test("orange:first-child")  #15
test("plate :only-child")  #16
test(".small:last-child")  #17
test(":nth-child(3)")  #18
test("bento:nth-last-child(3)")  #19
test("apple:first-of-type")  #20
test(":nth-of-type(even)")  #21
test(":nth-of-type(2n+3)")  #22
test("apple:only-of-type")  #23
test(".small:last-of-type")  #24
test("bento:empty")  #25
test("apple:not(.small)")  #26
test("[for]")  #27 
test("plate[for]")  #28
test("[for='Vitaly']")  #29
test("[for^='Sa']")  #30
test("[for$='ato']")  #31
test("[for*='obb']")  #32
  

closePage()
