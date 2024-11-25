from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    PROFESSION_TYPES = [
        ('maintenance_manager', 'Responsable Maintenance'),
        ('technician', 'Technicien'),
        ('service_provider', 'Prestataire'),
        ('user', 'Usager'),
    ]

    profession_type = models.CharField(max_length=20, choices=PROFESSION_TYPES, default='user')

    def __str__(self):
        return f"{self.username} ({self.get_profession_type_display()})"
