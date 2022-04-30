from ast import Raise
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import CoffeMachinesSerializer, CoffePodsSerializer, CoffeBeansSerializer
from rest_framework import viewsets, mixins 
from rest_framework.response import Response
from .models import CoffeMachines, CoffePods, CoffeBeans
import django_filters.rest_framework
from rest_framework.decorators import action
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import CoffeMachinesForm, CoffePodsForm, CoffeBeansForm

# Create your views here.
def index(request):
    return render(request, 'store/store.html')

class MachinesViewSet(viewsets.ModelViewSet):
    queryset = CoffeMachines.objects.all().order_by('id')
    serializer_class = CoffeMachinesSerializer
    filter_backends  = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    def list(self, request, *args, **kwargs):
        form = CoffeMachinesForm()
        coffe_machines = CoffeMachines.objects.all().order_by('id')
        coffe_machines_json = CoffeMachinesSerializer(coffe_machines, many=True).data

        if request.method == 'POST':
            form = CoffeMachinesForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/coffe-store/coffe-machines/')

        return render(request, 'store/machines.html', {'coffe_machines':coffe_machines_json, 'form':form})


class PodsViewSet(viewsets.ModelViewSet):
    queryset = CoffePods.objects.all().order_by('id')
    serializer_class  = CoffePodsSerializer
    filter_backends   = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields  = '__all__'
    
    def list(self, request, *args, **kwargs):
        form = CoffePodsForm()
        coffe_pods = CoffePods.objects.all().order_by('id')
        coffe_pods_json = CoffePodsSerializer(coffe_pods, many=True).data
        
        if request.method == 'POST':
            form = CoffePodsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/coffe-store/coffe-pods/')

        return render(request, 'store/pods.html', {'coffe_pods':coffe_pods_json, 'form':form})

    
    @csrf_exempt

    def create(self, request, *args, **kwargs):
        try:
            request_data = request.data
            
            if type(request_data) != dict:
                request_data = list(request_data.dict().values())[1:]
                coffe_pods_data = request_data
            else:
                coffe_pods_data = list(request_data.values())

                
            coffe_pods = CoffePods(id=coffe_pods_data[0], product_type=coffe_pods_data[1], coffe_flavor = coffe_pods_data[2], pack_size = coffe_pods_data[3], beans_type = coffe_pods_data[4])
            coffe_pods.save()
            pack_size = coffe_pods_data[3]

            try:   
                coffe_beans = coffe_pods.beans_type
                coffe_beans.reduce_coffe_beans(pack_size)
                coffe_beans_serialized = CoffeBeansSerializer(coffe_beans)
                return Response(coffe_beans_serialized.data)

            except:
                raise Exception("Coffe Beans Stock is Empty!")
            
        except Exception as e:
            raise e


class BeansViewset(viewsets.ModelViewSet):
    queryset = CoffeBeans.objects.all().order_by('id')
    serializer_class = CoffeBeansSerializer
    filter_backends  = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    def list(self, request, *args, **kwargs):
        form = CoffeBeansForm()
        coffe_beans = CoffeBeans.objects.all().order_by('id')
        coffe_beans_json = CoffeBeansSerializer(coffe_beans, many=True).data

        if request.method == 'POST':
            form = CoffeBeansForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/coffe-store/coffe-beans/')

        return render(request, 'store/beans.html', {'coffe_beans':coffe_beans_json, 'form':form})