import requests
from typing import List, Dict, Any

def fetch_jobs(label: str) -> List[Dict[str, Any]]:
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://portal.api.gupy.io/api/job"

    offset = 0
    limit = 10
    all_jobs: List[Dict[str, Any]] = []
    total = None

    try:
        while total is None or offset < total:
            params = {
                "name": label,
                "offset": offset,
                "limit": limit
            }

            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            result = response.json()

            data = result["data"]
            total = result["pagination"]["total"]

            all_jobs.extend(data)

            offset += limit

        return all_jobs

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar {label}: {e}")
        return []