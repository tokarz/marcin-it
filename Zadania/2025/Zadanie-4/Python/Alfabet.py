class Alfabet:
    def __init__(self):
        self.litery = []

    def dodaj(self , litera):
        self.litery.append(litera)

    def usun(self , ktoraLitera):
        if 0 <= ktoraLitera < len(self.litery):  
            self.litery.pop(ktoraLitera)
        else:
            print(f"Nieprawidłowa pozycja: {ktoraLitera}")

    def wypisz(self):
        print (self.litery)

def alfabet():  
    alfabet = Alfabet()
    alfabet.dodaj("a")
    alfabet.dodaj("b")
    alfabet.dodaj("c")
    alfabet.dodaj("d")
    alfabet.dodaj("e")
    alfabet.dodaj("f")
    alfabet.dodaj("g")
    alfabet.dodaj("h")
    alfabet.dodaj("i")
    alfabet.dodaj("j")
    alfabet.dodaj("k")
    alfabet.usun(2)
    alfabet.usun(5)
    alfabet.usun(6)
    alfabet.wypisz()

alfabet()



