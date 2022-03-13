from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import CoffeBeans


@shared_task
def reset_coffe_beans():
    brazilian_beans = CoffeBeans.objects.get(name="Brazilian_Beans")
    brazilian_beans.reset_coffe_beans(100, 200)

    arabic_beans = CoffeBeans.objects.get(name="Arabic_Beans")
    arabic_beans.reset_coffe_beans(150, 300)

    turkish_beans = CoffeBeans.objects.get(name="Turkish_Beans")
    turkish_beans.reset_coffe_beans(200, 400)
    
    # coffe_beans.reset_coffe_beans(capacity, quantity)
    return f"Coffe Beans Stocks have been reset successfully!"

