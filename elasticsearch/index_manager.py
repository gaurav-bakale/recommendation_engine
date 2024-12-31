from elasticsearch.es_client import get_es_client

def create_index(index_name):
    es = get_es_client()
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body={"mappings": {"properties": {"user_id": {"type": "integer"}}}})
        print(f"Index {index_name} created.")