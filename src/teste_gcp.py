from google.cloud import bigquery, storage
from dotenv import load_dotenv
import os

load_dotenv()

# testar BigQuery
bq_client = bigquery.Client()

query = "SELECT 1 as teste"
result = bq_client.query(query)

for row in result:
    print("Resultado:", row.teste)

# testar GCS
storage_client = storage.Client()

buckets = list(storage_client.list_buckets())
print("Buckets:", [b.name for b in buckets])