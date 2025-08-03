import javax.naming.spi.DirStateFactory.Result;

public abstract class Jogada implements Interface {
    private final Enum venco1;
    private final Enum venco2;

    public Jogada(Enum venco1, Enum venco2) {
        this.venco1 = venco1;
        this.venco2 = venco2;
    }

    public boolean verificarVenceu(Jogada jogada){
        boolean result = false;
        if(jogada.getTipo().equals(venco1))
            return true;
        else if(jogada.getTipo().equals(venco2))
            return true;
        return result;
    }


}
