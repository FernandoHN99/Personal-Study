from system import System
from util import Util

if __name__== '__main__':
    Util().clean_terminal()
    # list_food = ["Ovo De Galinha Inteiro Cozido", "Aveia em flocos finos Quaker", "Carne bovina patinho grelhado", "Arroz branco cozido", "Feijão carioca cozido", "Filé de frango grelhado", "Macarrão integral cozido", "Brócolis cozido", "Beterraba cozida", "Frango desfiado Vapza", "Doce de leite Aviação", "Molho de tomate Pomarola"]
    list_food = ["Azeite extra virgem Gallo"]
    
    
    sistema = System(browser='Brave', visible=False, overwrite=True, list_food_names=list_food)

    retorno_1 = sistema.run_system()
    if(retorno_1):
        print('Busca realizada com sucesso')
        retorno_2 = sistema.write_response_on_file()
        if(retorno_2):
            print('Dados salvos com sucesso')

