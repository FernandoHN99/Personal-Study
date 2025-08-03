public class App {
    public static void main(String[] args) throws Exception {
        System.clearProperty("cls");
        Cliente cliente1 = new Cliente("Murilo", 
                                       "456789", 
                                       "murilo.carvalho@maua.br", 
                                        new Conta(1234));
        cliente1.nome = "matheus";
        cliente1.setNome("matheus");
        System.out.println(cliente1.getNome());

        Cliente cliente2 = new Cliente("Fernando", 
        "49243017870", 
        "fernando.h.neto@maua.br", 
         new Conta());

        cliente1.visualizarCliente();
        cliente1.getConta().visualizarSaldo();
        cliente1.getConta().depositar(200);
        cliente1.getConta().visualizarSaldo(); 
        cliente1.visualizarCliente();

        cliente2.visualizarCliente();
        cliente2.getConta().visualizarSaldo();
        cliente2.getConta().depositar(200);
        cliente2.getConta().visualizarSaldo(); 
        cliente2.visualizarCliente();
        
    }
}