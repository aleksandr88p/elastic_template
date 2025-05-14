from elasticsearch import Elasticsearch
import json
from config import bonsai_url, bonsai_access_key, bonsai_secret_token


# Подключение к Bonsai
es = Elasticsearch(
    "https://{}".format(bonsai_url),
    http_auth=(bonsai_access_key, bonsai_secret_token)
)

# 1. Создание индекса
es.indices.create(
    index="legal_documents",
    body={
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "book": { "type": "keyword" },
                "libro": { "type": "keyword" },
                "titulo": { "type": "text" },
                "capitulo": { "type": "text" },
                "articulo": { "type": "keyword" },
                "texto": { "type": "text" }
            }
        }
    }
)

# 2. Загрузка данных из файла
with open("bulk_data.ndjson", "r", encoding="utf-8") as f:
    bulk_data = f.read()

# Отправка данных через Bulk API
response = es.bulk(body=bulk_data)

# # 3. Проверка результата
# count_response = es.count(index="legal_documents")
# print(f"Загружено документов: {count_response['count']}")

# # 4. Пример поиска
# search_response = es.search(
#     index="legal_documents",
#     body={
#         "query": {
#             "match": {
#                 "texto": "jurídico"
#             }
#         },
#         "size": 3
#     }
# )

# # Вывод результатов поиска
# for hit in search_response["hits"]["hits"]:
#     source = hit["_source"]
#     print(f"Найдено: {source['book']} - Artículo {source['articulo']}")
#     print(f"Texto: {source['texto'][:100]}...")
#     print("-" * 50)