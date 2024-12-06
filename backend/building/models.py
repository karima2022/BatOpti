from django.db import models

class Building(models.Model):
    BUILDING_TYPES = [
        ('school', 'École'),
        ('admin', 'Administration'),
        ('bank', 'Banque'),
        ('theater', 'Théâtre'),
        
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    building_type = models.CharField(max_length=20, choices=BUILDING_TYPES)
    picture = models.ImageField(upload_to='building_photos/', blank=True, null=True, default='default.jpg')



class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('elevator', 'Ascenseur'),
        ('hvac', 'Climatisation'),
        ('fire_alarm', 'Alarme incendie'),
    ]

    name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPES)
    building = models.ForeignKey(Building, related_name='equipments', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.name} ({self.building.get_building_type_display()})"
