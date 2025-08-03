// Fernando Henriques Neto
// RA:18.00931-0
public abstract class Membro implements PostarMensagem{
    private String usuario, email;
    protected Boolean turnoRegular;
    protected String funcao;

    public Membro(String usuario, String email){
        this.usuario = usuario;
        this.email = email;
        this.turnoRegular = true;
    }

    public void mudarTurno(){
        if(this.turnoRegular)
            this.turnoRegular = false;
        else
            this.turnoRegular = true;
    } 

    
    public String getUsuario() {
        return usuario;
    }

    public String getEmail() {
        return email;
    }

    public Boolean getTurnoRegular() {
        return turnoRegular;
    }


    public String getFuncao() {
        return funcao;
    }

    @Override
    public String toString() {
        return "Membro [email=" + email + ", funcao=" + funcao + ", turnoRegular=" + turnoRegular + ", usuario="
                + usuario + "]";
    }



}