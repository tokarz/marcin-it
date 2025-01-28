import utils.XPathSelectorSearcher;

public class POM_Aktualnosci {

    // KONSTRUTKOR
    POM_Aktualnosci() {
        // ZAINICJALIZOWAC KLASE
    }

    void Hello() {
        System.out.println("Hello");
    }

    // TYPY WBUDOWANE
    // JESLI MAMY TABLICE, TO BEDZIEMY UZYWAC PETLI
    Integer boo[] = new Integer[] { 1, 2, 3, 4, 5, 6, 7 };
    String[] qoo = new String[] { "a", "b" };

    // AMAZON
    String[] adresy = new String[] { "Krakow abc", "Wroclaw xyz", "ggg" }; // 3 element nie ma miasta!

    // TYPY NOWE, ZROBIONE PRZEZ USERA
    KlikaczNaButtony mojTyp;
    XPathSelectorSearcher searcher;
}

// KLASY = TYPY

// Typy: String, boolean, Integer, Double, Float
//

class Uczen {
    String imie;
    String nazwisko;
    String klasa;

    Uczen() {
        imie = "Jan";
        nazwisko = "Kowalski";
        klasa = "1A";
    }

    Uczen(String imie, String nazwisko, String klasa) {
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.klasa = klasa;
    }

}

class Main {

    void test() {

        Integer wiek = 7;
        // Integer wiekObiektowy = new Integer(7);

        String imie = "Jacek";
        // String imieObiektowe = new String("Jacek");

        // Jan Kowalski z 1A
        Uczen piotrek = new Uczen();

        // Jan Kowalski z 1A
        Uczen adam = new Uczen("Adam", "Majewski", "2B");

        /*
         * 
         * uczen = new Uczen()
         * 
         * 
         * 
         */

        // stwórz nową Zmienną TYPU uczen

        Klikacz searchField = new Klikacz("div[id='abc']", "CSS");
        searchField.kliknij_na();

        Klikacz searchField2 = new Klikacz("div[id='dupa']", "CSS");
        searchField2.kliknij_na();

        Klikacz searchField3 = new Klikacz(".button .item-356", "CSS");
        searchField3.kliknij_na();

        Klikacz searchField4 = new Klikacz("//div[@class='abc']", "XPATH");
        searchField4.kliknij_na();

    }

}

class Klikacz {
    String selektor;
    String slekctorType;

    Klikacz() {
        this.selektor = "div[id='abc']";
    }

    Klikacz(String selektor, String type) {
        this.selektor = selektor;
        this.slekctorType = type;
    }

    // Method OVERLOADING
    // PRZECIĄŻĄNIE METOD/FUNKCJI
    // funkcja == metoda
    boolean kliknij_na() {
        if (this.slekctorType == "CSS") {
            // selenium.driver.click(this.selektor)
        }
        if (this.slekctorType == "XPATH") {
            // selenium.driver.click(this.selektor)
        }

        return false;
    }

    boolean kliknij_na(String selektor) {

        return true;
    }

}

// CZASAMI MOWIMY O OGOLE A CZASAMI O SZCZEGOLE

// OGOLNYCH JEST MALO A SZCZEGOLNYCH DUZO

class Silnik {
    Integer pojemnosc;
    String nazwa;
    String typPaliwa;

    Silnik(Integer pojemnosc, String nazwa, String typPaliwa) {
        this.nazwa = nazwa;
        this.pojemnosc = pojemnosc;
        this.typPaliwa = typPaliwa;
    }

    void przedstawSie() {
        System.out.println("Hello " + this.nazwa);
    }
}

class Diesel extends Silnik {

    Diesel(Integer pojemnosc, String nazwa, String typPaliwa, String diesloweSprawy) {
        super(pojemnosc, nazwa, typPaliwa);
        this.diesloweSprawy = diesloweSprawy;
    }

    String diesloweSprawy;
}

class Benzyna extends Silnik {
    Benzyna(Integer pojemnosc, String nazwa, String typPaliwa, String benzynoweSprawy) {
        super(pojemnosc, nazwa, typPaliwa);
        this.benzynoweSprawy = benzynoweSprawy;
    }

    String benzynoweSprawy;
}

class Prad extends Silnik {
    Prad(Integer pojemnosc, String nazwa, String typPaliwa, String pojemnoscBaterii) {
        super(pojemnosc, nazwa, typPaliwa);
        this.pojemnoscBaterii = pojemnoscBaterii;
    }

    String pojemnoscBaterii;
}

class Test {

    void foo() {

        Diesel diesel = new Diesel(2, "ON", "Pontiac diesel", "Dieslowe parametry X Y Z");

    }
}