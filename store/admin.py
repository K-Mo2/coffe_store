from django.contrib import admin
from .models import CoffeMachines, CoffePods, CoffeBeans
class CoffeMachinesAdmin(admin.ModelAdmin):
    list_filter  = ('id','product_type', 'water_line_compatible', 'model_type')
    list_display = ('id','product_type', 'water_line_compatible', 'model_type')

admin.site.register(CoffeMachines, CoffeMachinesAdmin)

class CoffePodsAdmin(admin.ModelAdmin):
    list_filter  = ('id', 'product_type' , 'pack_size', 'coffe_flavor', 'beans_type')
    list_display = ('id', 'product_type' , 'pack_size', 'coffe_flavor', 'beans_type')

admin.site.register(CoffePods, CoffePodsAdmin)

class CoffeBeansAdmin(admin.ModelAdmin):
    list_filter  = ('name', 'capacity', 'quantity', 'consumption', 'depot_val')
    list_display = ('name', 'capacity', 'quantity', 'consumption', 'depot_val')

admin.site.register(CoffeBeans, CoffeBeansAdmin)
