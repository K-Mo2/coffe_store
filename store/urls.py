from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='coffe-store'),
    path('coffe-machines', views.machines, name='coffe-machines'),
    path('coffe-pods', views.pods, name='coffe-pods'),
]