from pom.Utilities.Utilities import Utilities


class Wyszukiwarka:
    def __init__(self , page):
        self.page = page
        self.utls = Utilities(page)

    def wyszukaj(self):
        self.utls.wyszukiwarka("czarni jasło" , 0)  
        print("OK")