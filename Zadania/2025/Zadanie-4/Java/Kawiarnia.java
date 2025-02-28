import java.util.ArrayList;
import java.util.List;

public class Kawiarnia {
    List<String> kawaNaStanie;
    List<String> kawaSprzedana;

    Kawiarnia() {
        kawaNaStanie = new ArrayList<String>();
        kawaNaStanie.add("Latte");
        kawaNaStanie.add("Czarna");
        kawaNaStanie.add("Capuccino");
        kawaNaStanie.add("Mocca");
        kawaNaStanie.add("Corto");
        kawaNaStanie.add("Espresso");
        kawaSprzedana = new ArrayList<String>();
    }

    public void sprzedajKawe(String kawa) {
        int index = kawaNaStanie.indexOf(kawa);
        if (index > 0) {
            kawaNaStanie.remove(index);
            kawaSprzedana.add(kawa);
        } else {
            System.out.println("Kawa niedostepna");
        }
    }

    public void pokazNaStanie() {
        System.out.println("Kawa na stanie : ");
        {
            for (int i = 0; i < kawaNaStanie.size(); i++) {
                System.out.println("Na stanie : " + kawaNaStanie.get(i));
            }
        }

    }

    public void pokazSprzedane() {
        System.out.println("Kawa sprzedana : ");
        {
            for (int i = 0; i < kawaSprzedana.size(); i++) {
                System.out.println("Sprzedane : " + kawaSprzedana.get(i));
            }
        }
    }

    public static void main(String[] args) {
        Kawiarnia Kawiarnia = new Kawiarnia();
        Kawiarnia.sprzedajKawe("Espresso");
        Kawiarnia.sprzedajKawe("Capuccino");
        Kawiarnia.sprzedajKawe("Czarna");
        Kawiarnia.pokazNaStanie();
        Kawiarnia.pokazSprzedane();
    }
}
