import socket
import time

import psutil
from confluent_kafka import Producer

KAFKA_CONF = {
    'bootstrap.servers': "localhost:9092",
    'client.id': socket.gethostname()
}
TOPIC_NAME = "top-events"

producer = Producer(KAFKA_CONF)


def produce_top_events(kafka_producer):
    cpu_percent = str(psutil.cpu_percent(percpu=True))
    print(f"CPU Percent: {cpu_percent}")
    # cpu_percent = cpu_percent.to_bytes(2, byteorder="big")
    kafka_producer.produce(TOPIC_NAME, key="cpu_percent", value=cpu_percent)

    # mem_percent = str(psutil.virtual_memory().percent)
    # print(f"Memory Percent: {mem_percent}")
    # kafka_producer.produce(TOPIC_NAME, key="mem_percent", value=mem_percent)


if __name__ == "__main__":
    while True:
        time.sleep(1.5)
        produce_top_events(producer)
