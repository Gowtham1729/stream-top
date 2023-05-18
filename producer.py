import time

import psutil
from confluent_kafka import Producer

from common.config import PRODUCER_KAFKA_CONF as KAFKA_CONF
from common.config import SLEEP_INTERVAL, TOPIC_NAME
from common.logger import configure_logger

logger = configure_logger(__name__)


def produce_top_events(kafka_producer):
    cpu_percent = str(psutil.cpu_percent(percpu=True))
    logger.info(f"CPU Percent: {cpu_percent}")
    kafka_producer.produce(TOPIC_NAME, key="cpu_percent", value=cpu_percent)

    # mem_percent = str(psutil.virtual_memory().percent)
    # print(f"Memory Percent: {mem_percent}")
    # kafka_producer.produce(TOPIC_NAME, key="mem_percent", value=mem_percent)


if __name__ == "__main__":
    producer = Producer(KAFKA_CONF)
    while True:
        time.sleep(SLEEP_INTERVAL)
        produce_top_events(producer)
