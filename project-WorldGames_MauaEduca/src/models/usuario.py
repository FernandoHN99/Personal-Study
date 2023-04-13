class Usuario:

    def __init__(self, email, senha, contato):
        self._email = email
        self._senha = senha
        self._contato = contato
    
    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha

    def get_contato(self):
        return self._contato
    
    def __str__(self):
        return f'Email: {self._email} - Senha: {self._senha} - Contato: {self._contato}'