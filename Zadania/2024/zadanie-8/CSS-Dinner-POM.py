from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CSSDinner:
    driver = webdriver.Chrome()

    input_selector = '.input-strobe'
    enter_button_selector = '.enter-button'

    success_class='.level-header.completed'
    
    def __init__(self) -> None:
        pass
    
    def openPage(self):
        self.driver.get("https://flukeout.github.io/")

    def closePage(self):
        self.driver.quit()
    
    def test(self,tekst):
        try:
            input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.input_selector))
            )
            input.send_keys(tekst)
            
            time.sleep(1)
            
            button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.enter_button_selector))
            )
            
            button.click()
            time.sleep(1)
            
            isCompleted = self.driver.find_elements(By.CSS_SELECTOR, self.success_class)
            
            if(isCompleted):
                print("Sukces")
                return 3
            else:
                print("Porazka")
                return 4
            
        finally:
            time.sleep(3)
            

myTestObject = CSSDinner()

myTestObject.openPage()
myTestObject.test("plate")  #1
myTestObject.test("bento")  #2
myTestObject.test("#fancy")  #3
myTestObject.test("plate apple")  #4
myTestObject.test("#fancy pickle")  #5
myTestObject.test("apple.small")  #6
myTestObject.test("orange.small")  #7
myTestObject.test("bento orange.small")  #8
myTestObject.test("plate , bento")  #9
myTestObject.test("*")  #10
myTestObject.test("plate *")  #11
myTestObject.test("plate + apple")  #12
myTestObject.test("bento ~ pickle")  #13
myTestObject.test("plate > apple")  #14
myTestObject.test("orange:first-child")  #15
myTestObject.test("plate :only-child")  #16
myTestObject.test(".small:last-child")  #17
myTestObject.test(":nth-child(3)")  #18
myTestObject.test("bento:nth-last-child(3)")  #19
myTestObject.test("apple:first-of-type")  #20
myTestObject.test(":nth-of-type(even)")  #21
myTestObject.test(":nth-of-type(2n+3)")  #22
myTestObject.test("apple:only-of-type")  #23
myTestObject.test(".small:last-of-type")  #24
myTestObject.test("bento:empty")  #25
myTestObject.test("apple:not(.small)")  #26
myTestObject.test("[for]")  #27 
myTestObject.test("plate[for]")  #28
myTestObject.test("[for='Vitaly']")  #29
myTestObject.test("[for^='Sa']")  #30
myTestObject.test("[for$='ato']")  #31
myTestObject.test("[for*='obb']")  #32
  

myTestObject.closePage()