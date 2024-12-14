from pom.Utilities.Utilities import Utilities

class SocialMedia:
    def __init__(self , page):
        self.page = page
        self.utils = Utilities(page)

    def click_facebook(self):
        resultUrl = self.utils.sprawdz_odnosnik("0", "https://www.facebook.com/czarnijaslo1910/")
        assert resultUrl == "https://www.facebook.com/czarnijaslo1910/"
        print("OK")

    def click_instagram(self): 
        resultUrl = self.utils.sprawdz_odnosnik("1", "https://www.instagram.com/czarni_1910_jaslo/")
        assert resultUrl == "https://www.instagram.com/czarni_1910_jaslo/"
        print("OK")
        
    
    def click_x(self): 
        resultUrl = self.utils.sprawdz_odnosnik("2", "https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910")
        assert resultUrl == "https://x.com/i/flow/login?redirect_after_login=%2Fczarnijaslo1910"
        print("OK")
        
    def click_yt(self):
        resultUrl = self.utils.sprawdz_odnosnik("3", "https://www.youtube.com/channel/UCrk8GobYCsKntXBQBUYK7Ww")
        assert resultUrl == "https://www.youtube.com/channel/UCrk8GobYCsKntXBQBUYK7Ww"
        print("OK")
        