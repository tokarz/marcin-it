from playwright.sync_api import sync_playwright
import base64

def zdekoduj_obrazek(screenshot_bytes):
    return base64.b64encode(screenshot_bytes).decode()










def screenshot_bytes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        screenshot_bytes = page.screenshot()
        print(zdekoduj_obrazek(screenshot_bytes))
        browser.close()

screenshot_bytes()