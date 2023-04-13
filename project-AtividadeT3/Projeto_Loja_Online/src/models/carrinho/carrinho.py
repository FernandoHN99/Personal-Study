# Fernando Henriques Neto
# RA:18.00931-0
class Carrinho():

    def __init__(self):
        self._itens = []
    
    def adicionar_item(self, produto_novo):
        for item in self._itens:
            if(item["Produto"] == produto_novo):
                item["Quantidade"] += 1
                return
        
        self._itens.append({"Produto":produto_novo, "Quantidade": 1})
        return
    
    def remover_item(self, produto):
        for i, item in enumerate(self._itens):
            if(item["Produto"] == produto):
                if(item["Quantidade"]==1):
                    self._itens.pop(i)
                else:
                    item["Quantidade"] -= 1

    def qtde_total_itens(self):
        qtde_total = 0
        for item in self._itens:
            qtde_total += item["Quantidade"]

        return qtde_total
    
    def get_itens(self):
        return self._itens

    def calcular_valor_total(self):
        total = 0
        for item in self._itens:
            total += (item["Produto"].get_valor())*item["Quantidade"]
        return total
    
    def retornar_qtd_item(self, item_procurado):
        for item in self._itens:
            if(item["Produto"] == item_procurado):
                return item["Quantidade"]
        return 0


    def __str__(self):
        return f'Itens:{self._itens}'