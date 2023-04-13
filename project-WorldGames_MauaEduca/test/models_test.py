from src.models.usuario import Usuario
from src.models.contato import Contato
from src.models.item import Item
from src.models.pedido import Pedido


ctt = Contato(nome="Fernando", telefone="1112345678", dt_nascimento= "09/11/1989", sexo="Masculino")
user = Usuario(email="fernando@gmail.com", senha= "Fernando123", contato= ctt)

print(f'Usuario: {user}')

item = Item(nome="GTAV V", plataforma="PS4", valor=200.00, imagem="path")
item2 = Item(nome="GTAV IV", plataforma="PS4", valor=200.00, imagem="path")

print(f'Item: {item}')
print(f'Item2: {item2}')

pdd1 = Pedido(email_user=user.get_email() , status="Carrinho", qtde=3, item_id=item.get_id(), numero_pdd="001")
pdd2 = Pedido(email_user=user.get_email() , status="Carrinho", qtde=3, item_id=item2.get_id(), numero_pdd="001")

print(f'Pedido 1: {pdd1}')
print(f'Pedido 2: {pdd2}')