from elasticsearch import Elasticsearch

def get_es_client():
    return Elasticsearch(hosts=["http://localhost:9200"])