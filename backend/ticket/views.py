from rest_framework import viewsets, serializers, permissions

from customUser.models import CustomUser
from .models import Ticket
from .serializers import TicketSerializer

class IsAuthenticatedAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user

class IsAuthenticatedAndHasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if view.action == 'assign' and request.user.profession_type != 'maintenance_manager':
            return False
        if view.action == 'update' and request.user.profession_type not in ['maintenance_manager', 'technician']:
            return False
        return True

class TicketViewSet(viewsets.ModelViewSet):

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedAndHasPermission]

    def get_queryset(self):
        building_id = self.request.query_params.get('building')
        if building_id:
            return Ticket.objects.filter(building__id=building_id)
        return Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_assign(self, serializer):
        if self.request.user.profession_type != 'maintenance_manager':
            raise serializers.ValidationError("Seul un manager peut assigner un ticket.")
        
        assigned_to_id = self.request.data.get('assigned_to')
        assigned_to = None
        if assigned_to_id:
            try:
                assigned_to = CustomUser.objects.get(id=assigned_to_id)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError({"assigned_to": "Utilisateur introuvable"})
    
        serializer.save(assigned_to=assigned_to)

        
    def perform_update(self, serializer):
        ticket = self.get_object()
        new_status = self.request.data.get('status')

        if new_status == 'open':
            print(self.request.user.profession_type)
            if self.request.user.profession_type != 'maintenance_manager':
                print(self.request.user.profession_type)
                raise serializers.ValidationError("Seul un manager peut ouvrir un ticket.")
            try:
                ticket.open_ticket()
            except Exception as e:
                raise serializers.ValidationError(f"Erreur lors de l'ouverture du ticket: {str(e)}")
        elif new_status == 'in_progress':
            try:
                ticket.start_progress()
            except Exception as e:
                raise serializers.ValidationError(f"Erreur lors du démarrage du ticket: {str(e)}")
        elif new_status == 'resolved':
            try:
                ticket.resolve_ticket()
            except Exception as e:
                raise serializers.ValidationError(f"Erreur lors de la résolution du ticket: {str(e)}")
        else:
            raise serializers.ValidationError("Statut non valide.")

        serializer.save(status=new_status)


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
