public class Pedra extends Jogada{

    public Pedra() {
        super(Enum.TESOURA, Enum.LAGARTO);
    }

    @Override
    public Enum getTipo() {
        return Enum.PEDRA;
    }

    
    
}
