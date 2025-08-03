// import javax.swing.JOptionPane;
// int a = Integer.parseInt(JOptionPane.showInputDialog("Digite idade"));
import java.util.*;


public class Sistema {
    private Map<String, Object> dataBase = new HashMap<String, Object>();
    private int numeroDeRegistros = 0;
    private Scanner input = new Scanner(System.in);
    
    public void run(){

        while(true){
            Util.clearScreen();
            interfaceGrafica();

            System.out.println("Digite a Opção Desejada - (S)air");
            String opcao = input.next();

            if(opcao.toUpperCase().compareTo("S") == 0){
                break;
            }

            Util.clearScreen();
            chamarOpcoes(opcao);
        }
        input.close();
    }

    private void interfaceGrafica(){
        String strMenu = ("\t\t MENU DE OPÇÕES \n\n" +
        "Opção 1 - Adicionar Conta\n" +
        "Opção 2 - Adicionar Saldo\n" +
        "Opção 3 - Retirar Dinheiro\n" +
        "Opção 4 - Gerar um QRCode\n" +
        "Opção 5 - Realizar Pagamento\n" +
        "Opção 6 - Visualizar Registros\n");
        System.out.println(strMenu);
    }

    private void chamarOpcoes(String opcao){
        switch(opcao) {
            case "1":
                dataBase = adicionarResgistros(dataBase);
                break;
            case "2":
                adicionarSaldo(dataBase);
                break;
            case "3":
                retirarDinheiro(dataBase);
                break;
            case "4":
                receptorQRCode(dataBase);
                break;
            case "5":
                realizarPagamento();
                break;
            case "6":
                visualizarResgistros(dataBase);
                break;
            default:
                break;
        }
    }

    private Map<String, Object> adicionarResgistros(Map<String, Object> mapDataBase){
        Conta acc;
        Usuario user;
        String nome, email, senha;

        System.out.println("Digite o nome do Usuário");
        nome = input.next();
        System.out.println("Digite o email de " + nome);
        email = input.next();  
        System.out.println("Digite a senha de " + nome);
        senha = input.next();  

        numeroDeRegistros += 1;
        user = new Usuario(nome, email, senha);
        acc = new Conta("#" + numeroDeRegistros, user);
        mapDataBase.put(acc.getIdConta(), acc);

        return mapDataBase;
    }

    private void visualizarResgistros(Map<String, Object> mapDataBase){
        String strValores = "";
        Conta acc = getContaById("#"+1);
        int i = 1;

        while(acc != null){
            strValores += ("\n\t\t USUÁRIO " + acc.getIdConta() + "\t\t\n" +  
            "Nome: " + acc.getUser().getNome() + "\n" +
            "Email: " + acc.getUser().getEmail() + "\n" +
            "Senha: " + acc.getUser().getSenha() + "\n" +
            "QRCodes: " + acc.getUser().getListQRCodes()+ "\n" +
            "Saldo: " + acc.visualizarSaldo() + "\n\n");

            i += 1;
            acc = getContaById("#"+i);
        }

        System.out.println(strValores);
        System.out.println("Digite algo para Voltar ao Menu");
        String wait = input.next();
    }


    private void adicionarSaldo(Map<String, Object> mapDataBase){
        System.out.println("Digite o ID da Conta sem #");
        String id = input.next();
        Conta acc = getContaById("#"+id);

        if(acc != null){
            System.out.println("Digite a quantia");
            double valor = input.nextDouble();

            boolean var = acc.depositar(valor);
        }
    }

    private void retirarDinheiro(Map<String, Object> mapDataBase){
        System.out.println("Digite o ID da Conta sem #");
        String id = input.next();
        Conta acc = getContaById("#"+id);

        if(acc != null){
            System.out.println("Digite a quantia");
            double valor = input.nextDouble();

            boolean var = acc.sacar(valor);
        }
    }

    private void receptorQRCode(Map<String, Object> mapDataBase){
        System.out.println("Digite o ID da Conta sem # que irá receber o pagamento");
        String id = ("#" + input.next());
        
        Conta acc = getContaById(id);
        if(acc != null){
            System.out.println("Digite a quantia (USUÁRIO " + acc.getIdConta()+ " - " + acc.getUser().getNome() + ")");
            double valor = input.nextDouble();

            if(valor >= 0)
                acc.getUser().setListQRCodes(gerarQRCode(id, acc.getUser().getNome(), valor)); 
            
        }
    }

    private void realizarPagamento(){
        System.out.println("Digite o ID da Conta do Pagador sem #");
        String idTransfer = "#" + input.next();
        Conta accTransfer = getContaById(idTransfer);
        System.out.println("Saldo: " + accTransfer.visualizarSaldo());
        
        if(accTransfer != null){
            System.out.println("Digite o ID da Conta do Receptor sem #");
            String idReceptor = ("#" + input.next());
            Conta accReceptor = getContaById(idReceptor);
            System.out.println("QRCodes: " + accReceptor.getUser().getListQRCodes());
            
            if(accReceptor != null){
                System.out.println("Digite o valor a ser Pago para "+ accReceptor.getUser().getNome());
                Double valor = input.nextDouble();
                String strQrcode = gerarQRCode(idReceptor, accReceptor.getUser().getNome(), valor);
                int index = accReceptor.getUser().checkQRCode(strQrcode);

                if(index != -1){
                    if(accTransfer.sacar(valor) && accReceptor.depositar(valor)){
                        accReceptor.getUser().getListQRCodes().remove(index);
                        System.out.println("Transferência Realizada com sucesso!\n");
                        System.out.println("Pressione qualquer tecla para sair!");
                        String wait = input.next();
                    }
                }
            }
        }
    }

    private Conta getContaById(String id){
        Conta acc = new Conta();
        if(Util.verifyContainsKey(dataBase,(id))){
            acc = (Conta) dataBase.get(id);
        }else{
            acc = null;
        }
        return acc;
    }

    public static String gerarQRCode(String idContaRecebedora, String nome, double valorTransacao ){
        return (idContaRecebedora + ";" + nome + ";" + String.valueOf(valorTransacao));
    }

        

        // Map<String, String> oi = new Map<String, String>();
        // Usuario user1 = new Usuario("Fernando", "fernandoHenriques@gmail.com", "fernando123");
        // Conta conta1 = new Conta("#1234", user1);
        // conta1.depositar(200);
        // System.out.println("Saldo Conta1: "+ conta1.visualizarSaldo());

        // Usuario user2 = new Usuario("Sandra", "sandraHenriques@gmail.com", "sandra123");
        // Conta conta2 = new Conta("#1234", user2);
        // conta2.depositar(100);
        // System.out.println("Saldo Conta2: "+ conta2.visualizarSaldo());

        
        // String transacao = Transacoes.gerarQRCode(conta2.getIdConta() , conta2.getUser().getNome(), 200);
        // System.out.println("QRCode Conta2: " + transacao);


}
