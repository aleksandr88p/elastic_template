import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from config import index_name, address

es = Elasticsearch(address)

try:
    es.indices.delete(index=index_name)
    print(f"Index '{index_name}' deleted successfully.")
except NotFoundError:
    print(f"Index '{index_name}' does not exist.")
except Exception as e:
    print(f"Error deleting index: {e}")