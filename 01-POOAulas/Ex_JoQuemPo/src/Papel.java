public class Papel extends Jogada{

    public Papel() {
        super(Enum.PEDRA,Enum.SPOCK );
    }

    @Override
    public Enum getTipo() {
        return Enum.PAPEL;
    }
    
}
