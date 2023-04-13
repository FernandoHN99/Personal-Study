from src.controllers.usuario_controller import Usuario_Controller
from src.models.usuario.usuario import Usuario
from src.models.contato.contato import Contato

controller = Usuario_Controller()

# contato_add = Contato(nome="Renato2", sexo="Masculino", telefone="1112344", data_nascimento="1999-11-09")
# usuario_add = Usuario(email="a", senha="1234", contato=contato_add)
# controller.adicionar_user(usuario_add)

# user = controller.buscar_user_email("a")
# print("user:", user)
# user.set_senha("a")
# print("Resultado:", controller.atualizar_user(user))
# user = controller.buscar_user_email("a")
# print("user:", user)

# lista_usuarios = controller.buscar_todos_users()
# for i, usuario in enumerate(lista_usuarios):
#     print(f'Usuario {i}: {usuario}')

# controller.deletar_todos_users()

lista_usuarios = controller.buscar_todos_users()
for i, usuario in enumerate(lista_usuarios):
    print(f'Usuario {i}: {usuario}')
