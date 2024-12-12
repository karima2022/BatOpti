

from customUser.serializers import CustomUserSerializer


from rest_framework import serializers
from .models import Ticket, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

