package Java;

import java.util.ArrayList;
import java.util.List;

class MeczCS {

    boolean czyBombaPodlozona = false;
    List<Terrorysta> terrorysci = new ArrayList<Terrorysta>();
    List<Antyterrorysta> antyterrorysci = new ArrayList<Antyterrorysta>();

    public MeczCS() {
        Bron AK47 = new Bron("AK47", true);
        Bron M4A1S = new Bron("M4A1S", true);

        for (int i = 1; i <= 4; i++) {
            terrorysci.add(new Terrorysta("Terrorysta" + i, AK47, i == 1));
        }
        for (int i = 1; i <= 4; i++) {
            antyterrorysci.add(new Antyterrorysta("Antyterrorysta" + i, M4A1S));
        }
    }

    public void start() {
        for (Terrorysta terrorysta : terrorysci) {
            terrorysta.shoot();
        }
        for (Antyterrorysta antyterrorysta : antyterrorysci) {
            antyterrorysta.shoot();
        }
        terrorysci.get(0).podlozBombe();
        czyBombaPodlozona = true;
        antyterrorysci.get(0).rozbrojBombe();
        czyBombaPodlozona = false;
    }

}

public class Main {
    public static void main(String[] args) {
        MeczCS mecz = new MeczCS();
        mecz.start();
    }
}
