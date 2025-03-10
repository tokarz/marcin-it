package Java;

public class Gracz{
    String nickname;
    Bron actualWeapon;
    Gracz(String nickname , Bron actualWeapon){
        this.nickname = nickname;
        this.actualWeapon = actualWeapon;
    }
    public void shoot(){
        if (actualWeapon != null){
            actualWeapon.shoot();
            }
        else{
            System.out.println(nickname +" nie posiada broni !");
        }
    }
    public void changeWeapon(Bron newWeapon){
        this.actualWeapon = newWeapon;
        System.out.println(nickname + "changed weapon for : " + newWeapon);
    }
}

