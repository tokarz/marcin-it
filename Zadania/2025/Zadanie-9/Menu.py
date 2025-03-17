class Menu:
    def __init__(self,  name , isDropdown = False, link ):
        self.name = name
        self.isDropdown = isDropdown
        self.link = link
        self.subMenus = [Menu]