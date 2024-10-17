from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()








def wejdz_na_strone(adres_www):
     driver.get(adres_www)
     poczekaj(3)


def poczekaj(czas):
    time.sleep(czas)

def player(driver):
    movie_player = driver.find_element("css selector", "#movie_player")
    movie_player.click()
    poczekaj(10)



def film_yt(adres_www):
    wejdz_na_strone(adres_www)
    player
    driver.quit()

##########
film_yt("https://www.youtube.com/watch?v=ouEl3qTLc0M&list=RDCLAK5uy_kLWIr9gv1XLlPbaDS965-Db4TrBoUTxQ8&index=2")
##########