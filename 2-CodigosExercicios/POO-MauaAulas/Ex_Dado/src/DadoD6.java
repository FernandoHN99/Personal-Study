import java.util.concurrent.ThreadLocalRandom;

public class DadoD6 extends Dado {

    public DadoD6(String id) {
        super(id);
    }

    @Override
    public void rodar() {
        this.face =  ThreadLocalRandom.current().nextInt(1, 21);
    }

    
}
