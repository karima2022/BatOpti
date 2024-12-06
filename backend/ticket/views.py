from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    
    serializer_class = TicketSerializer
    def get_queryset(self):
        building_id = self.request.query_params.get('building')
        if building_id:
            return Ticket.objects.filter(building__id=building_id)
        return Ticket.objects.all()