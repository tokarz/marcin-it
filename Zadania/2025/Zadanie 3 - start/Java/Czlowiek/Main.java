package Czlowiek;
public class Main {
    public static void main(String[] args) {
        Glowa glowa = new Glowa(40, "Niebieskie");
         // Dodaj Tułów, ręce i nogi i skonstruuj człowieja używając new Czlowiek(...)
        Tulow tulow = new Tulow(70, true);

        Reka prawaReka = new Reka(true, false, 44);
        Reka lewaReka = new Reka(false, true, 45);

        Noga prawaNoga = new Noga("prawa", 77);
        Noga lewaNoga = new Noga("Lewa", 77);
        
        
        Czlowiek czlowiek = new Czlowiek(glowa, tulow, prawaReka, lewaReka, prawaNoga, lewaNoga);

        
    }
 
    
      

}
