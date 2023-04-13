public class Tesoura extends Jogada{

    public Tesoura() {
        super(Enum.PAPEL, Enum.LAGARTO);
    }
    @Override
    public Enum getTipo() {
        return Enum.TESOURA;
    }
        
    
}
