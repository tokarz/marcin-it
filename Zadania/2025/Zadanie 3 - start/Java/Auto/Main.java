package Auto;

public class Main {

    public static void main(String[] args) {
        
        Kolo kolo = new Kolo(89, "wysoki");
        Silnik silnik = new Silnik(1499, "spalinowy");
        SkrzynaBiegow skrzynaBiegow = new SkrzynaBiegow(6, true);
        Kierownica kierownica = new Kierownica(true);

        Auto auto = new Auto(kolo, silnik, skrzynaBiegow, kierownica);

    }
    
}
