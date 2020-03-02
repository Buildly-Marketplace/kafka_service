import json

from django.conf import settings
from kafka import KafkaConsumer, KafkaProducer


class KafkaClient:
    def __init__(self, topic: str):
        self.__topic = topic
        self.__servers = settings.KAFKA_HOSTS

        self.__producer = KafkaProducer(
            bootstrap_servers=self.__servers,
            retries=5
        )

    def publish(self, payload: dict, key: bytes = None, headers: list = None):
        body = json.dumps(payload).encode('utf-8')

        future = self.__producer.send(
            topic=self.__topic,
            key=key if key else self.__topic.encode('utf-8'),
            value=body
        )

        future.get(timeout=60)
        self.__producer.flush(timeout=60)

    def consume(self):
        consumer = KafkaConsumer(
            bootstrap_servers=self.__servers,
            consumer_timeout_ms=60
        )
        consumer.subscribe(topics=[self.__topic])
        consumer.topics()
        consumer.seek_to_beginning()
        return consumer
