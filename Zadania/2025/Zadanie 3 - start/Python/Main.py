from Czlowiek import Czlowiek
from Reka import Reka
from Noga import Noga
from Tulow import Tulow
from Glowa import Glowa




        
def main():
    nowy_czlowiek = Czlowiek(
        rekaPrawa = Reka(True ,False , 45),
        rekaLewa= Reka(False , True , 44),
        nogaPrawa= Noga( "prawa" , 76),
        nogaLewa= Noga("lewa" , 75),
        tulow= Tulow(78 , True),
        glowa= Glowa(45 , "zielony")
        )
    
    print(nowy_czlowiek)

main()
        
            


    
        
   
       
