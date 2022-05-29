from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet, basename='sensors')
router.register(r'measurements', MeasurementViewSet, basename='measurements')
urlpatterns = router.urls

