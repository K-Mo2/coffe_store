from factory.django import DjangoModelFactory
from factory import Faker
from store.models import CoffeMachines, CoffePods, CoffeBeans


class CoffeMachinesFactory(DjangoModelFactory):
    class Meta:
        model = CoffeMachines
    
    
    id = '1'
    product_type = 'coffe_machine' 
    water_line_compatible = 'yes'
    model_type = 'model_1'


class CoffePodsFactory(DjangoModelFactory):
    class Meta:
        model = CoffePods
    
    
    id = '2'
    product_type = 'coffe_pods' 
    pack_size = '10'
    coffe_flavor = 'cappuccino'
    beans_type = 'Brazilian_Beans'


class CoffeBeansFactory(DjangoModelFactory):
    class Meta:
        model = CoffeBeans
    
    
    name = 'Brazilian_Beans'
    capacity = 100
    quantity = 200
    consumption = 10
    depot_val = 200