import java.util.ArrayList;
import java.util.List;

public class Alfabet {
    List<String> litery ;

    Alfabet(){
        litery =  new ArrayList<String>();   
    }
    public void dodaj(String litera){
        this.litery.add(litera);
    }
    public void usun(int pozycja){
        this.litery.remove(pozycja);
    }
    public void wypisz(){
        System.out.println(litery);
    }
    public static void main(String[] args) {
        Alfabet Alfabet = new Alfabet();
        Alfabet.dodaj("g");
        Alfabet.dodaj("c");
        Alfabet.dodaj("d");
        Alfabet.dodaj("f");
        Alfabet.dodaj("j");
        Alfabet.dodaj("x");
        Alfabet.dodaj("b");
        Alfabet.usun(2);
        Alfabet.usun(1);
        Alfabet.dodaj("a");
        Alfabet.dodaj("k");
        Alfabet.dodaj("m");
        Alfabet.wypisz();
    }
}

