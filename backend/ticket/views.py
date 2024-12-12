from rest_framework import viewsets, serializers

from customUser.models import CustomUser
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):

    serializer_class = TicketSerializer
    def get_queryset(self):
        building_id = self.request.query_params.get('building')
        if building_id:
            return Ticket.objects.filter(building__id=building_id)
        return Ticket.objects.all()

    def perform_create(self, serializer):
        print(f"Utilisateur authentifié : {self.request.user}")
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        assigned_to_id = self.request.data.get('assigned_to')  # ID fourni dans la requête
        assigned_to = None
        if assigned_to_id:
            try:
                assigned_to = CustomUser.objects.get(id=assigned_to_id)  # Trouver l'utilisateur
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError({"assigned_to": "Utilisateur introuvable"})

        serializer.save(assigned_to=assigned_to)
