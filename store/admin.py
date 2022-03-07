from django.contrib import admin
from .models import CoffeMachines, CoffePods, CoffeBeans
# Register your models here.
class CoffeMachinesAdmin(admin.ModelAdmin):
    list_filter = ('id','product_type', 'water_line_compatible', 'model_type')
    list_display = ('id','product_type', 'water_line_compatible', 'model_type')

admin.site.register(CoffeMachines, CoffeMachinesAdmin)

class CoffePodsAdmin(admin.ModelAdmin):
    list_filter = ('id', 'product_type' , 'pack_size', 'coffe_flavor')
    list_display = ('id', 'product_type' , 'pack_size', 'coffe_flavor')

admin.site.register(CoffePods, CoffePodsAdmin)

class CoffeBeansAdmin(admin.ModelAdmin):
    list_filter = ('capacity', 'quantity')
    list_display = ('capacity', 'quantity')

admin.site.register(CoffeBeans, CoffeBeansAdmin)
