from api import fetch_jobs
from storage import save_json

def main():
    labels = ["analista", "dados", "python", "administração", 
              "engenharia","desenvolvedor", "data",
              "software", "ciência"]

    for label in labels:
        jobs = fetch_jobs(label)

        path = f"../dados/vagas{label}.json"

        save_json(jobs, path)

        print(f"{label}: {len(jobs)} vagas salvas")


if __name__ == "__main__":
    main()