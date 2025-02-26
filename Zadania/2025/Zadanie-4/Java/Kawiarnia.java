import java.util.ArrayList;
import java.util.List;

public class Kawiarnia {
    List<String>kawaNaStanie;
    List<String>kawaSprzedana;

    Kawiarnia(){
        kawaNaStanie = new ArrayList<String>();
        kawaNaStanie.add("Latte");
        kawaNaStanie.add("Czarna");
        kawaNaStanie.add("Capuccino");
        kawaNaStanie.add("Mocca");
        kawaNaStanie.add("Corto");
        kawaNaStanie.add("Espresso");
        kawaSprzedana = new ArrayList<String>();
    }
    public void sprzedajKawe(String kawa){
        int index = kawaNaStanie.indexOf(kawa);
		kawaNaStanie.remove(index);
        kawaSprzedana.add(kawa);
        }
    public void pokazNaStanie(){
        System.out.println(kawaNaStanie);
    }
    public void pokazSprzedane(){
        System.out.println(kawaSprzedana);
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
