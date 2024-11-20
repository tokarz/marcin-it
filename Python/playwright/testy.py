import re
from playwright.sync_api import sync_playwright
from newsy_strona_glowna import SprawdzNaglowekNewsa
from liczba_komentarzy_news import LiczbaKomentarzyNews
from bukmacherzy import Bukmacherzy
from sportbuzz_ranking import Sportbuzz

with sync_playwright() as driver:
    
    sprawdz_naglowek = SprawdzNaglowekNewsa()
    liczba_komentarzy = LiczbaKomentarzyNews()
    bukmacher = Bukmacherzy()
    sportbuzz =Sportbuzz()
   
    ########
    sprawdz_naglowek.sprawdz_naglowek_newsa(driver)
    ########
    liczba_komentarzy.sprawdz_liczbe_komentarzy_newsa(driver)
    ########
    bukmacher.sprawdz_bukmachera(driver) 
    
    bukmacher.sprawdz_bukmachera_2(driver)

    bukmacher.sprawdz_bukmachera_3(driver)

    bukmacher.sprawdz_bukmachera_4(driver)
    #######
    sportbuzz.sprawdzenie_rankingu(driver , "Łukasz22")

    sportbuzz.sprawdzenie_rankingu_miejsce(driver , "2" , "Mladen")

    sportbuzz.sprawdzenie_rankingu_miejsce(driver , "5" , "Bilon87")

    sportbuzz.sprawdzenie_rankingu_miejsce(driver , "8" , "brutalna_prawda")