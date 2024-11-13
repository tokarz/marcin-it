import pytest
from playwright.sync_api import sync_playwright

def test_open_page_and_click():
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless=False)  
        page = browser.new_page()

        page.goto("https://czarnijaslo.pl")

        page.wait_for_selector("#menu-menu-3 .menu-item-20775")

        page.click("#menu-menu-3 .menu-item-20775")

        page.wait_for_url("https://www.facebook.com/APCzarniJaslo")

        assert page.url == "https://www.facebook.com/APCzarniJaslo"




#'#menu-menu-3 .menu-item-20775





