from rest_framework import serializers
from .models import CoffeMachines, CoffePods

class CoffeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeMachines
        fields = ['id', "product_type", "water_line_compatible", "model_type"]


class CoffePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffePods
        fields = ['id', "product_type", "coffe_flavor", "pack_size"]