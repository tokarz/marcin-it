

public class Kalkulator {

    Integer dodaj(Integer a , Integer b){
        return a + b ;
    }

    Boolean czyWieksza(Integer a , Integer b){
        if(a > b){
            return true;
        }
        else{
            return false;
        }
    }

    void hello(){
        System.out.println("Hello");

    }
    
    public static void main(String[] args) {
        Kalkulator naszKalkulator = new Kalkulator();
        naszKalkulator.hello();
      

    }

}
