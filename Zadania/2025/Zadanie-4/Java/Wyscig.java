package Wyscig;


class Czlowiek{

    String  imie;
    String  nazwisko;

    Czlowiek(String imie , String nazwisko){

        this.imie = imie;
        this.nazwisko  = nazwisko;

    }


}

class Auto{
    String marka;
    int moc;

    Auto(String marka , int moc){
        this.marka = marka;
        this.moc = moc;

    }
}

public class Wyscig{

    Czlowiek czlowiek;
    Auto auto;

    Wyscig(){

        Czlowiek kierowca1 = new Czlowiek("Marcin", "Iskrzycki");
        Czlowiek kierowca2 = new Czlowiek("Waclaw", "Nowak");
        Auto auto1 = new Auto("Vw", 1998);
        Auto auto2 = new Auto("Chevrolet", 4000);

        Czlowiek [] kierowcyWAutach = new Czlowiek[0];
        Auto [] autaNaStarcie = new Auto[0];

    }

}