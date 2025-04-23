import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from elasticsearch import Elasticsearch
from config import index_name, address

def search_laws(query, size=5):
    es = Elasticsearch(address)
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["texto^3", "titulo^2", "libro", "capitulo", "articulo"],
                "analyzer": "spanish"
            }
        }
    }
    res = es.search(index=index_name, body=body, size=size)
    hits = res['hits']['hits']
    print(f"\nНайдено {len(hits)} наиболее релевантных результатов по запросу: \"{query}\"\n")
    for i, hit in enumerate(hits, 1):
        source = hit['_source']
        print(f"{i}) Артикул: {source.get('articulo', '')}, Книга: {source.get('libro', '')}, Титул: {source.get('titulo', '')}")
        print(f"Score: {hit['_score']:.2f}")
        print(f"Текст: {source['texto'][:200]}...\n")

if __name__ == "__main__":
    user_query = input("Введите ваш запрос (на испанском): ")
    search_laws(user_query)