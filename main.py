import requests # fazer requisições HTTP para a API
import json # salvar os dados retornados pela API
from pathlib import Path # manipular pastas

def main():
    labels = ["analista", "dados", "python"] # palavras para procurar vagas / filtros de busca

    headers = {
        "User-Agent": "Mozilla/5.0" # requisição como se fosse um navegador
        }

    url = "https://portal.api.gupy.io/api/job" # endereço da api

    Path("dados/vagas").mkdir(parents=True, exist_ok = True) # criar diretório

    for label in labels:
        # parâmetros da requisição HTTP
        params = {
            "name": label,
            "offset": 0, # posição inicial da busca (página)
            "limit": 400 # número máximo de resultados
            }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            # timeout para esperar no máximo 10 segundos pela resposta
            response.raise_for_status()
            # gerar erro se o servidor responder algo como 404

            data = response.json()["data"]

            with open(f"dados/vagas/{label}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                # ensure_ascii= False preserva os acentos
            print(f"{label}: {len(data)} vagas salvas")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar {label}: {e}")

main()
    