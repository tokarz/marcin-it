package Java;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Gildia {
    String nazwaGildi;
    String liderGildi;
    List<Druzyna> listaDruzyn;

    Gildia(String nazwaGildi, String liderGildi, List<Druzyna> listaDruzyn) {
        this.nazwaGildi = nazwaGildi;
        this.liderGildi = liderGildi;
        this.listaDruzyn = new ArrayList<Druzyna>();
    }

    public void dodajDruzyne(Druzyna druzyna) {
        this.listaDruzyn.add(druzyna);
    }

    public Wojownik najsilniejszyWojownik() {
        Wojownik najsilniejszy = null;
        for (Druzyna druzyna : listaDruzyn) {
            for (Wojownik wojownik : druzyna.getCzlonkowie()) {
                if (najsilniejszy == null || wojownik.getSila() > najsilniejszy.getSila()) {
                    najsilniejszy = wojownik;
                }
            }
        }
        return najsilniejszy;
    }

    public Wojownik najmocniejszyPoziom() {
        Wojownik najwyzszyPoziom = null;

        for (Druzyna druzyna : listaDruzyn) {
            for (Wojownik wojownik : druzyna.getCzlonkowie()) {
                if (najwyzszyPoziom == null || wojownik.getPoziom() > najwyzszyPoziom.getPoziom()) {
                    najwyzszyPoziom = wojownik;
                }
            }
        }
        return najwyzszyPoziom;
    }

    public static void main(String[] args) {
        Gildia gildia = new Gildia("Cienie Valhalli", "Ragnar", null);
        String[] imiona = { "Thorin", "Eldrin", "Gorash", "Liriel", "Azog" };
        String[] rasy = { "Krasnolud", "Elf", "Ork", "Czlowiek" };
        String[] nazwyDruzyn = { "Wilki Północy", "Strażnicy Ognia", "Mroczne Ostrza" };
        Random random = new Random();
        for (String nazwa : nazwyDruzyn) {
            Druzyna druzyna = new Druzyna(nazwa, null);
            for (int i = 0; i < 5; i++) {
                Wojownik wojownik = new Wojownik(imiona[random.nextInt(imiona.length)],
                        rasy[random.nextInt(rasy.length)],
                        random.nextInt(100) + 1,
                        1 + random.nextDouble() * 9);
                druzyna.dodajWojownika(wojownik);  
            }
            gildia.dodajDruzyne(druzyna);
        }
        System.out.println("Najsilniejszy wojownik: " + gildia.najsilniejszyWojownik());
        System.out.println("Wojownik z najwyższym poziomem: " + gildia.najmocniejszyPoziom());
    }
}
