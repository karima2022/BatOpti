from django.conf import settings
from django.db import models
from building.models import Building, Equipment
from customUser.models import CustomUser
from django_fsm import FSMField, transition


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = FSMField(default='created', choices=[('created', 'Créé'),('open', 'Ouvert'), ('in_progress', 'En cours'), ('resolved', 'Résolu')])
    priority = models.CharField(max_length=10, choices=[('low', 'Faible'), ('medium', 'Moyenne'), ('high', 'Élevée')])
    ticket_type = models.CharField(max_length=20, choices=[('intervention', 'Intervention'), ('maintenance', 'Maintenance')])
    assigned_to = models.ForeignKey(CustomUser,  related_name='assigned_to',on_delete=models.SET_NULL, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)  
    equipment = models.ForeignKey(Equipment, related_name='tickets', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='created_tickets', default=1
    )

    def is_maintenance_manager(self):
        return self.created_by.profession_type == 'maintenance_manager'

    @transition(field=status, source='created', target='open', conditions=[is_maintenance_manager])
    def open_ticket(self):
        pass

    @transition(field=status, source='open', target='in_progress')
    def start_progress(self):
        pass

    @transition(field=status, source='in_progress', target='resolved')
    def resolve_ticket(self):
        pass

    @transition(field=status, source='*', target='created', conditions=['is_maintenance_manager'])
    def reset_ticket(self):
        pass

  


    def __str__(self):
        return f"{self.title} - {self.status}"
