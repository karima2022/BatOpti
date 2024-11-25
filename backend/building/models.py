from django.db import models

class Building(models.Model):
    BUILDING_TYPES = [
        ('school', 'École'),
        ('admin', 'Administration'),
        ('bank', 'Banque'),
        ('theater', 'Théâtre'),
        # Ajoute d'autres types de bâtiments ici
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    building_type = models.CharField(max_length=20, choices=BUILDING_TYPES)
    picture = models.ImageField(upload_to='building_photos/', blank=True, null=True, default='default.jpg')

    def __str__(self):
        return f"{self.name} ({self.get_building_type_display()})"
