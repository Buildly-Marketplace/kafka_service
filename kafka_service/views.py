import json

from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from kafka_service.client import KafkaClient


class KafkaView(views.APIView):
    def post(self, request, *args, **kwargs):
        client = KafkaClient(settings.KAFKA_TOPIC)

        message = request.data
        client.publish(message)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        client = KafkaClient(settings.KAFKA_TOPIC)
        consumer = client.consume()
        response = list()
        for message in consumer:
            payload = message.value.decode('utf-8')
            json_payload = json.loads(payload)
            response.append(json_payload)

        return Response(response, status=status.HTTP_200_OK)
