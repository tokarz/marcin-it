from playwright.sync_api import sync_playwright

def screenshot_full_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        page.screenshot(path="screenshot_full_page.png", full_page=True)
        browser.close()

screenshot_full_page()