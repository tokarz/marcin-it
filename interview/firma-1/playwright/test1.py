


# POM ! <-- klasy!
# PyTest
# próbować robić jak najwięcej generycznych funkcji



# Klasas Utils / Helper

class ClickUtils:
    def  click(selector)
    def  dblClick(selector)
    def  hover(selector)
    def  enter(selector)
    def clickAgreeToCookies()

# 
class PanelGorny:
    utils:ClickUtils
    
    def __init__(self):
        self.id = 'MojId'
        self.utils = ClickUtils()
        
    def kliknijNaSelektor(self, selektor):
        self.utils.clickAgreeToCookies()
        self.utils.click()
    
    def kliknijDwaRazyNaSelektor(self, selektor):
        self.utils.click()
        
    