from playwright.sync_api import sync_playwright

def screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        page.screenshot(path="screenshot1.png")
        browser.close()

screenshot()