import pytest
from pytest_factoryboy import register
from .factories import CoffeMachinesFactory, CoffePodsFactory, CoffeBeansFactory

register(CoffeMachinesFactory)
register(CoffePodsFactory)
register(CoffeBeansFactory)