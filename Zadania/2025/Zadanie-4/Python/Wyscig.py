class Czlowiek :
    def __init__ (  self , imie , nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko



class Auto :
    def __init__(self, marka , moc):
        self.marka = marka
        self.moc = moc

class Team :
    def __init__(self, nazwa , budzet):
        self.nazwa = nazwa
        self.budzet = budzet


class Wyscig:
    def __init__(self , ):
        self.kierowca1  = Czlowiek("Marcin" , "Iskrzycki")
        self.kierowca2 = Czlowiek ("Jan" , "Kowalski")
        self.auto1 = Auto("BMW" , "2000")
        self.auto2 = Auto("Mercedes" , "1998")
        self.kierowcyWAutach = []
        self.autaNaStarcie = []
        self.teamList = []
        