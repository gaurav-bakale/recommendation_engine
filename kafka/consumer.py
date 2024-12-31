from kafka import KafkaConsumer
import json

def consume_data():
    consumer = KafkaConsumer('user_actions', bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    for message in consumer:
        print(f"Consumed: {message.value}")