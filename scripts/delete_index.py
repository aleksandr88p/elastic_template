from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from config import index_name

es = Elasticsearch("http://localhost:9200")

try:
    es.indices.delete(index=index_name)
    print(f"Index '{index_name}' deleted successfully.")
except NotFoundError:
    print(f"Index '{index_name}' does not exist.")
except Exception as e:
    print(f"Error deleting index: {e}")