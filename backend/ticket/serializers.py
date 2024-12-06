from rest_framework import serializers
from .models import Ticket

from rest_framework import serializers
from .models import Ticket, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'profession_type']

class TicketSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

