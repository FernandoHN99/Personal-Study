public class Spock extends Jogada {

    public Spock() {
        super(Enum.TESOURA,Enum.PEDRA );
    }

    @Override
    public Enum getTipo() {
        return Enum.SPOCK;
    }
    
}
