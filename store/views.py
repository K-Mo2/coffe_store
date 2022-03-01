from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CoffeMachinesSerializer, CoffePodsSerializer
from rest_framework import viewsets
from .models import CoffeMachines, CoffePods
import django_filters.rest_framework
# Create your views here.
def index(request):
    return HttpResponse("""
    <ol>
    <li> <a href='/coffe-store/coffe-machines'> Coffe Machines </a> </li>
    <li> <a href='/coffe-store/coffe-pods'> Coffe Pods </a> </li>
    </ol>
    """)

class MachinesViewSet(viewsets.ModelViewSet):
    queryset = CoffeMachines.objects.all().order_by('id')
    serializer_class = CoffeMachinesSerializer
    filter_backends  = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'product_type', 'water_line_compatible', 'model_type']

class PodsViewSet(viewsets.ModelViewSet):
    queryset = CoffePods.objects.all().order_by('id')
    serializer_class  = CoffePodsSerializer
    filter_backends   = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields  = ['id', 'product_type', 'coffe_flavor', 'pack_size']


