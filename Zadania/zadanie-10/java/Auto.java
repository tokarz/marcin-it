package java;

public class Auto{      
    Silnik silnik;
    Kolo[] kola;
    Hamulec[] hamulce;
    Kierownica kierownica;


    Auto(){
        this.silnik = new Silnik();
        this.kola = new Kolo[] {new Kolo(), new Kolo()};
        this.hamulce = new Hamulec[] {new Hamulec() , new Hamulec()};
        this.kierownica = new Kierownica();
        }

    public void opis() {
        System.out.println(silnik.hello());
            for (Kolo kolo : kola) {
        System.out.println(kolo.hello());
            }
            for (Hamulec hamulec : hamulce) {
        System.out.println(hamulec.hello());
            }
        System.out.println(kierownica.hello());
        }
        
    public static void main(String[] args) {
        Auto mojeAuto = new Auto();
        mojeAuto.opis();
    }
}