package Java;

import java.util.ArrayList;
import java.util.List;

public class Druzyna {
    String nazwaDruzyny;
    List<Wojownik> czlonkowie;

    Druzyna(String nazwaDruzyny, List<Wojownik> czlonkowie) {
        this.nazwaDruzyny = nazwaDruzyny;
        this.czlonkowie = new ArrayList<Wojownik>();
    }
    public void dodajWojownika(Wojownik wojownik){
        this.czlonkowie.add(wojownik);
    }
    public List<Wojownik> getCzlonkowie() { return czlonkowie; }
}
