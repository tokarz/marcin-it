public class Silnik{

    Integer pojemnosc;
    String nazwa;
    String paliwo;
    String id;

    Silnik(){
        pojemnosc = 2;
        nazwa = "Hybrydowy";
        paliwo = "Benzyna/Prad";
        id = "qwer123";
    }

    Silnik( Integer pojemnosc , String nazwa , String paliwo , String id){
        this.pojemnosc = pojemnosc;
        this.nazwa = nazwa;
        this.paliwo = paliwo;
        this.id = id;
    }

    void Hello(){
        System.out.println("Czesc , jestem " + this.nazwa + "i mam pojemnosc = " + this.pojemnosc);
    }

}




class Auto{
        String nazwa;
        Silnik silnik;

    Auto(){
        nazwa = "Porshe";
        silnik = new Silnik();
    }
    
    Auto(String nazwa , Silnik silnik){
        this.nazwa = nazwa;
        this.silnik = silnik;
    }
    }





class Diesel extends Silnik{
    Diesel(Integer pojemnosc , String nazwa , String paliwo , String id){
        super(pojemnosc , nazwa , paliwo , id);

    }
}

class Benzyna extends Silnik{
    Benzyna(Integer pojemnosc , String nazwa , String paliwo , String id){
        super(pojemnosc , nazwa , paliwo , id);
    }
}

class Prad extends Silnik{
    Prad(Integer pojemnosc , String nazwa , String paliwo , String id){
        super(pojemnosc , nazwa , paliwo , id);
    }

} 

