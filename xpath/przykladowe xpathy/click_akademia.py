from playwright.sync_api import sync_playwright
import time


def click_akademia():
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless= False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        akademia = '//li[contains(@class , "menu-item-20775")]//div[@class="tdb-menu-item-text"]'
        page.wait_for_selector(akademia)
        page.click(akademia)
        time.sleep(5)
        browser.close()
        print("OK")


click_akademia()




#'//li[contains(@class , "menu-item-20775")]//div[@class="tdb-menu-item-text"]'