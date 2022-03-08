from rest_framework import serializers
from .models import CoffeMachines, CoffePods, CoffeBeans

class CoffeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachines
        fields = "__all__" 


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = "__all__" 


class CoffeBeansSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeBeans
        fields = "__all__" 


