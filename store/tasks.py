from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import CoffeBeans


@shared_task
def reset_coffe_beans():
    
    coffe_beans = CoffeBeans.objects.all()
    
    for obj in coffe_beans:
        obj.reset_coffe_beans()
    
    # coffe_beans.reset_coffe_beans(capacity, quantity)
    return f"Coffe Beans Stocks have been reset successfully!"

