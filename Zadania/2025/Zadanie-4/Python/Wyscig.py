class Czlowiek :
    def __init__ (  self , imie , nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko



class Auto :
    def __init__(self, marka , moc):
        self.marka = marka
        self.moc = moc






class Wyscig:
    def __init__(self , ):
        kierowca1  = Czlowiek("Marcin" , "Iskrzycki")
        kierowca2 = Czlowiek ("Jan" , "Kowalski")
        auto1 = Auto("BMW" , "2000")
        auto2 = Auto("Mercedes" , "1998")
        self.kierowcyWAutach = [Czlowiek]
        self.autaNaStarcie = [Auto]
        
        