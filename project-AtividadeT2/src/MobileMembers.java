// Fernando Henriques Neto
// RA:18.00931-0
public class MobileMembers extends Membro {

    public MobileMembers(String usuario, String email) {
        super(usuario, email);
        super.funcao = "MobileMembers";
    }

    @Override
    public void retornarMsg(){
        if(super.turnoRegular)
            System.out.println("Happy Coding!");
        else
            System.out.println("Happy_C0d1ng. Maskers");
    }
}
