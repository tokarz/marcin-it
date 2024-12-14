from playwright.sync_api import sync_playwright, Playwright
import pytest

@pytest.fixture(scope="function")
def przegladarka():  
    with sync_playwright() as playwright:    
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page 
        browser.close()
    
    
    
def test_click_aktualnosci(przegladarka):
    przegladarka.goto("https://czarnijaslo.pl/")
    aktualnosci = przegladarka.locator("#menu-menu-3").get_by_role("link", name="Aktualności")
    aktualnosci.click()
    przegladarka.wait_for_url("https://czarnijaslo.pl/category/wydarzenia/")
    assert przegladarka.url =="https://czarnijaslo.pl/category/wydarzenia/"
    print("OK")
    




