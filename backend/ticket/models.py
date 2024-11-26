from django.db import models
from building.models import Building, Equipment
from customUser.models import CustomUser


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('open', 'Ouvert'), ('in_progress', 'En cours'), ('resolved', 'Résolu')])
    priority = models.CharField(max_length=10, choices=[('low', 'Faible'), ('medium', 'Moyenne'), ('high', 'Élevée')])
    ticket_type = models.CharField(max_length=20, choices=[('intervention', 'Intervention'), ('maintenance', 'Maintenance')])
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True) 
    building = models.ForeignKey(Building, on_delete=models.CASCADE)  
    equipment = models.ForeignKey(Equipment, related_name='tickets', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
