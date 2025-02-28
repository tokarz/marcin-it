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
    public String ileKofeiny(String kawa){
        switch (kawa) {
            case "Latte": return "20g";
            case "Czarna": return "25g";
            case "Cappucino": return "15g";
            case "Mokka": return "10g";
            case "Corto": return "22g";
            case "Espresso": return "80g";
            default:
                return "0g";
        }
    }
    public void ileKaloriMajaKawy(){
        for(int i = 0 ; i < kawaNaStanie.size(); i ++){
            String ileKofeiny = ileKofeiny(kawaNaStanie.get(i));
            System.out.println(ileKofeiny);
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
