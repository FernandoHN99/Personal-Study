from src.models.item import Item

class Item_Controller:

    def __init__(self):
        self._itens_cadastrados = [
            Item(nome="Overwatch", plataforma="PC", valor=200.00, imagem="assets/item_1.jpg"),
            Item(nome="The Sims 4", plataforma="PC", valor=200.00, imagem="assets/item_2.jpg"),
            Item(nome="Grand Theft Auto V", plataforma="PC", valor=200.50, imagem="assets/item_3.jpg"),
            Item(nome="Minecraft", plataforma="PC", valor=200.00, imagem="assets/item_4.jpg"),
            Item(nome="Fortnite", plataforma="PC", valor=200.00, imagem="assets/item_5.jpg"),
            Item(nome="Spider-Man", plataforma="PS4", valor=200.00, imagem="assets/item_6.jpg"),
            Item(nome="Doom", plataforma="PS4", valor=200.00, imagem="assets/item_7.jpg"),
            Item(nome="Fifa 19", plataforma="PS4", valor=200.00, imagem="assets/item_8.jpg"),
            Item(nome="Cyberpunk 2077", plataforma="PS4", valor=200.00, imagem="assets/item_9.jpg"),
            Item(nome="Jump Force", plataforma="PS4", valor=200.00, imagem="assets/item_10.jpg"),
            Item(nome="Watch Dogs", plataforma="PS4", valor=200.00, imagem="assets/item_11.jpg"),
            Item(nome="Battlefiel 2042", plataforma="PS4", valor=200.00, imagem="assets/item_12.jpg"),
            Item(nome="Horizon Forbidden West", plataforma="PS4", valor=200.00, imagem="assets/item_13.jpg"),
            Item(nome="Grand Theft Auto  IV", plataforma="PS4", valor=200.00, imagem="assets/item_14.jpg"),
            Item(nome="Uncharted 4: A Thief's End", plataforma="PS4", valor=200.00, imagem="assets/item_15.jpg")
		]

    def buscar_item_id(self, id_):
        for item in self._itens_cadastrados:
            if item.get_id() == id_:
                return item
        return None

    def gerar_dict_item_nomes(self):
        dic = {}
        for item in self._itens_cadastrados:
            dic[item.get_id()] = item.get_nome()
        return dic

    def exibir_itens(self):
        for i, item in enumerate(self._itens_cadastrados):
            print(f"Item {i}: {item}")
    
    def get_itens_cadastrados(self):
        return self._itens_cadastrados
