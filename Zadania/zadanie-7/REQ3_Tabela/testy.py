from Tabela import Tabela
import time

test = Tabela()

#TC1-1
# Given
test.otworz_strone()
# When

# Then (sprawdzenie, asercja)
czyJestOk = test.pierwsze_miejsce_kolor()
if(czyJestOk):
    print("Sukces")
else:
    print("Porazka")
time.sleep(3)

#TC1-2
test.otworz_strone()

#Then
czyTestOk = test.drugie_miejsce_kolor()
time.sleep(3)

#TC1-3
test.otworz_strone()
test.ostatnie_miejsce_kolor()
time.sleep(3)

#TC3-1-1 czarni jaslo 
test.otworz_strone()
test.kliknij_w_zespol("czarni jaslo")
test.czy_na_stronie("https://czarnijaslo.pl/club/czarni-jaslo/")
time.sleep(3)

#TC3-1-2 sokol nisko
test.otworz_strone()
test.kliknij_w_zespol("sokol nisko")
test.czy_na_stronie("https://czarnijaslo.pl/club/sokol-nisko/")
time.sleep(3)

#TC3-1-2 strug tyczyn
test.otworz_strone()
test.kliknij_w_zespol("strug tyczyn")
test.czy_na_stronie("https://czarnijaslo.pl/club/strug-tyczyn/")
time.sleep(3)