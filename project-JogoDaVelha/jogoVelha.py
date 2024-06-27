import numpy as np
import math
from util import Util
from abc import ABC, abstractmethod
from tqdm import tqdm

class JogoVelha(ABC):
   
   def __init__(self, nivel_dificuldade, n_colunas, n_minimo_consecutivos):
      self.n_minimo_consecutivos = n_minimo_consecutivos
      self.nivel_dificuldade = nivel_dificuldade
      self.mat = Util.criar_matriz_quadrada(n_colunas)
      self.dic_colunas = Util.criar_dicionario_letra_numero(n_colunas)
      self.simbolo_humano = "X"
      self.simbolo_computador = "O"

   @abstractmethod
   def pontuar(self, mat_str, jogador):
      pass

   @abstractmethod
   def funcao_avaliacao(self):
      pass

   @abstractmethod
   def verificar_vitoria(self, placar):
      pass

   def contar_jogadas_restantes(self):
      return sum(1 for linha in self.mat for elemento in linha if elemento == " ")

   def marcar_jogada_humano(self, linha, coluna):
      self.mat[linha][coluna] = self.simbolo_humano
   
   def marcar_jogada_computador(self, linha, coluna):
      self.mat[linha][coluna] = self.simbolo_computador
   
   def desfazer_jogada(self, linha, coluna):
      self.mat[linha][coluna] = " "
   
   def validar_jogada(self, linha, coluna):
      return (
         Util.validar_coluna(coluna, self.dic_colunas) 
         and Util.validar_linha(linha, self.mat) 
         and self.mat[linha][self.dic_colunas[coluna]] == " "
      )

   def imprimir_jogo(self):
      Util.limpar_tela()
      print(F"{self.simbolo_computador} = Computador    {self.simbolo_humano} = Humano\n")
      for i in range(1, len(self.mat)+1):
         print(f"{i:2}", end=" ")
         for j in range(1, len(self.mat[0])+1):
               jogada = self.mat[i-1][j-1]
               if(j != len(self.mat[0])):
                  print(f"  {jogada}  |", end="")
               else:
                  print(f"  {jogada}  ", end="")
         print(f"\n   {(' - - -' * len(self.mat[0]))[:-1]}")
      print("     ", end="")
      for letra in self.dic_colunas.keys():
         print(f"{letra:4}  ", end="")
      print("\n")

   def perguntar_jogada(self):
      eh_jogada_valida = False
      while not eh_jogada_valida:
         self.imprimir_jogo()
         try:
               coluna = input(f"Digite a coluna: ").upper()
               linha = int(input(f"Digite a linha: ")) - 1
               eh_jogada_valida = self.validar_jogada(linha, coluna)
               if not eh_jogada_valida:
                  input("\nJogada inválida! Enter para tentar novamente.")
         except ValueError:
               input("\nJogada inválida! Enter para tentar novamente.")
               continue
      return linha, self.dic_colunas[coluna]

   def avaliar_linhas(self, jogador):
      mat_linhas_str = Util.mat_to_mat_string_linhas(self.mat)
      return self.pontuar(mat_linhas_str, jogador)

   def avaliar_colunas(self, jogador):
      mat_transposta = np.transpose(self.mat)
      mat_colunas_str = Util.mat_to_mat_string_linhas(mat_transposta)
      return self.pontuar(mat_colunas_str, jogador)

   def avaliar_diagonais_principais(self, jogador):
      mat_diagonais_p_str = Util.mat_to_mat_string_diagonais(self.mat, self.n_minimo_consecutivos)
      return self.pontuar(mat_diagonais_p_str, jogador)

   def avaliar_diagonais_secundarias(self, jogador):
      mat_invertida = np.fliplr(self.mat)
      mat_diagonais_s_str = Util.mat_to_mat_string_diagonais(mat_invertida, self.n_minimo_consecutivos)
      return self.pontuar(mat_diagonais_s_str, jogador)

   def minimax(self, profundidade, eh_maximizador):
      placar = self.funcao_avaliacao()
      if self.verificar_vitoria(placar) or profundidade == 0 or self.contar_jogadas_restantes() == 0:
         return placar

      if eh_maximizador:
         max_avaliacao = -math.inf
         for i in range(len(self.mat)):
               for j in range(len(self.mat[i])):
                  if self.mat[i][j] == ' ':
                     self.marcar_jogada_computador(i, j)
                     avaliacao = self.minimax(profundidade - 1, False)
                     self.desfazer_jogada(i, j)
                     max_avaliacao = max(max_avaliacao, avaliacao)
         return max_avaliacao

      else:
         min_avaliacao = math.inf
         for i in range(len(self.mat)):
               for j in range(len(self.mat[i])):
                  if self.mat[i][j] == ' ':
                     self.marcar_jogada_humano(i, j)
                     avaliacao = self.minimax(profundidade - 1, True)
                     self.desfazer_jogada(i, j)
                     min_avaliacao = min(min_avaliacao, avaliacao)
         return min_avaliacao

   def melhor_movimento(self):
      melhor_avaliacao = -math.inf
      for i in tqdm(range(len(self.mat)), desc="Processando..."):
         for j in range(len(self.mat[i])):
               if self.mat[i][j] == ' ':
                  self.marcar_jogada_computador(i, j)
                  avaliacao = self.minimax(self.nivel_dificuldade, False)
                  self.desfazer_jogada(i, j)
                  if avaliacao > melhor_avaliacao:
                     melhor_avaliacao = avaliacao
                     linha, coluna = i, j
      return linha, coluna
   
   def jogada_aleatoria_computador(self):
      Util.limpar_tela()
      if(Util.retornar_random_true_false()):
         linha, coluna = Util.retornar_linha_coluna_central(self.mat)
         self.marcar_jogada_computador(linha, coluna)


   def jogar(self):
      self.jogada_aleatoria_computador()
      while True:
         linha, coluna = self.perguntar_jogada()
         self.marcar_jogada_humano(linha, coluna)
         self.imprimir_jogo()
         placar = self.funcao_avaliacao()
         if self.verificar_vitoria(placar):
               print("Você venceu!")
               break
         elif self.contar_jogadas_restantes() == 0:
               print("Empate!")
               break
         linha, coluna = self.melhor_movimento()
         self.marcar_jogada_computador(linha, coluna)
         placar = self.funcao_avaliacao()
         self.imprimir_jogo()
         if self.verificar_vitoria(placar):
               print("Computador venceu!")
               break
         elif self.contar_jogadas_restantes() == 0:
               print("Empate!")
               break