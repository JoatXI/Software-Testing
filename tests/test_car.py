import pytest
from car import Car


def test_create_car():
    car1 = Car(20, 40)
    assert car1.current_speed == 20