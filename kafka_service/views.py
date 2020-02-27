import json

from django.conf import settings

from rest_framework import status, views
from rest_framework.response import Response

from kafka_service.client import KafkaClient


class KafkaServer(views.APIView):
    def post(self, request, *args, **kwargs):
        client = KafkaClient(settings.KAFKA_TOPIC)

        message = json.dumps(request.data)
        client.publish(message)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        client = KafkaClient(settings.KAFKA_TOPIC)
        messages = client.consume()

        return Response(messages, status=status.HTTP_200_OK)
