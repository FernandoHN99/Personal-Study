from jogoVelha import JogoVelha
from abc import ABC, abstractmethod

class JogoVelhaNxN(JogoVelha, ABC):
   
   @abstractmethod
   def __init__(self, nivel_dificuldade, n_colunas, n_minimo_consecutivos):
      super().__init__(nivel_dificuldade, n_colunas, n_minimo_consecutivos)

   def pontuar(self, mat_str, jogador):
      quatro_consecutivos = jogador * 4
      tres_consecutivos = jogador * 3
      dois_consecutivos = jogador * 2

      if quatro_consecutivos in mat_str: return 4
      if f" {tres_consecutivos} " in mat_str: return 3.5
      if (
         f"{tres_consecutivos} " in mat_str or 
         f" {tres_consecutivos}" in mat_str or 
         f"{dois_consecutivos} {jogador}" in mat_str or 
         f"{jogador} {dois_consecutivos}" in mat_str
         ):
         return 3
      if (
         f" {dois_consecutivos} " in mat_str or
         f"{dois_consecutivos}  " in mat_str or
         f"  {dois_consecutivos}" in mat_str
      ): 
         return 2
      else: return 0

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
      
      if   pontuacaoHumano == 4: retorno = -1000
      elif pontuacaoComput == 4: retorno = 1000
      elif pontuacaoHumano == 3.5: retorno = -750
      elif pontuacaoComput == 3.5: retorno = 750
      elif pontuacaoHumano == 3: retorno = -500
      elif pontuacaoComput == 3: retorno = 500
      elif pontuacaoHumano == 2: retorno = -100
      elif pontuacaoComput == 2: retorno = 100
      else: retorno = 0
      # print(f'Pontuação Humano={pontuacaoHumano}, Pontuação Computador={pontuacaoComput}, Retorno={retorno}')
      return retorno