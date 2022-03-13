from ast import Raise
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CoffeMachinesSerializer, CoffePodsSerializer, CoffeBeansSerializer
from rest_framework import viewsets, mixins 
from rest_framework.response import Response
from .models import CoffeMachines, CoffePods, CoffeBeans
import django_filters.rest_framework
from rest_framework.decorators import action
import json
from django.views.decorators.csrf import csrf_exempt

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
    
    @csrf_exempt

    def create(self, request, *args, **kwargs):
        try:
            request_data = request.data
            
            if type(request_data) != dict:
                request_data = list(request_data.dict().values())[1:]
                coffe_pods_data = request_data
            else:
                coffe_pods_data = list(request_data.values())

                
            coffe_pods = CoffePods(id=coffe_pods_data[0], product_type=coffe_pods_data[1], coffe_flavor = coffe_pods_data[2], pack_size = coffe_pods_data[3])
            coffe_pods.save()
            pack_size = coffe_pods_data[3]

            try:   
                coffe_beans = coffe_pods.beans_type
                coffe_beans.reduce_coffe_beans(coffe_beans.name ,pack_size)
                coffe_beans_serialized = CoffeBeansSerializer(coffe_beans)
                return Response(coffe_beans_serialized.data)

            except:
                raise Exception("Coffe Beans Stock is Empty!")
            
        except Exception as e:
            raise e

   