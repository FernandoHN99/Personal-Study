import java.util.ArrayList;
import java.util.*;

public class Formulario {
    //****************Variaveis statics necessarias administrar questoes ****************
    public static double totalPontosConservador, totalPontosConservadorModerado, totalPontosModerado, totalpontosModeradoAgressivo, totalPontosAgressivo;
    public static final List<String> listAlternativasSimbolos = Arrays.asList("a","b","c","d","e","f");
    private static ArrayList<MultiplaEscolha> listMultiplaEscolhas = new ArrayList<MultiplaEscolha>();
    
    public static void criarFormulario(){
        ArrayList<Alternativa> listAlternativas;
        //****************Limpar Tela****************
        Util.clearScreen();

        //****************Criação Questão 1****************
        listAlternativas = new ArrayList<Alternativa>();
        listAlternativas.add(new Alternativa("Curto-Prazo"));
        listAlternativas.add(new Alternativa("Médio-Prazo"));
        listAlternativas.add(new Alternativa("Longo-Prazo"));
        MultiplaEscolha questao1 = new MultiplaEscolha("Qual o prazo de seus investimentos", 1, listAlternativas);
        listMultiplaEscolhas.add(questao1);
        
        
        //****************Criação Questão 2****************
        listAlternativas = new ArrayList<Alternativa>();
        listAlternativas.add(new Alternativa("0%-20%"));
        listAlternativas.add(new Alternativa("20%-40%"));
        listAlternativas.add(new Alternativa("40%-60%"));
        listAlternativas.add(new Alternativa("60%-80%"));
        listAlternativas.add(new Alternativa("80%-100%"));
        MultiplaEscolha questao2 = new MultiplaEscolha("Qual a porcentagem do seu patrimônio está em bitcoin", 1, listAlternativas);
        listMultiplaEscolhas.add(questao2);
        
        //****************Criação Questão 3****************
        listAlternativas = new ArrayList<Alternativa>();
        listAlternativas.add(new Alternativa("0%-20%"));
        listAlternativas.add(new Alternativa("20%-40%"));
        listAlternativas.add(new Alternativa("40%-60%"));
        listAlternativas.add(new Alternativa("60%-80%"));
        listAlternativas.add(new Alternativa("80%-100%"));
        MultiplaEscolha questao3 = new MultiplaEscolha("Quanto de stable coins você possuí em seu portifólio", 1, listAlternativas);
        listMultiplaEscolhas.add(questao3);
        
        //****************Calculo da Pontuação dos Perfis****************
        calcularPontosParaCadaPerfil();
    }

    private static void calcularPontosParaCadaPerfil(){
        for (MultiplaEscolha questao : Formulario.listMultiplaEscolhas){
            totalPontosConservador += questao.getPontosConservador();
            totalPontosConservadorModerado += questao.getPontosConservadorModerado();
            totalPontosModerado += questao.getPontosModerado();
            totalpontosModeradoAgressivo += questao.getPontosModeradoAgressivo();
            totalPontosAgressivo += questao.getPontosAgressivo();
        }
    }

    public static void iniciarFormulario(Usuario user){
        for (MultiplaEscolha questao : Formulario.listMultiplaEscolhas) {
            if(user.getTotalPontosUsuario() >= questao.getPontuacaoMinima())
                user.responderPergunta(questao);
        }
        user.definirPerfilDoInvestidor();
    }

    public static String exibirPontosFormulario(){
        return "Formulario [totalPontosAgressivo=" + totalPontosAgressivo + ", totalPontosConservador="
                + totalPontosConservador + ", totalPontosConservadorModerado=" + totalPontosConservadorModerado
                + ", totalPontosModerado=" + totalPontosModerado + ", totalpontosModeradoAgressivo="
                + totalpontosModeradoAgressivo + "]\n";
    }

}
