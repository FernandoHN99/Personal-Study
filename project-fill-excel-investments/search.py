import requests

API_KEY_ALPHA = "J9OM0X9200KP47G2"

def buscar_ativos(nome_ativo: str):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": nome_ativo,
        "apikey": API_KEY_ALPHA
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        matches = data.get("bestMatches", [])
        if not matches:
            print("Nenhum ativo encontrado.")
            return

        print(f"\nResultados para '{nome_ativo}':\n")
        for match in matches:
            symbol = match.get("1. symbol", "N/A")
            name = match.get("2. name", "N/A")
            type = match.get("3. type", "N/A")
            region = match.get("4. region", "N/A")
            currency = match.get("8. currency", "N/A")

            print(f"📈 Nome: {name}")
            print(f"   Símbolo: {symbol}")
            print(f"   Tipo: {type}")
            print(f"   Região: {region}")
            print(f"   Moeda: {currency}\n")

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
    except ValueError:
        print("Erro ao processar resposta da API.")

if __name__ == "__main__":
    nome = input("Digite o nome do ativo para buscar: ").strip()
    buscar_ativos(nome)
