from pom.Utilities.Utilities import Utilities

class Tabela:
    def __init__(self , page):
        self.page = page
        self.utls = Utilities(page)

    def click_sokol_kolbuszowa_dolna(self):
        self.utls.tabela("Sokół Kolbuszowa D." , "https://czarnijaslo.pl/club/sokol-kolbuszowa-dolna/")
        
        print("OK")
    
        
    def click_jks_jaroslaw(self):
        self.utls.tabela("JKS Jarosław" , "https://czarnijaslo.pl/club/jks-jaroslaw/")
       
        print("OK")
    


    def click_jks_czarni_jaslo(self):
        self.utls.tabela("Czarni Jasło" , "https://czarnijaslo.pl/club/czarni-jaslo/")
        
        print("OK")

    def click_sokol_kamien(self):
        self.utls.tabela("Sokół Kamień" , "https://czarnijaslo.pl/club/sokol-kamien/")
        
        print("OK")

        
        