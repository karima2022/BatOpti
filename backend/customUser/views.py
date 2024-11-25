from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        profession_type = data.get('profession_type')

        if not username or not password:
            raise ValidationError("Le nom d'utilisateur et le mot de passe sont requis.")
        if profession_type not in dict(CustomUser.PROFESSION_TYPES):
            raise ValidationError("Le type de profession est invalide.")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            profession_type=profession_type
        )
        return Response({"message": "Inscription réussie !"}, status=status.HTTP_201_CREATED)



class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profession_type": user.profession_type,
        })