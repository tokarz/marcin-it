from panel_glowny import PanelGlowny
import time

test = PanelGlowny()


#TC4-1
#given
test.otworz_strone()
#when
test.click_aktualnosci()
#then
test.czy_na_stronie("https://czarnijaslo.pl/category/wydarzenia/")
time.sleep(3)

#TC4-2
#G: uzytkownik jest na stronie glownej www.czarnijaslo.pl
test.otworz_strone()
#W: ustawia kursor myszy na przycisk "Klub 100" i klika na niego
test.click_klub100()
#T: zostaje przeniesiony na strone https://czarnijaslo.pl/category/klub-100/
test.czy_na_stronie("https://czarnijaslo.pl/category/klub-100/")



##TC4-3
test.otworz_strone()
test.click_sponsoring()
test.czy_na_stronie("https://czarnijaslo.pl/sponsoring/")
time.sleep(3)

##TC4-4
test.otworz_strone()
test.click_akademia()
test.czy_na_stronie("https://www.facebook.com/APCzarniJaslo")
time.sleep(3)

#TC3-1
test.otworz_strone()
test.click_klub()
test.kliknij_na("o klubie")
test.czy_na_stronie("https://czarnijaslo.pl/o-klubie/")

#TC3-2
test.otworz_strone()
test.click_druzyny()
test.kliknij_na("seniorzy")
test.czy_na_stronie("https://czarnijaslo.pl/kadra-seniorow/")
time.sleep(3)

#TC3-3
test.otworz_strone()
test.click_rozgrywki()
test.kliknij_na("IV liga")
test.czy_na_stronie("https://czarnijaslo.pl/competition/4-liga-podkarpacka/")
time.sleep(3)

#TC3-4
test.otworz_strone()
test.click_kibice()
test.kliknij_na("bilety")
test.czy_na_stronie("https://czarnijaslo.pl/bilety/")
time.sleep(3)


#TC3-5
time.sleep(3)
test.otworz_strone()
test.click_klub()
test.kliknij_na("historia")
test.czy_na_stronie("https://czarnijaslo.pl/historia/")
time.sleep(3)

#TC3-6
test.otworz_strone()
test.click_klub()
test.kliknij_na("sztab")
test.czy_na_stronie("https://czarnijaslo.pl/sztab-szkoleniowy/")

