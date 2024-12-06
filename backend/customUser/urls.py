from django.urls import path, include
from .views import RegisterView, LoginView, UserListView
from .views import UserInfoView
from .views import UserListView
from rest_framework.routers import DefaultRouter
from .views import UserListView  # Importez votre ViewSet

# Créez un router
router = DefaultRouter()
router.register(r'users', UserListView, basename='user')
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
    path('', include(router.urls)),
]
