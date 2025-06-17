import pytest
from playwright.sync_api import sync_playwright
import json

with open("config.json") as f:
    config = json.load(f)


def test_check_category_sport_teams():
  with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])

        text_to_find = ".teams h1"
        element = page.wait_for_selector(text_to_find)
        selector_text = element.text_content()
        assert selector_text == "Sport Teams" , print("nagłowek jest inny")

def test_check_category_players():
    with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])
    
        text_to_find = ".players h1"
        element = page.wait_for_selector(text_to_find)
        selector_text = element.text_content()
        assert selector_text == "Players" , print("nagłowek jest inny")

def test_check_category_coach():
    with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])
     
        text_to_find = ".coach h1"
        element = page.wait_for_selector(text_to_find)
        selector_text = element.text_content()
        assert selector_text == "Coach" , print("nagłowek jest inny")


        

#test_check_category_sport_teams()
#test_check_category_players()

        