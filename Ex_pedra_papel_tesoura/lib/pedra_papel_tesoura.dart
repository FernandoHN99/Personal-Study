import 'dart:io';
import 'dart:math';

enum OPCAO { pedra, papel, tesoura, sair }

void exibe(String texto) {
  print(texto);
}

int pegaOpcaoUsuario() {
  return int.parse(stdin.readLineSync()!);
}

bool opcaoEhValida(int opcao) {
  return opcao >= 1 && opcao <= 4;
}

OPCAO mapeiaOpcao(int opcao) {
  return OPCAO.values[opcao - 1];
}

String decideResultado(OPCAO opcaoUsuario, OPCAO opcaoComputador) {
  if (opcaoUsuario == opcaoComputador) {
    return "Empate";
  } else if (
    (opcaoUsuario == OPCAO.papel && opcaoComputador == OPCAO.pedra) ||
    (opcaoUsuario == OPCAO.pedra && opcaoComputador == OPCAO.tesoura) ||
    (opcaoUsuario == OPCAO.tesoura && opcaoComputador == OPCAO.papel)
  ) {
    return "Você venceu";
  } else {
    return "Computador venceu";
  }
}


void jogo() {
  int opUsuario;

  do {
    // Exibir menu e capturar opção do usuário, validando
    do {
      exibe('1-Pedra\n2-Papel\n3-Tesoura\n4-Sair');
      opUsuario = pegaOpcaoUsuario();
    } while (!opcaoEhValida(opUsuario));

    // Se o usuário digitar 4, sair; senão, continuar o jogo
    if (opUsuario != 4) {
      // Sortear escolha do computador
      int opComputador = Random().nextInt(3) + 1;

      // Mapear opção do usuário e do computador para enum
      OPCAO opcaoUsuario = mapeiaOpcao(opUsuario);
      OPCAO opcaoComputador = mapeiaOpcao(opComputador);

      // Exibir as opções de cada um
      exibe(
          'Você (${opcaoUsuario.name}) vs (${opcaoComputador.name}) Computador');

      // Decidir quem venceu, ou se houve empate
      String vencedor = decideResultado(opcaoUsuario, opcaoComputador);

      // Exibir o resultado
      exibe(vencedor);
      exibe('***********************************');
      sleep(Duration(seconds: 3));
    }
  } while (opUsuario != 4);

  exibe('Até logo');
}
