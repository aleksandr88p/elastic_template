from elasticsearch import Elasticsearch
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import index_name, address
def connect_to_elasticsearch():

    
    try:
        print("Connecting to Elasticsearch...")
        # Attempt to connect to Elasticsearch
        es = Elasticsearch(address)
        print(es.info())
        
        print("Elasticsearch client created")
        if es.ping():
            print("Connected to Elasticsearch")
            cluster_info = es.info()
            print("Cluster Info:", cluster_info)
        else:
            print("Could not connect to Elasticsearch")
            print("Check if the Elasticsearch server is running and accessible.")
    except Exception as e:
        print("Error connecting to Elasticsearch:", str(e))
        print("Ensure that the Elasticsearch server is running and accessible.")
if __name__ == "__main__":  
    connect_to_elasticsearch()