from kafka import KafkaProducer
import json
import time

def produce_data():
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    sample_data = [
        {"user_id": 1, "action": "view", "item_id": 101},
        {"user_id": 2, "action": "like", "item_id": 102},
    ]
    for data in sample_data:
        producer.send('user_actions', value=data)
        print(f"Produced: {data}")
        time.sleep(1)
    producer.close()