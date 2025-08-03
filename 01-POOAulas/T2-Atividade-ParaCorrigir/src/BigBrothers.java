// Fernando Henriques Neto
// RA:18.00931-0

public class BigBrothers extends Membro{


    public BigBrothers(String usuario, String email) {
        super(usuario, email);
        super.funcao = "BigBrothers";
    }

    @Override
    public void retornarMsg(){
        if(super.turnoRegular)
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        else
            System.out.println("...");
    }
    
}
