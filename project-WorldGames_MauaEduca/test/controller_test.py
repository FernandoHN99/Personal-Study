from src.models.usuario import Usuario
from src.models.contato import Contato
from src.models.item import Item
from src.models.pedido import Pedido
from src.controllers.usuario_controller import Usuario_Controller
from src.controllers.item_controller import Item_Controller


# ctt = Contato(nome="Fernando", telefone="1112345678", dt_nascimento= "09/11/1989", sexo="Masculino")
# user = Usuario(email="fernando@gmail.com", senha= "Fernando123", contato= ctt)

# usuario_controller = Usuario_Controller()


# usuario_controller.adicionar_usuario(user)

# # usuario_controller.exibir_usuarios()

# usuario_busca = usuario_controller.buscar_usuario_email(user.get_email())
# usuario_busca2 = usuario_controller.buscar_usuario_email("teste")

# print(f'Usuario Busca: {usuario_busca}')
# print(f'Usuario Busca: {usuario_busca2}')

###########################################################

item_controller = Item_Controller()

# item_controller.exibir_itens()

# lista = item_controller.gerar_lista_item_nomes()

# print(lista)

item = item_controller.buscar_item_id(item_controller.get_itens_cadastrados()[10].get_id())

print(item)





