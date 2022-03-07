from rest_framework import serializers
from .models import CoffeMachines, CoffePods

class CoffeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachines
        fields = "__all__" 


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = "__all__" 


