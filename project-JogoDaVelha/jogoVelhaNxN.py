from jogoVelha import JogoVelha
from abc import ABC, abstractmethod
from util import Util
class JogoVelhaNxN(JogoVelha, ABC):
   
   @abstractmethod
   def __init__(self, nivel_dificuldade, n_colunas, n_minimo_consecutivos):
      super().__init__(nivel_dificuldade, n_colunas, n_minimo_consecutivos)

   def pontuar(self, mat_str, jogador):
      quatro_consecutivos = jogador * 4
      tres_consecutivos = jogador * 3
      dois_consecutivos = jogador * 2
      pontuacao = 0

      if quatro_consecutivos in mat_str: pontuacao += 10000
      if f" {tres_consecutivos} " in mat_str: pontuacao += 750
      if (
         f"{tres_consecutivos} " in mat_str or 
         f" {tres_consecutivos}" in mat_str or
         f"{dois_consecutivos} {jogador}" in mat_str or 
         f"{jogador} {dois_consecutivos}" in mat_str
         ):
         pontuacao += 500
      if (
         f" {dois_consecutivos} " in mat_str or
         f"{dois_consecutivos}  " in mat_str or
         f"  {dois_consecutivos}" in mat_str
      ): 
         pontuacao += 100
      elif f"  {jogador}  " in mat_str: pontuacao+=50
      
      return pontuacao

   def funcao_avaliacao(self):
      pontuacaoComput = sum([
         self.avaliar_linhas(self.simbolo_computador),
         self.avaliar_colunas(self.simbolo_computador),
         self.avaliar_diagonais_principais(self.simbolo_computador),
         self.avaliar_diagonais_secundarias(self.simbolo_computador),
      ])
      pontuacaoHumano = sum([
         self.avaliar_linhas(self.simbolo_humano),
         self.avaliar_colunas(self.simbolo_humano),
         self.avaliar_diagonais_principais(self.simbolo_humano),
         self.avaliar_diagonais_secundarias(self.simbolo_humano),
      ])

      if(pontuacaoHumano) >= 10000:
         return -pontuacaoHumano
      elif(pontuacaoComput >= 10000):
         return pontuacaoComput
      else:
         retorno = pontuacaoComput - pontuacaoHumano

      # print(f'Pontuação Humano={pontuacaoHumano}, Pontuação Computador={pontuacaoComput}, Retorno={retorno}')
      return retorno
