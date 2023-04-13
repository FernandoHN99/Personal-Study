public class Usuario {
    private String nome;
    private String senha;
    private String email;
    private int transporteUtilizado;

    public Usuario(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.transporteUtilizado = 0;
    }

    public String toString() {
        return "Usuario [nome=" + this.nome + ", email=" + this.email + ", senha=" + this.senha + "]";
    }

    public boolean Alugar(Transporte meioTransporte){
        if(meioTransporte.getDisponibilidade()){
            meioTransporte.setDisponibilidade(false);
            this.transporteUtilizado = meioTransporte.getIdTransporte();
            return true;
        }else{
            return false;
        }
    }

    public boolean Trocar(Transporte meioTransporteAtual, Transporte meioTransporteFuturo){
        if(Alugar(meioTransporteFuturo)){
            meioTransporteAtual.setDisponibilidade(true);
            return true;
        }else{
            return false;
        }
    }

    public boolean Devolver(Transporte meioTransporte){
        if(this.transporteUtilizado == meioTransporte.getIdTransporte()){
            meioTransporte.setDisponibilidade(true);
            this.transporteUtilizado = 0;
            return true;
        }else{
            return false;
        }
    }
}
