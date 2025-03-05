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
    
    public Uczen prymus() {
        Uczen najlepszyUczen = null;
        double najwyzszaSrednia = -1;

        for (Klasa klasa : klasy) {
            for (Uczen uczen : klasa.uczniowie) {
                if (uczen.sredniaOcen > najwyzszaSrednia) {
                    najwyzszaSrednia = uczen.sredniaOcen;
                    najlepszyUczen = uczen;
                }
            }
        }
        return najlepszyUczen;
    }

    public Uczen zdolnyAleLen() {
        Uczen najgorszyUczen = null;
        double najnizszaSrednia = 6.1; 

        for (Klasa klasa : klasy) {
            for (Uczen uczen : klasa.uczniowie) {
                if (uczen.sredniaOcen < najnizszaSrednia) {
                    najnizszaSrednia = uczen.sredniaOcen;
                    najgorszyUczen = uczen;
                }
            }
        }
        return najgorszyUczen;
    }

    public static void main(String[] args) {
        Szkola szkola = new Szkola("Mikolaj Kopernik", 4, null);
        String[] imiona = { "Daniel ", "Marcin ", "Damian ", "Dominik ", "Daria ", "Ewa ", " Patrycja " };
        String[] nazwiska = { "Kowalski ", "Nowak ", "Iskrzycki ", " Poliwka ", "Stachurski ", "Stoch ","Lewandowski " };
        Random random = new Random();

        for (char litera = 'A'; litera <= 'E'; litera++) {
            Klasa klasa = new Klasa(String.valueOf(litera), 1, null);
            for (int i = 1; i <=20; i++) {
                String imie = imiona[random.nextInt(imiona.length)];
                String nazwisko = nazwiska[random.nextInt(nazwiska.length)];
                double srednia = 1 + (5 * random.nextDouble());
                klasa.dodajUcznia(new Uczen(imie, nazwisko, i, srednia));
            }
            szkola.dodajKlase(klasa);
        }
            szkola.wyswietlSzkole();
            Uczen prymus = szkola.prymus();
            Uczen zdolnyAleLen = szkola.zdolnyAleLen();
            System.out.println(prymus);
            System.out.println(zdolnyAleLen);
        
    }
}
