from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet, EquipmentViewSet

router = DefaultRouter()
router.register(r'building', BuildingViewSet, basename='building')
router.register('equipment', EquipmentViewSet, basename='equipment')

urlpatterns = [
    path('', include(router.urls)),
]
