import java.util.ArrayList;
import java.util.List;

public class Petle_i_listy {
    // Tablica ma taką długość jaką jej powiemy, że ma mieć
    // String[] alfabet = new String[20]; // NA SZTYWNO TYLKO 20 ARRAY <-- tablica

    List<String> alfabetLepszy = new ArrayList<String>(); // DYNAMICZNA TABLICA KTORA ROSNIE SAMA LISTA

    public void WstawLitery() {
        // wstawanie
        this.alfabetLepszy.add("a");
        this.alfabetLepszy.add("b");
        this.alfabetLepszy.add("c");
        this.alfabetLepszy.add("e"); //
        this.alfabetLepszy.add("f");

        // pobierania
        this.alfabetLepszy.get(0); // a
        this.alfabetLepszy.get(1); // b
        this.alfabetLepszy.get(2); // c
        this.alfabetLepszy.get(3); // d

        this.alfabetLepszy.remove(3);

        // usun wszystko
        this.alfabetLepszy.clear();

    }

    public void WypiszLitery() {
        // Listy idą w parze z pętlami

        // pętle - iterują (iteracja)
        // Zacznij od 0; Dopóki nasz indeks "i" nie przekroczy rozmiaru tablicy,
        // zwiększaj go o 1
        for (int i = 0; i < this.alfabetLepszy.size(); i++) {
            // jesli lista ma 20 elementow, to i bedzie mial wartosci
            // 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
            this.alfabetLepszy.get(i);
        }

    }
}
