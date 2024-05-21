from jogoVelhaNxN import JogoVelhaNxN

class JogoVelha7x7(JogoVelhaNxN):
   
   def __init__(self, nivel_dificuldade):
      super().__init__(nivel_dificuldade, n_colunas=7, n_minimo_consecutivos=7)