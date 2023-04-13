public class Sistema {

    public static void main(String[] args) throws Exception {

        //****************Criação do Formulário****************
        Formulario.criarFormulario();

        //****************Criação dos Usuarios****************
        Usuario user1 = new Usuario("Fernando");
        Usuario user2 = new Usuario("Vinincius");

        //****************Interação com Usuarios****************
        Formulario.iniciarFormulario(user1);
        Formulario.iniciarFormulario(user2);
        
        //****************Exibição de Perfil dos Usuários****************
        System.out.println(user1.toString());
        System.out.println(user2.toString());
        System.out.println(Formulario.exibirPontosFormulario());
         
    }


}