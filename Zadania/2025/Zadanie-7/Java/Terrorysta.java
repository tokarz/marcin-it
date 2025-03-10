package Java;

class Terrorysta extends Gracz{
    boolean czyMaBombe;
    public Terrorysta(String nickname ,Bron actualWeapon , boolean czyMaBombe){
        super(nickname, actualWeapon);
        this.czyMaBombe = czyMaBombe;
    }
    public void podlozBombe(){
        if (czyMaBombe){
            System.out.println(nickname + " podkłada bobmbe!");
        }else{
            System.out.println(nickname + " nie ma bomby!");
        }
    }
}
