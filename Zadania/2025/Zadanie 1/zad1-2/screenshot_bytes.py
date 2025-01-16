from playwright.sync_api import sync_playwright
import base64

def screenshot_bytes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        screenshot_bytes = page.screenshot()
        print(base64.b64encode(screenshot_bytes).decode())
        browser.close()

screenshot_bytes()