from CzarniJaslo import CzarniJaslo
from Menu import Menu
from Table import Table
from Zespol import Zespol

O_KLUBIE = Menu("O Klubie", False, "https://czarnijaslo.pl/o-klubie/")
WLADZE = Menu("Władze", False, "https://czarnijaslo.pl/wladze-klubu/")
SZTAB = Menu("Sztab", False, "https://czarnijaslo.pl/sztab-szkoleniowy/")
HISTORIA = Menu("Historia", False, "https://czarnijaslo.pl/historia/")
STATUT = Menu("Status", False, "https://czarnijaslo.pl/statut-klubu/")

SENIORZY = Menu("Seniorzy", False, "https://czarnijaslo.pl/kadra-seniorow/")
REZERWY_U19 = Menu("Rezerwy U19", False, "https://czarnijaslo.pl/kadra-zespolu-rezerw/")
JUNIORZY_MLODSI = Menu("Juniorzy Młodsi", False, "https://czarnijaslo.pl/juniorzy-mlodsi/")
TRAMPKARZE_STARSI = Menu("Trampkarze starsi", False, "https://czarnijaslo.pl/trampkarze-starsi/")
TRAMPKARZE_MLODSI = Menu("Trampkarze młodsi", False, "https://czarnijaslo.pl/trampkarze-mlodsi/")

IV_LIGA_PODKARPACKA = Menu("IV Liga Podkarpacka", False, "https://czarnijaslo.pl/competition/4-liga-podkarpacka/")
OKREGOWY_PUCHAR_POLSKI = Menu("Okręgowy puchar Polski", False, "https://czarnijaslo.pl/competition/okregowy-puchar-polski/")


class Main:
    # to co bedziemy uzywac w metodach musimy wyciągnąć do klasy
    menuOptions = []
    table = Table()
    
    def __init__(self):
        
        
        aktualnosci = Menu("Aktualnosci", False, "https://czarnijaslo.pl/category/wydarzenia/");
        subMenusClub = [O_KLUBIE, WLADZE, SZTAB, HISTORIA, STATUT]
        subMenusTeams = [SENIORZY, REZERWY_U19, JUNIORZY_MLODSI, TRAMPKARZE_STARSI, TRAMPKARZE_MLODSI]
        subMenusGames = [IV_LIGA_PODKARPACKA, OKREGOWY_PUCHAR_POLSKI]
        
        klub = Menu("Klub", True, "", subMenusClub)
        
        self.menuOptions.append(aktualnosci)
        self.menuOptions.append(klub)
        self.menuOptions.append(subMenusTeams)
        self.menuOptions.append(subMenusGames)
        

        
        self.table.dodaj_druzyne(Zespol("Czarni Jaslo", "25", "10" , "8" , "6")),
        self.table.dodaj_druzyne(Zespol("Sokol Nisko", "15" , "5" , "12" , "10")),
        self.table.dodaj_druzyne(Zespol("Iglopol Debica" , "20" , "8" , "8" , "9")),
        self.table.dodaj_druzyne(Zespol("Stal Sanok" , "26" , "11" , "7" , "5"))

        #self.czarnijaslo = CzarniJaslo(menuOptions = menu_options , table = table)
        # tutaj przekazujemy utworzone zmienne, nie musimy ich przypisywać w ciele funkcji
        self.czarnijaslo = CzarniJaslo(self.menuOptions , self.table)

	    
