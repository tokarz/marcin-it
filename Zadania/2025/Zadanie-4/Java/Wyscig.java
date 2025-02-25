import java.util.ArrayList;
import java.util.List;

class Czlowiek {
    String imie;
    String nazwisko;

    Czlowiek(String imie, String nazwisko) {
        this.imie = imie;
        this.nazwisko = nazwisko;
    }
}

class Auto {
    String marka;
    int moc;

    Auto(String marka, int moc) {
        this.marka = marka;
        this.moc = moc;
    }
}

class Team {
    String nazwa;
    int budzet;

}



public class Wyscig {
    Czlowiek kierowca1;
    Czlowiek kierowca2;

    Auto auto1;
    Auto auto2;

    List<Czlowiek> kierowcyWAutach = new ArrayList<Czlowiek>();
    List<Auto> autaNaStarcie = new ArrayList<Auto>();
    List<Team> teamyList = new ArrayList<Team>();


    Wyscig() {
        this.kierowca1 = new Czlowiek("Marcin", "Iskrzycki");
        this.kierowca2 = new Czlowiek("Waclaw", "Nowak");

        this.auto1 = new Auto("Vw", 1998);
        this.auto2 = new Auto("Chevrolet", 4000);
    }

        public void  getIntoCar(Czlowiek kierowca ,Auto  auto){
            this.kierowcyWAutach.add(kierowca);
            this.autaNaStarcie.add(auto);
        }

        public Czlowiek ktoNaStarcie(int numer){
            return this.kierowcyWAutach.get(numer);
        }

        public Auto jakieAuto(int numer){
            return this.autaNaStarcie.get(numer);
        }
        public Team jakiTeam(int numer){
            return this.teamyList.get(numer);
        }
        public void wyswietlKierowcow(){
            for(int i = 0 ; i < this.kierowcyWAutach.size() ; i++){
                System.out.println(this.kierowcyWAutach.get(i));
            }
        }
        public void wyswietlAuta(){
            for(int i = 0 ; i < this.autaNaStarcie.size(); i++){
                System.out.println(this.autaNaStarcie.get(i));
            }
        }
        public void wyswietlTeamy(){
            for(int i = 0 ; i < this.teamyList.size(); i++){
                System.out.println(this.teamyList.get(i));
            }
        }
}