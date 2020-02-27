from django.urls import path

from kafka_service import views


urlpatterns = [
    path('data/', views.KafkaView.as_view(), name='kafka-view')
]
