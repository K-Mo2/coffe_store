import pytest
from pytest_factoryboy import register
from .factories import CoffeMachinesFactory, CoffePodsFactory, CoffeBeansFactory

register(CoffeMachinesFactory)
register(CoffePodsFactory)
register(CoffeBeansFactory)

@pytest.fixture
def init_factories(db, coffe_machines_factory, coffe_pods_factory, coffe_beans_factory):
    machines = coffe_machines_factory.create()
    pods = coffe_pods_factory.create()
    beans = coffe_beans_factory.create()
    return machines, pods, beans