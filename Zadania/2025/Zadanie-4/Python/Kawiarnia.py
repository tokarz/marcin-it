class Kawiarnia:
    def __init__(self):
    
        self.kawaNaStanie = ["Latte", "Czarna", "Capuccino", "Mocca", "Corto", "Espresso"]
 
        self.kawaSprzedana = []

    def sprzedajKawe(self,kawa ):
        index = self.kawaNaStanie.index(kawa)
        self.kawaNaStanie.pop(index)
        self.kawaSprzedana.append(kawa)

    def pokazNaStanie(self):
        print("Kawa na stanie : " )
        for kawa in self.kawaNaStanie:
            print (f"Na stanie : {kawa}"  )

    def pokazSprzedane(self ):
        print("Sprzedane : " )
        for kawa in self.kawaSprzedana:
            print ( f"Sprzedana : {kawa}")

def kawa():
    kawiarnia = Kawiarnia()
    kawiarnia.sprzedajKawe("Latte")
    kawiarnia.sprzedajKawe("Espresso")
    kawiarnia.pokazNaStanie()
    kawiarnia.pokazSprzedane()

kawa()