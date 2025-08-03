// Fernando Henriques Neto
// RA:18.00931-0
public class ScriptGuys extends Membro {


    public ScriptGuys(String usuario, String email) {
        super(usuario, email);
        super.funcao = "ScriptGuys";
    }

    @Override
    public void retornarMsg(){
        if(super.turnoRegular)
            System.out.println("Prazer em ajudar novos amigos de código!");
        else
            System.out.println("QU3Ro_S3us_r3curs0s.py");
    }
    
}
