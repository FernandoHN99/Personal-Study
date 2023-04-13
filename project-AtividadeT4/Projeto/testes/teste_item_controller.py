from src.controllers.produto_controller import Produto_Controller
from src.models.produtos.item import Item

controller = Produto_Controller()

# lista_itens = controller.coletar_item_nome("GTA IV")
# for i, item in enumerate(lista_itens):
#     print(f'item {i}: {item}')

# lista_itens = controller.coletar_item_plataforma("PC")
# for i, item in enumerate(lista_itens):
#     print(f'item {i}: {item}')

item = Item(nome="Doom", descricao="MUITO LEGAL", valor=99.90, plataforma="PS4")
print(controller.adicionar_item(item))

# # lista_itens = controller.coletar_todos_itens()
# lista_itens = controller.coletar_todos_itens_nomes()
# for i, item in enumerate(lista_itens):
#     print(f'item {i}: {item}')

# print('##########################')
    
# lista_itens = controller.coletar_item_nome("900")
# lista_itens[0].set_nome('900')
# lista_itens[0].set_plataforma('PS4')
# lista_itens = controller.atualizar_item(lista_itens[0])

# controller.apagar_item(lista_itens[0].get_id())
# controller.apagar_todos_itens()

print('##########################')
lista_itens = controller.coletar_todos_itens()
for i, item in enumerate(lista_itens):
    print(f'item {i}: {item}')