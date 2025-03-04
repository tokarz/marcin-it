package Java;

import java.util.ArrayList;
import java.util.List;

public class Klasa {
    String literaKlasy;
    int numerKlasy;
    List<Uczen>uczniowie;

    Klasa(String literaKlasy , int numerKlasy ,List<Uczen>uczniowie){
        this.literaKlasy = literaKlasy;
        this.numerKlasy = numerKlasy;
        this.uczniowie = new ArrayList<Uczen>();
    }
    
    public void dodajUcznia(Uczen uczen){
        uczniowie.add(uczen);
    }

}
