from klasa import Klasa

class Szkola:
    def __init__(self , patron , numerSzkoly , klasy):
        self.patron = patron
        self.numerSzkoly = numerSzkoly
        self.klasy = [Klasa]
    
    def dodajKlase(self ,klasa):
        self.klasy.append(klasa)

    def wyswietlSzkole(self ,) :
        print(f"Szkola im  {self.patron} nr : {self.numerSzkoly}")
        for klasa in self.klasy:
            print(klasa)

       


        
        