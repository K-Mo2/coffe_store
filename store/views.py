from ast import Raise
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CoffeMachinesSerializer, CoffePodsSerializer
from rest_framework import viewsets, mixins
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
    filterset_fields = '__all__'

class PodsViewSet(viewsets.ModelViewSet):
    queryset = CoffePods.objects.all().order_by('id')
    serializer_class  = CoffePodsSerializer
    filter_backends   = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields  = '__all__'

    def create(self, request, *args, **kwargs):
        try:
            pods_pack_size = int(self.request.query_params.get('pack_size'))
            coffe_pods = CoffePods.objects.all()
            
            
            if pods_pack_size == 1:
                coffe_pods.capacity -= 0.5
                coffe_pods.quantity -= 1
                coffe_pods.save()

            elif pods_pack_size == 2:
                coffe_pods.capacity -= 1.0
                coffe_pods.quantity -= 2
                coffe_pods.save()

            
            elif pods_pack_size == 3:
                coffe_pods.capacity -= 1.5
                coffe_pods.quantity -= 3
                coffe_pods.save()

            elif pods_pack_size == 4:
                coffe_pods.capacity -= 2.0
                coffe_pods.quantity -= 4
                coffe_pods.save()

        except Exception as e:
            raise e

        return self.create(self, request)

   