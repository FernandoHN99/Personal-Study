class Contato:

    def __init__(self, nome, dt_nascimento, sexo, telefone):
        self._nome = nome
        self._dt_nascimento = dt_nascimento
        self._sexo = sexo
        self._telefone = telefone

    def get_nome(self):
        return self._nome

    def get_dt_nascimento(self):
        return self._dt_nascimento

    def get_sexo(self):
        return self._sexo

    def get_telefone(self):
        return self._telefone

    def __str__(self):
        return f'Nome: {self._nome} - Data Nascimento: {self._dt_nascimento} - Sexo: {self._sexo} - Telefone: {self._telefone}'