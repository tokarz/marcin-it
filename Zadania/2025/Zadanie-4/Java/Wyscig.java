package Wyscig;

class Czlowiek {
    String imie;
    String nazwisko;

    Czlowiek(String imie, String nazwisko) {
        this.imie = imie;
        this.nazwisko = nazwisko;
    }
}

class Auto {
    String marka;
    int moc;

    Auto(String marka, int moc) {
        this.marka = marka;
        this.moc = moc;
    }
}

public class Wyscig {
    Czlowiek kierowca1;
    Czlowiek kierowca2;

    Auto auto1;
    Auto auto2;

    Czlowiek[] kierowcyWAutach;
    Auto[] autaNaStarcie;

    Wyscig() {
        this.kierowca1 = new Czlowiek("Marcin", "Iskrzycki");
        this.kierowca2 = new Czlowiek("Waclaw", "Nowak");

        this.auto1 = new Auto("Vw", 1998);
        this.auto2 = new Auto("Chevrolet", 4000);

        this.kierowcyWAutach = new Czlowiek[2];
        this.autaNaStarcie = new Auto[2];
    }

}