class Silnik():
    def __init__(self, moc):
        self.moc = moc

    def pokaz_moc(self):
        return self.moc
    
class Nr_rejestracyjny():
    def __init__(self, miasto , nr):
        self.miasto = miasto
        self.nr = nr

    def wyswietl_nr(self):
       return self.miasto + self.nr
        
class Typ():
    def __init__(self, rodzaj):
        self.rodzaj = rodzaj

    def wyswietl_typ(self):
        return self.rodzaj 

class Standard():
    def __init__(self, standard):     
        self.standard = standard
    
    def wyswietl_standard(self):
        return self.standard

class Auto():
    def __init__(self , silnik : Silnik , nr_rejestracyjny : Nr_rejestracyjny , typ: Typ , standard: Standard):
        self.silnik = silnik
        self.nr_rejestracyjny = nr_rejestracyjny
        self.rodzaj = typ
        self.standard = standard


    def zmien_nr_rejestracyjny(self, nowy_nr_rejestracyjny):
        self.nr_rejestracyjny = nowy_nr_rejestracyjny

    def pokaz_moc_silnika(self):
        moc = self.silnik.pokaz_moc()
        self.przedstaw_auto(moc)
    


    def przedstaw_auto(self, moc):
        print("Auto " + self.rodzaj.wyswietl_typ() + "o nr rejestracyjnym " + self.nr_rejestracyjny.wyswietl_nr() + "i ma moc" + moc + " Ma standard " + self.standard.wyswietl_standard())


