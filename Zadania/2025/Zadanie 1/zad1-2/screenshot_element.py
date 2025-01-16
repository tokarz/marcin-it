from playwright.sync_api import sync_playwright
import time

def screenshot_element():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        locator = page.locator(".tdm-inline-image-wrap").first
        time.sleep(3)
        
        locator.screenshot(path="screenshot_element.png")
        browser.close()

screenshot_element()