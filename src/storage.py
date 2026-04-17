import json
from pathlib import Path
from typing import List, Dict, Any

def save_json(data: List[Dict[str,Any]],path:str) -> None:
    Path("../dados/vagas").mkdir(parents=True, exist_ok = True) # criar diretório

    with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            # ensure_ascii= False preserva os acentos