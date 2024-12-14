from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")
def przegladarka():  
    with sync_playwright() as playwright:    
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page 
        browser.close()

def test_click_stopka_mojejaslo(przegladarka):   
    przegladarka.goto("https://czarnijaslo.pl/")
    stopka_moje_jaslo = przegladarka.locator("aside").filter(has_text="Zaprzyjaźnione media").get_by_role("link")
    stopka_moje_jaslo.click()
    przegladarka.wait_for_url("https://mojejaslo.pl/")
    assert przegladarka.url == "https://mojejaslo.pl/"
    print ("OK")

