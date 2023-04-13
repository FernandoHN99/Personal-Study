import java.util.concurrent.ThreadLocalRandom;

public class Transporte {
    protected Double custoPorHora;
    protected int idTransporte;
    protected boolean disponibilidade;

    protected int gerarID(){
        this.idTransporte = ThreadLocalRandom.current().nextInt(1000, 10000);
        return idTransporte;
    }

    public Double getCustoPorHora() {
        return custoPorHora;
    }

    public int getIdTransporte() {
        return idTransporte;
    }

    public void testar(){
        System.out.println("Transporte [id=" + this.idTransporte + ", custoPorHora=" + this.custoPorHora + "]");
    }

    public boolean getDisponibilidade() {
        return disponibilidade;
    }
    public boolean setDisponibilidade(boolean disponibilidade) {
        return this.disponibilidade = disponibilidade;
    }


}
