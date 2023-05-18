import configparser
import socket

config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")

PRODUCER_KAFKA_CONF = {
    "bootstrap.servers": config.get("KAFKA", "bootstrap_servers"),
    "client.id": socket.gethostname(),
}
CONSUMER_KAFKA_CONF = {
    "bootstrap.servers": config.get("KAFKA", "bootstrap_servers"),
    "group.id": config.get("CONSUMER", "group_id"),
    "auto.offset.reset": config.get("CONSUMER", "auto_offset_reset"),
}
TIMEZONE = config.get("CONSUMER", "timezone")

TOPIC_NAME = config.get("KAFKA", "topic_name")
SLEEP_INTERVAL = config.getfloat("PRODUCER", "sleep_interval")

logging_config = {
    "filename": config.get("LOGGING", "file_name"),
    "level": config.get("LOGGING", "log_level"),
    "format": config.get("LOGGING", "format"),
}
