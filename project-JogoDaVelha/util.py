import string
import os
import numpy as np
import math
import random

class Util:

   @staticmethod
   def limpar_tela():
      os.system('clear')

   @staticmethod
   def criar_matriz_quadrada(n_linhas):
      return np.full((n_linhas, n_linhas), ' ')

   @staticmethod
   def criar_dicionario_letra_numero(n_colunas):
      dicionario = {}
      lista_letras = [chr(i) for i in range(ord('A'), ord('A') + n_colunas)]
      for i, letra in enumerate(string.ascii_uppercase[:len(lista_letras)]):
         dicionario[letra] = i
      return dicionario

   @staticmethod
   def validar_coluna(coluna, dic_colunas):
      return coluna in dic_colunas.keys()

   @staticmethod
   def validar_linha(linha, mat):
      return 0 <= linha < len(mat)

   @staticmethod
   def mat_to_mat_string_linhas(mat):
      mat_linhas_str = ""
      for l in range(len(mat)):
         mat_linhas_str += ''.join(mat[l]) + "\n"
      return mat_linhas_str

   @staticmethod
   def mat_to_mat_string_diagonais(mat, n_minimo_consecutivos):
      mat_diagonais_str = ''.join(mat.diagonal()) + "\n"

      for i in range(1, len(mat)):
         diagonal_acima = mat.diagonal(offset=i)
         diagonal_abaixo = mat.diagonal(offset=-i)

         if len(diagonal_acima) >= n_minimo_consecutivos:
            mat_diagonais_str += ''.join(diagonal_acima) + "\n" + ''.join(diagonal_abaixo) + "\n"
      
      return mat_diagonais_str

   @staticmethod
   def retornar_random_true_false():
      return random.choice([True, False])
   
   @staticmethod
   def retornar_linha_coluna_central(mat):
      n_linhas, n_colunas = mat.shape

      linha_central = n_linhas // 2 if n_linhas % 2 != 0 else n_linhas // 2 - 1
      coluna_central = n_colunas // 2 if n_colunas % 2 != 0 else n_colunas // 2 - 1

      return linha_central, coluna_central