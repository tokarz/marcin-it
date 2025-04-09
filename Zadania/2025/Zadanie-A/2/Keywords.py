from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Keywords:

    def wyszukiwarka(self, szukaj):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            driver = seleniumlib.driver
            wait = WebDriverWait(driver, 10)

            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tdb-search-icon-svg")))
            element.click()

            element1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tdb-head-search-form-input")))
            element1.click()
            element1.send_keys(szukaj)

            element2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tdb-head-search-form-btn")))
            element2.click()



        except Exception as e:
            print(f"Error occurred: {e}")

    def kliknij_artykul1(self):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            driver = seleniumlib.driver
            wait = WebDriverWait(driver, 10)

            elementy = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".td-module-title")))

            element = elementy[0]

            wait.until(EC.visibility_of(element))

            element.click()

        except Exception as e:
            print(f"Error occurred: {e}")

    def kliknij_artykul2(self):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            driver = seleniumlib.driver
            wait = WebDriverWait(driver, 10)

            elementy = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".td-module-title")))

            element = elementy[1]

            wait.until(EC.visibility_of(element))

            element.click()

        except Exception as e:
            print(f"Error occurred: {e}")


    def kliknij_artykul_3(self):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            driver = seleniumlib.driver
            wait = WebDriverWait(driver, 10)

            elementy = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".td-module-title")))

            element = elementy[2]

            wait.until(EC.visibility_of(element))

            element.click()

        except Exception as e:
            print(f"Error occurred: {e}")


    def sprawdz_url(self, url):
        seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            driver = seleniumlib.driver
            wait = WebDriverWait(driver, 10)

            wait.until(EC.url_to_be(url))

            print(f"URL jest poprawny: {url}")

        except Exception as e:
            print(f"Error occurred: {e}")