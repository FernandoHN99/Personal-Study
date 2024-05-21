from jogoVelhaNxN import JogoVelhaNxN

class JogoVelha5x5(JogoVelhaNxN):
   
   def __init__(self, nivel_dificuldade):
      super().__init__(nivel_dificuldade, n_colunas=5, n_minimo_consecutivos=5)