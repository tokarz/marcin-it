class Calendar:
    def __init__(self):
        self.dniTygodnia = ["Monday" , "Tuesday" , "Wensday" , "Thursday", "Friday" , "Saturday" , "Sunday" ]
        self.miesiace = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , " August" , "September", "October" , "Novamber", "December"]
        self.ileDni=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def ileDniWMiesiacu(self,ktoryMiesiac ):
        if 0 <= ktoryMiesiac <=11:
            return self.ileDni[ktoryMiesiac]
        else:
            return "___Błąd!!!___"
        
    def jakiDzien(self, numerDnia):
        if 0 <= numerDnia <=6:
            return self.dniTygodnia[numerDnia]
        else:
            return "___Błąd!!!___"
        
    def jakiMiesiac(self, numerMiesiaca):
        if 0 <= numerMiesiaca <11:
            return self.miesiace[numerMiesiaca]
        else:
            return "___Błąd!!!___"
        
    def dniMiesiaca(self, numerMiesiaca):
        if 0 <= numerMiesiaca <= 11:
            dniWMiesiacu = self.ileDni[numerMiesiaca]
            wynik = []
            pierwszyDzien= numerMiesiaca % 7
            for i in range(dniWMiesiacu):
                wynik.append(self.dniTygodnia[(pierwszyDzien + i) % 7])
            return wynik
        else:
            return "___Błąd!!!___"
        
##########################
calendar = Calendar()
print(calendar.jakiMiesiac(5))
print(calendar.ileDniWMiesiacu(7))
print(calendar.jakiDzien(6))
print(calendar.dniMiesiaca(8))
        