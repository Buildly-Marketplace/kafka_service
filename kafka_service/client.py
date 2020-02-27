import json

from django.conf import settings
from kafka import KafkaConsumer, KafkaProducer


class KafkaClient:
    def __init__(self, topic: str):
        self.__topic = topic
        self.__server_url = f'{settings.KAFKA_HOST}:{settings.KAFKA_PORT}'

        self.__producer = KafkaProducer(
            bootstrap_servers=[self.__server_url],
            retries=5
        )

    def publish(self, payload: dict, key: bytes = None, headers: list = None):
        body = json.dumps(payload).encode('utf-8')

        self.__producer.send(
            topic=self.__topic,
            key=key if key else self.__topic.encode('utf-8'),
            value=body
        )

    def consume(self):
        return KafkaConsumer(
            self.__topic,
            bootstrap_servers=[self.__server_url],
            consumer_timeout_ms=1000
        )
