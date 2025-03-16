package Java;

public class Wojownik{
    String imie;
    String rasa;
    int level;
    double sila;
    Wojownik(String imie , String rasa , int level , double sila){
        this.imie = imie;
        this.rasa = rasa;
        this.level = level;
        this.sila = sila;
    }
    @Override
    public String toString() {
        return "Wojownik [Imie=" + imie + ", Rasa=" + rasa + ", Siła=" + sila + ", Poziom=" + level + "]";
    }
    public double getSila() { 
        return sila; 
    };
    public int getPoziom(){
        return level;
    }
}