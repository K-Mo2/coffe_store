from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import CoffeBeans


@shared_task
def reset_coffe_beans(capacity, quantity):
    coffe_beans = CoffeBeans()
    coffe_beans.reset_coffe_beans(capacity, quantity)
    return f"Coffe Beans Stock has been reset successfully!\n Capacity: {coffe_beans.capacity} Quantity: {coffe_beans.quantity}."

