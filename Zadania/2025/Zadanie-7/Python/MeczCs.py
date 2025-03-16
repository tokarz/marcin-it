from Bron import Bron
from Terrorysta import Terrorysta
from Antyterrorysta import Antyterrorysta



class MeczCs:
    def __init__(self):
        czyBombaPodlozona = False
        self.terrorysci = []
        self.antyterrorysci = []


    def start(self):
        for terrorysta in self.terrorysci :
            terrorysta.shoot()

        for antyterrorysta in self.antyterrorysci:
            antyterrorysta.shoot()

        if self.terrorysci:
            self.terrorysci[0].podlozBombe()
            self.czyBombaPodlozona = True
        if self.antyterrorysci:
            self.antyterrorysci[0].rozbrojBombe()
            self.czyBombaPodlozona = False