from rest_framework import routers

from kafka_service import views

router = routers.SimpleRouter()

router.register(r'data', views.KafkaServer)


urlpatterns = router.urls
