import pytest
from playwright.sync_api import sync_playwright

def test_open_page_and_click():
    with sync_playwright() as driver:
        
        
        browser = driver.chromium.launch(headless=False)  # Set headless=True if you don't need a UI
        page = browser.new_page()

        # G
        # Navigate to the target URL
        page.goto("https://czarnijaslo.pl/")

        # Wait for the element with CSS selector and click on it
        # WHEN
        page.wait_for_selector("#menu-menu-3 .menu-item-327")  # Replace with your selector
        page.click("#menu-menu-3 .menu-item-327")
        
        page.wait_for_timeout(4000)
        
        # Assert the URL after clicking
        # Make sure/ check 
        
        # THEN
        assert page.url == "https://czarnijaslo.pl/category/wydarzenia/"  # Replace with expected URL

        browser.close()
        