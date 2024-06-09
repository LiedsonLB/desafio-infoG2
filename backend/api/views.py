from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Survivor, Resource
from .serializers import SurvivorSerializer, ResourceSerializer
from django.db.models import Sum 

class SurvivorViewSet(viewsets.ModelViewSet):
    queryset = Survivor.objects.all()
    serializer_class = SurvivorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'])
    def update_location(self, request, pk=None):
        survivor = self.get_object()
        survivor.last_location_latitude = request.data.get('last_location_latitude', survivor.last_location_latitude)
        survivor.last_location_longitude = request.data.get('last_location_longitude', survivor.last_location_longitude)
        survivor.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def report_infection(self, request, pk=None):
        survivor = self.get_object()
        survivor.infected = True
        survivor.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def report(self, request):
        total_survivors = Survivor.objects.count()
        infected_survivors = Survivor.objects.filter(infected=True).count()
        non_infected_survivors = total_survivors - infected_survivors

        infected_percentage = (infected_survivors / total_survivors) * 100 if total_survivors > 0 else 0
        non_infected_percentage = (non_infected_survivors / total_survivors) * 100 if total_survivors > 0 else 0

        resource_totals = Resource.objects.values('resource_type').annotate(total_quantity=Sum('quantity'))  # Corrigido para usar Sum
        avg_resources_per_survivor = {res['resource_type']: res['total_quantity'] / total_survivors for res in resource_totals} if total_survivors > 0 else {}

        lost_points = sum(res['total_quantity'] * self.get_resource_point_value(res['resource_type']) for res in Resource.objects.filter(survivor__infected=True).values('resource_type').annotate(total_quantity=Sum('quantity')))  # Corrigido para usar Sum

        report_data = {
            'infected_percentage': infected_percentage,
            'non_infected_percentage': non_infected_percentage,
            'avg_resources_per_survivor': avg_resources_per_survivor,
            'lost_points': lost_points,
        }

        return Response(report_data)

    def get_resource_point_value(self, resource_type):
        resource_points = {
            'water': 4,
            'food': 3,
            'medication': 2,
            'ammunition': 1
        }
        return resource_points.get(resource_type, 0)
