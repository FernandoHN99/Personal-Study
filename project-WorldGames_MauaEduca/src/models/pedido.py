import uuid
class Pedido:

    def __init__(self, email_user, status, qtde, item_id, numero_pdd):
        self._id = str(uuid.uuid4())
        self._email_user = email_user
        self._status = status
        self._qtde = qtde
        self._item_id = item_id
        self._numero_pdd = numero_pdd
    
    def get_id(self):
        return self._id

    def get_email_user(self):
        return self._email_user

    def get_status(self):
        return self._status

    def get_qtde(self):
        return self._qtde

    def get_item_id(self):
        return self._item_id

    def get_numero_pdd(self):
        return self._numero_pdd
    
    def __str__(self):
        return f'Id: {self._id} - Email Usuario: {self._email_user} - Status: {self._status} Quantidade: {self._qtde} - Item Id: {self._item_id} Numero Pedido: {self._numero_pdd}'