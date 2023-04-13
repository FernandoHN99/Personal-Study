from src.models.usuario import Usuario
from src.models.contato import Contato

class Usuario_Controller:

    def __init__(self):
        novo_contato = Contato(nome="a", dt_nascimento="1999-08-08", sexo="Masculino", telefone="12345")
        novo_usuario = Usuario(email="a", senha="a", contato=novo_contato)
        self.usuarios_cadastrados = [novo_usuario]
    
    def buscar_usuario_email(self, email):
        for user in self.usuarios_cadastrados:
            if user.get_email() == email:
                return user
        return None
    
    def adicionar_usuario(self, usuario):
        self.usuarios_cadastrados.append(usuario)

    def get_users_cadastrados(self):
        return self.usuarios_cadastrados
    
    def exibir_usuarios(self):
        for i, user in enumerate(self.usuarios_cadastrados):
            print(f'Usuario {i}: {user}')
