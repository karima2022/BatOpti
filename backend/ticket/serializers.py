from rest_framework import serializers
from .models import Ticket

from rest_framework import serializers
from .models import Ticket, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    assigned_to = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Ticket
        fields = '__all__'

