import itertools
from itertools import combinations



# --------------- Gerar Possibilidades --------------------------
def gerar_possibilidades(numero_fixo, numero_variavel, digitos_errados):
    digitos_validos = '0123456789'
    numero_variavel = str(numero_variavel)
    possibilidades = set()
    
    # Encontra todas as combinações de posições a serem alteradas
    posicoes = list(range(len(numero_variavel)))
    for posicoes_erradas in combinations(posicoes, digitos_errados):
        for substituicoes in itertools.product(digitos_validos, repeat=digitos_errados):
            novo_numero = list(numero_variavel)
            for i, posicao in enumerate(posicoes_erradas):
                novo_numero[posicao] = substituicoes[i]
            possibilidades.add(numero_fixo + "".join(novo_numero))

    print(f"Total de possibilidades: {len(possibilidades)}")
    return sorted(possibilidades)



# --------------- Cria Arquivo --------------------------
def salvar_contato_vcard(numeros, nome_arquivo, limite_por_card, nome_base): 
    with open(nome_arquivo, "w") as arquivo:
        for i in range(0, len(numeros), limite_por_card):
            nome_contato = f"{nome_base}{(i//limite_por_card):03d}"
            contato = f"""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//macOS 15.3//EN
N:;{nome_contato};;;
FN:{nome_contato}
"""
            for numero in numeros[i:i + limite_por_card]:
                contato += f"TEL;type=IPHONE;type=CELL;type=VOICE:+55 {numero}\n"
            contato += "END:VCARD\n"
            arquivo.write(contato)

    print(f"Total de cartões criados: {len(numeros) // limite_por_card + 1}")    



# --------------- VARS --------------------------
numero_fixo = "(35) 9"  # Prefixo fixo
numero_errado = "97607383"  # Número a ser corrigido
digitos_errados = 2  # Quantidade de dígitos que podem estar errados

nome_arquivo = "contato.vcf"  # Nome do arquivo de saída
limite_por_card = 50  # Quantidade de números por cartão
nome_base = "DEB"  # Nome base para os contatos

# --------------- EXEC --------------------------
possiveis_numeros = gerar_possibilidades(numero_fixo, numero_errado, digitos_errados)
salvar_contato_vcard(possiveis_numeros, nome_arquivo, limite_por_card, nome_base)

