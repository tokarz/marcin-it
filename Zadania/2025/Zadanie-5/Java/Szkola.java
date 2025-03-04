package Java;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Szkola {
    String patronSzkoly;
    int numerSzkoly;
    List<Klasa> klasy;

    Szkola(String patronSzkoly, int numerSzkoly, List<Klasa> klasy) {
        this.patronSzkoly = patronSzkoly;
        this.numerSzkoly = numerSzkoly;
        this.klasy = new ArrayList<Klasa>();
    }

    public void dodajKlase(Klasa klasa) {
        klasy.add(klasa);
    }
    public void wyswietlSzkole() {
        System.out.println("Szkoła im. " + patronSzkoly + " nr " + numerSzkoly);
        for (Klasa klasa : klasy) {
            System.out.println(klasa);
        }
    }

    public static void main(String[] args) {
        Szkola szkola = new Szkola("Mikolaj Kopernik", 4, null);
        String[] imiona = { "Daniel ", "Marcin ", "Damian ", "Dominik ", "Daria ", "Ewa ", " Patrycja " };
        String[] nazwiska = { "Kowalski ", "Nowak ", "Iskrzycki ", " Poliwka ", "Stachurski ", "Stoch ","Lewandowski " };
        Random random = new Random();

        for (char litera = 'A'; litera <= 'E'; litera++) {
            Klasa klasa = new Klasa(String.valueOf(litera), 1, null);
            for (int i = 0; i <=20; i++) {
                String imie = imiona[random.nextInt(imiona.length)];
                String nazwisko = nazwiska[random.nextInt(nazwiska.length)];
                double srednia = 1 + (5 * random.nextDouble());
                klasa.dodajUcznia(new Uczen(imie, nazwisko, i, srednia));
            }
            szkola.dodajKlase(klasa);
        }
            szkola.wyswietlSzkole();
        
    }
}
