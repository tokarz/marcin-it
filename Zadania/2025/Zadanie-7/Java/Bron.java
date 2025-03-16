package Java;

public class Bron {
    String nazwaBroni;
    boolean czyAutomat;

    Bron(String nazwaBroni, boolean czyAutomat) {
        this.nazwaBroni = nazwaBroni;
        this.czyAutomat = czyAutomat;
    }

    public void shoot() {
        if (czyAutomat) {
            System.out.println(nazwaBroni + " RATATATATATAT!");
        } else {
            System.out.println(nazwaBroni + "BOOM!");
        }
    }
}
