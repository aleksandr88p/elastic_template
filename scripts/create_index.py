import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
from config import index_name, address

es = Elasticsearch(address)

mapping = {
    "mappings": {
        "properties": {
            "book":     { "type": "keyword" },   # "codigo penal" или "codigo civil"
            "libro":    { "type": "keyword" },   # "Libro 1", "Libro 2", ...
            "titulo":   { "type": "keyword" },   # "Título I", ...
            "capitulo": { "type": "keyword" },   # "Capítulo 1", может быть пустым
            "articulo": { "type": "keyword" },   # "Artículo 15", может быть пустым
            "texto":    { "type": "text", "analyzer": "spanish" }  # основной текст
        }
    }
}

try:
    es.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' created successfully.")
except RequestError as e:
    if e.error == 'resource_already_exists_exception':
        print(f"Index '{index_name}' already exists.")
    else:
        print(f"Error: {e}")