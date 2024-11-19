from kalkulator import Kalkulator

#klasa Fizyk oblicza predkosc, przyspieszenie , 
#predkosc = S/t
#przyspieszenie= V/t
#zdefiniuj 2 metody oblicz predkosc , oblicz przyspieszenie i uzyj do tego klasy kalkulator



class Fizyk:
    def __init__(self):
        self.kalkulator = Kalkulator()

    def oblicz_przyspieszenie ( self , V , t):
        self.kalkulator.podziel(V , t)

    def oblicz_predkosc( self , S , t):
        self.kalkulator.podziel(S , t)

einstain = Fizyk()

einstain.oblicz_predkosc(4 , 2)



