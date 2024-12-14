from playwright.sync_api import sync_playwright

class CzarniJaslo:
    def __init__(self):
        self.id = "czarnijaslo"


    def czarnijaslo(self):
        with sync_playwright() as playwright:
            self.browser = playwright.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            self.page.goto("https://czarnijaslo.pl/")
            return self.page
        