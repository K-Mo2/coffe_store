from tabnanny import verbose
from django.db import models

# Create your models here.

machines_product_type_list = (
    ("1","COFFEE_MACHINE_LARGE"),
    ("2","COFFEE_MACHINE_SMALL"),
    ("3","ESPRESSO_MACHINE"),
)

pods_product_type_list = (
    ("1","COFFEE_POD_LARGE"),
    ("2","COFFEE_POD_SMALL"),
    ("3","ESPRESSO_POD"),
)

flavors_list = (
    ("1","COFFEE_FLAVOR_VANILLA"),
    ("2","COFFEE_FLAVOR_CARAMEL"),
    ("3","COFFEE_FLAVOR_PSL"),
    ("4","COFFEE_FLAVOR_MOCHA"),
    ("5","COFFEE_FLAVOR_HAZELNUT"),
)

pack_size_list = (
    ("1","1 dozen (12)"),
    ("2","3 dozen (36)"),
    ("3","5 dozen (60)"),
    ("4","7 dozen (84)"),
)

model_type_list = (
    ("1","base model"),
    ("2","premium model"),
    ("3","deluxe model"),
)
class CoffeMachines(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    product_type = models.CharField(max_length=50,choices=machines_product_type_list)
    water_line_compatible = models.BooleanField()
    model_type = models.CharField(max_length=50, null=True, blank=True, choices=model_type_list)

    class Meta:
        verbose_name_plural = "Coffe Machines"

    def __str__(self):
        return f"{self.id.upper()} - {self.product_type}, {self.model_type} { self.water_line_compatible and ', water line compatible'}"



class CoffePods(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    product_type = models.CharField(max_length=50, choices=pods_product_type_list)
    coffe_flavor = models.CharField(max_length=50, choices=flavors_list)
    pack_size = models.CharField(max_length=50, choices=pack_size_list)

    class Meta:
        verbose_name_plural = "Coffe Pods"


    def __str__(self):
        return f"{self.id.upper()} - {self.product_type}, {self.pack_size}, {self.coffe_flavor}"