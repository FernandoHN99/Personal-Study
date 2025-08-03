// Fernando Henriques Neto
// RA:18.00931-0

public class HeavyLifters extends Membro {


    public HeavyLifters(String usuario, String email) {
        super(usuario, email);
        super.funcao = "HeavyLifters";
    }

    @Override
    public void retornarMsg(){
        if(super.turnoRegular)
            System.out.println("Podem contar conosco!");
        else
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
    }
    
}
