import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from elasticsearch import Elasticsearch, helpers
from config import index_name, address

NDJSON_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'all_laws.ndjson')

def generate_docs(ndjson_path):
    with open(ndjson_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                doc = json.loads(line)
                yield {
                    "_index": index_name,
                    "_source": doc
                }

def main():
    es = Elasticsearch(address)
    print(f"Загрузка данных из {NDJSON_PATH} в индекс '{index_name}' ...")
    try:
        result = helpers.bulk(es, generate_docs(NDJSON_PATH))
        print(f"Успешно загружено документов: {result[0]}")
    except Exception as e:
        print("Ошибка при загрузке данных:", str(e))

if __name__ == "__main__":
    main()

