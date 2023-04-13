import uuid
class Item:

    def __init__(self, nome, plataforma, valor, imagem):
        self._id = str(uuid.uuid4())
        self._nome = nome
        self._plataforma = plataforma
        self._valor = valor
        self._imagem = imagem
    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self._nome

    def get_plataforma(self):
        return self._plataforma

    def get_valor(self):
        return self._valor

    def get_imagem(self):
        return self._imagem
    
    def __str__(self):
        return f'Id: {self._id} - Nome: {self._nome} - Plataforma: {self._plataforma} Valor: {self._valor } Imagem: {self._imagem}'