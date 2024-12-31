from flink.flink_config import get_flink_env
from flink.transformations import process_stream

def start_flink_job():
    env = get_flink_env()
    stream = env.from_collection([
        {"user_id": 1, "action": "view", "item_id": 101},
        {"user_id": 2, "action": "like", "item_id": 102},
    ])
    process_stream(stream)
    env.execute("Flink Streaming Job")