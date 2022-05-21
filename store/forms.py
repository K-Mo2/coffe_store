from django import forms
from django.core.validators import MinValueValidator
from .models import model_type_list, machines_product_type_list, pods_product_type_list, flavors_list, pack_size_list, CoffeBeans, CoffePods, CoffeMachines

# class CoffeMachinesForm(forms.Form):
#     id = forms.CharField(max_length=50)
#     product_type = forms.ChoiceField(choices=machines_product_type_list)
#     water_line_compatible = forms.BooleanField(required=False)
#     model_type = forms.ChoiceField(choices=model_type_list)


class CoffeMachinesForm(forms.ModelForm):
    class Meta:
        model = CoffeMachines
        fields = "__all__"


# class CoffeBeansForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     capacity = forms.FloatField(validators=[MinValueValidator(0.0)])
#     quantity = forms.IntegerField(validators=[MinValueValidator(0)])
#     consumption = forms.IntegerField(validators=[MinValueValidator(0)])
#     depot_val = forms.IntegerField(validators=[MinValueValidator(0)])


class CoffeBeansForm(forms.ModelForm):
    class Meta:
        model = CoffeBeans
        fields = "__all__"




class CoffePodsForm(forms.ModelForm):
    class Meta:
        model = CoffePods
        fields = "__all__"



# class CoffePodsForm(forms.Form):
#     id = forms.CharField(max_length=50)
#     product_type = forms.ChoiceField(choices=pods_product_type_list)
#     coffe_flavor = forms.ChoiceField(choices=flavors_list)
#     pack_size = forms.ChoiceField(choices=pack_size_list)
#     beans_type = forms.ModelChoiceField(queryset=CoffeBeans.objects.all())