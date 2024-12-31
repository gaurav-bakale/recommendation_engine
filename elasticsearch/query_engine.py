from elasticsearch.es_client import get_es_client

def query_recommendations():
    es = get_es_client()
    query = {
        "query": {
            "match_all": {}
        }
    }
    response = es.search(index="recommendations", body=query)
    print("Recommendations:", response["hits"]["hits"])