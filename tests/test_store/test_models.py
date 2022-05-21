import pytest
from store.models import CoffeMachines, CoffePods, CoffeBeans

def test_coffe_machines_factory(coffe_machines_factory):
    assert coffe_machines_factory.product_type == 'coffe_machine'

def test_coffe_pods_factory(coffe_pods_factory):
    assert coffe_pods_factory.product_type == 'coffe_pods'


def test_coffe_beans_factory(coffe_beans_factory):
    assert coffe_beans_factory.name == 'Brazilian_Beans'