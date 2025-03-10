package Java;

public class Antyterrorysta extends Gracz {
    public Antyterrorysta(String nickname , Bron actualWeapon ){
        super(nickname, actualWeapon);
    }
    public void rozbrojBombe(){
        System.out.println(nickname + " rozbraja bombe ! . . .");
    }
    
}

