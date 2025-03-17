from Zespol import Zespol

class Table:
    def __init__(self, klasyfikacja = dict):
        self.zespoly = [Zespol]
        self.klasyfikacja = klasyfikacja

    def dodaj_druzyne(self, team = Zespol):
        self.zespoly.append(team)
        self.klasyfikacja[team.name] = {
            "nazwa": team.nazwa,
            "punkty": team.punkty,
            "wygrane": team.wygrane,
            "remisy": team.remisy,
            "przegrane": team.przegrane
        }