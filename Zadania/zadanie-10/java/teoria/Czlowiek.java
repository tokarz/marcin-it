package teoria;

// Typ 
public class Czlowiek {

    public static void main(String[]... args) {
        //
    }
}

class Zwierze {
    String imie;
    Integer sila;
    Integer hp;

    public void zarycz() {
        System.out.println("NIE WIEM JAK");
    }
}

class ZwierzeRoslinozerne extends Zwierze {

}

class ZwierzeMiesozerne extends Zwierze {

}

class Tygrys extends ZwierzeMiesozerne {

    Boolean czyNiebezpieczny = true;

    public void zarycz() {
        System.out.println("RAAAAAAAAAAAAAAAAAAAR");
    }
    
}

class Slon extends ZwierzeRoslinozerne {

    Boolean czyNiebezpieczny = false;

    public void zarycz() {
        System.out.println("TRUUUUUUUUUUUUU");
    }
}

class Malpa extends ZwierzeRoslinozerne {
    Boolean czyNiebezpieczny = false;
}

class Ptak extends ZwierzeRoslinozerne {

}

class Zoo {
    Malpa malpa;
    Tygrys tygrys;
    Slon slon;

    public boolean Fight(Zwierze pierwsze, Zwierze drugie) {

        return false;
    }

}

// Dzielimy KLASY na 2 główne rodzaje - Klasy z DANYMI i Klasy które coś robią

class OpcjaMenuGlownego {
    // DOSTEP DO ELEMENTU W KLASIE PUBLICZNY
    public String tytul;

    // DOSTEP DO ELEMENTU W KLASIE OGRANICZONY
    protected String toWidzaTylkoMojeDzieci;

    // DOSTEP DO ELEMENTU W KLASIE ZAKAZANY
    private String klasaCSS;
}

// Akademia JEST opcją Menu głównego
class Aktualnosci extends OpcjaMenuGlownego {

    public void createPanel() {
        this.tytul = "Aktualnosci";
        this.toWidzaTylkoMojeDzieci = "LALA";
    }
}

// Akademia JEST opcją Menu głównego
class Klub extends OpcjaMenuGlownego {

}

// Akademia JEST opcją Menu głównego
class Akademia extends OpcjaMenuGlownego {

}

// POM
class CzarniJaslo {
    Aktualnosci aktualnosci;
    Klub Klub;
    Akademia akademia;

    public void foo() {
        aktualnosci.tytul = "Aktualnosci";

    }
}

class RadioFuji extends Radio {

    public boolean zrobTestOpornikow() {
        return true;
    }
}

class Radio {

    // public
    public String przelacznikGlosnosci;
    public String przelacznikOnOff;

    public boolean wlacz() {
        return true;
    }

    public boolean wylacz() {
        return true;
    }

    // private
    private String okablowanie;
    private String zabezpieczenieNapiecia;

    public boolean zrobTestOpornikow() {
        if (okablowanie == "ABC") {
            return false;
        }

        return true;
    }

}