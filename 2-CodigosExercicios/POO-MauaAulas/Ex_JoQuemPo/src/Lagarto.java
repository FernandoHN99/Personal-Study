public class Lagarto extends Jogada {

    public Lagarto() {
        super(Enum.PAPEL,Enum.SPOCK);
    }

    @Override
    public Enum getTipo() {
        return Enum.LAGARTO;
    }
}
