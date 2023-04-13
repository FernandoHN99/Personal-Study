public class Conta {
    private String idConta;
    private double saldo;
    private Usuario user;

    public Conta(){}

    public Conta(String idConta, Usuario user){
        this.idConta = idConta;
        this.user = user;
        saldo = 0;
    }

    public String visualizarSaldo(){
        return String.format("R$%.2f", saldo);
    }

    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }

    public double getSaldo() {
        return saldo;
    }

    public Usuario getUser() {
        return user;
    }

    public String getIdConta() {
        return idConta;
    }

}
