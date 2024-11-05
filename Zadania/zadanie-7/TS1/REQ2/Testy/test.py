from panel_glowny import PanelGlowny
import time

test = PanelGlowny()



#given
test.otworz_strone()

#when
test.click_aktualnosci()

#then
test.czy_na_stronie("https://czarnijaslo.pl/category/wydarzenia/")

time.sleep(3)


#G: uzytkownik jest na stronie glownej www.czarnijaslo.pl
test.otworz_strone()

#W: ustawia kursor myszy na przycisk "Klub 100" i klika na niego
test.click_klub100()

#T: zostaje przeniesiony na strone https://czarnijaslo.pl/category/klub-100/
test.czy_na_stronie("https://czarnijaslo.pl/category/klub-100/")


time.sleep(3)

test.otworz_strone()

test.click_klub()

test.kliknij_na("historia")

test.czy_na_stronie("https://czarnijaslo.pl/historia/")


time.sleep(3)

test.otworz_strone()

test.click_klub()

test.kliknij_na("sztab")

test.czy_na_stronie("https://czarnijaslo.pl/sztab-szkoleniowy/")

