from playwright.sync_api import sync_playwright
import time


def click_yt():
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless= False)
        page = browser.new_page()
        page.goto("https://czarnijaslo.pl/")
        yt_selector = '//div[contains(@class , "tdm-social-wrapper")]//div[@class = "tdm-social-item-wrap"]//a[@class = "tdm-social-item"]//i[contains(@class , "td-icon-youtube")]'
        page.wait_for_selector(yt_selector)
        page.click(yt_selector)
        time.sleep(5)
        browser.close()
        print("OK")

click_yt()

#'//div[contains(@class , "tdm-social-wrapper")]//div[@class = "tdm-social-item-wrap"]//a[@class = "tdm-social-item"]//i[contains(@class , "td-icon-youtube")]'