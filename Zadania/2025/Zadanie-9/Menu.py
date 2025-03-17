class Menu:
    # link tez musi miec wartosc domyslna, skoro wystepuje po isDropdown, dlatego
    # dodalem link = ""
    def __init__(self,  name , isDropdown = False, link = "", subMenus = [] ):
        self.name = name
        self.isDropdown = isDropdown
        self.link = link
        self.subMenus = subMenus