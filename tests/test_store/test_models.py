import pytest

def test_coffe_machines_factory(coffe_machines_factory):
    assert coffe_machines_factory.id == '1'
    assert coffe_machines_factory.product_type == 'coffe_machine'
    assert coffe_machines_factory.water_line_compatible == 'yes'
    assert coffe_machines_factory.model_type == 'model_1'


def test_coffe_pods_factory(coffe_pods_factory):
    assert coffe_pods_factory.id == '2'
    assert coffe_pods_factory.product_type == 'coffe_pods'
    assert coffe_pods_factory.pack_size == '10'
    assert coffe_pods_factory.coffe_flavor == 'cappuccino'
    assert coffe_pods_factory.beans_type == 'Brazilian_Beans'


def test_coffe_beans_factory(coffe_beans_factory):
    assert coffe_beans_factory.name == 'Brazilian_Beans'
    assert coffe_beans_factory.capacity == 100
    assert coffe_beans_factory.quantity == 200
    assert coffe_beans_factory.consumption == 10
    assert coffe_beans_factory.depot_val == 200