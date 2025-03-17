from CzarniJaslo import CzarniJaslo
from Menu import Menu
from Table import Table
from Zespol import Zespol


class Main:
    def __init__(self):
        menu_options = [
            Menu(name="Aktualnosci", isDropdown=False, link="https://czarnijaslo.pl/aktualnosci"),
            Menu(name="Rozgrywki", isDropdown=True, link="https://czarnijaslo.pl/rozgrywki", 
                subMenu=[Menu(name="IV liga podkarpacka", isDropdown=False, link="https://czarnijaslo.pl/rozgrywki/IVliga"),
                         Menu(name="Okregowy Puchar Polski", isDropdown=False, link="https://czarnijaslo.pl/rozgrywki/OkregowyPucharPolski")]),
            Menu(name="Klub100", isDropdown=False, link="https://czarnijaslo.pl/Klub100"),
            Menu(name="Kibice", isDropdown=True, link="https://czarnijaslo.pl/Kibice"),
                subMenu2=[Menu(name="Bilety wstepu na mecze" , isDropdown= False , link= "https://czarnijaslo.pl/Kibice/bilety" ),
                          Menu(name= "Koszulki meczowe" , isDropdown = False , link = "https://czarnijaslo.pl/Kibice/koszulki")]
                          ]

        table = Table()
        table.dodaj_druzyne(Zespol("Czarni Jaslo", "25", "10" , "8" , "6")),
        table.dodaj_druzyne(Zespol("Sokol Nisko", "15" , "5" , "12" , "10")),
        table.dodaj_druzyne(Zespol("Iglopol Debica" , "20" , "8" , "8" , "9")),
        table.dodaj_druzyne(Zespol("Stal Sanok" , "26" , "11" , "7" , "5"))

        self.czarnijaslo = CzarniJaslo(menuOptions = menu_options , table = table)
