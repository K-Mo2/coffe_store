from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router =  routers.DefaultRouter()
router.register(r'coffe-machines', views.MachinesViewSet)
router.register(r'coffe-pods', views.PodsViewSet)

urlpatterns = [
    path('', views.index, name='coffe-store'),
    path('', include(router.urls)),
]