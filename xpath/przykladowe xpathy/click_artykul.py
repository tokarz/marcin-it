from playwright.sync_api import sync_playwright
import time

def click_artykul():
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless= False)
        page = browser.new_page( )
        page.goto("https://czarnijaslo.pl/")
        artykul1 = '//div[@class="td_block_inner"]//div[contains(@class , "td-posts-1")]'
        page.wait_for_selector(artykul1)
        page.click(artykul1)
        time.sleep(5)
        browser.close()
        print("OK")

click_artykul()
       