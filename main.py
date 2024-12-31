from kafka.producer import produce_data
from flink.flink_job import start_flink_job
from elasticsearch.query_engine import query_recommendations

if __name__ == "__main__":
    produce_data()  
    start_flink_job()  
    query_recommendations()