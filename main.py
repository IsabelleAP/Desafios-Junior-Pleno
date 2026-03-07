import requests
import json
from pathlib import Path

def main():
    labels = ["analista", "dados", "python"]

    headers = {
        "User-Agent": "Mozilla/5.0"
        }

    url = "https://portal.api.gupy.io/api/job"

    Path("dados/vagas").mkdir(parents=True, exist_ok=True)

    for label in labels:
        params = {
            "name": label,
            "offset": 0,
            "limit": 400
            }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()["data"]

            with open(f"dados/vagas/{label}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"{label}: {len(data)} vagas salvas")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar {label}: {e}")

if __name__ == "__main__":
    main()
    