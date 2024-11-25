from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet

router = DefaultRouter()
router.register(r'building', BuildingViewSet, basename='building')

urlpatterns = [
    path('', include(router.urls)),
]
