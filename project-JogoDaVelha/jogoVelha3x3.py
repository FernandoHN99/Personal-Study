from jogoVelha import JogoVelha

class JogoVelha3x3(JogoVelha):
   def __init__(self, nivel_dificuldade):
      super().__init__(nivel_dificuldade, n_colunas=3, n_minimo_consecutivos=3)

   def pontuar(self, mat_str, jogador):
      tres_consecutivos = jogador * 3
      dois_consecutivos = jogador * 2

      if tres_consecutivos in mat_str: return 3
      if (
         f"{dois_consecutivos}" in mat_str or 
         f" {dois_consecutivos}" in mat_str or
         f"{jogador} {jogador}" in mat_str
         ):
         return 2
      else:
         return 0
   
   def funcao_avaliacao(self):
      pontuacaoComput = max(
         self.avaliar_linhas(self.simbolo_computador),
         self.avaliar_colunas(self.simbolo_computador),
         self.avaliar_diagonais_principais(self.simbolo_computador),
         self.avaliar_diagonais_secundarias(self.simbolo_computador),
      )
      pontuacaoHumano = max(
         self.avaliar_linhas(self.simbolo_humano),
         self.avaliar_colunas(self.simbolo_humano),
         self.avaliar_diagonais_principais(self.simbolo_humano),
         self.avaliar_diagonais_secundarias(self.simbolo_humano),
      )
      if pontuacaoHumano == 3: retorno = -1000
      elif pontuacaoComput == 3: retorno = 1000
      elif pontuacaoHumano == 2: retorno = -500
      elif pontuacaoComput == 2: retorno = 500
      else: retorno = 0
      # print(f'Pontuação Humano={pontuacaoHumano}, Pontuação Computador={pontuacaoComput}, Retorno={retorno}')
      return retorno