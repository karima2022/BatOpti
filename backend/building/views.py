from rest_framework import viewsets

from .models import Building, Equipment
from .serializers import BuildingSerializer, EquipmentSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit buildings.
    """
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit equipment, with optional filtering by building_id.
    """
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        building_id = self.request.query_params.get('building_id')
        if building_id:
            return Equipment.objects.filter(building_id=building_id)
        return Equipment.objects.all()


