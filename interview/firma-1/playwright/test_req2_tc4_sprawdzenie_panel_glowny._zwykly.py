from utilities import Utilities
from playwright.sync_api import sync_playwright

util = Utilities()


with sync_playwright() as driver:
    util.click_panel_glowny_zwykly(driver , "Aktualności" , "https://czarnijaslo.pl/category/wydarzenia/")
    util.click_panel_glowny_zwykly(driver , "Klub100" , "https://czarnijaslo.pl/category/klub-100/")
    util.click_panel_glowny_zwykly(driver , "Sponsoring" , "https://czarnijaslo.pl/sponsoring/")
    util.click_panel_glowny_zwykly(driver , "Akademia" , "https://www.facebook.com/APCzarniJaslo")