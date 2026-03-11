import requests

def fetch_jobs(label):
    headers = {"User-Agent": "Mozilla/5.0"} # requisição como se fosse um navegador
    url = "https://portal.api.gupy.io/api/job" # endereço da api

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

        return data

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar {label}: {e}")
        return []