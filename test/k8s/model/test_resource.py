import pytest
from pydantic_core import ValidationError
from k8s.model.resource import Resource


def test_resource_addition():
    # Create two Resource instances
    resource1 = Resource(cpu=1.5, memory=2.0, pods=3)
    resource2 = Resource(cpu=2.5, memory=3.0, pods=2)

    # Add the two resources
    result = resource1 + resource2

    # Check if the result is a Resource instance
    assert isinstance(result, Resource)

    # Check if the values are correctly summed
    assert result.cpu == pytest.approx(4.0)
    assert result.memory == pytest.approx(5.0)
    assert result.pods == 5


def test_resource_addition_invalid():
    resource = Resource(cpu=1.0, memory=2.0, pods=1)

    # Try adding a non-Resource object
    with pytest.raises(TypeError):
        resource + 5


def test_resource_subtraction():
    # Create two Resource instances
    resource1 = Resource(cpu=4.0, memory=6.0, pods=5)
    resource2 = Resource(cpu=1.5, memory=2.0, pods=2)

    # Subtract the resources
    result = resource1 - resource2

    # Check if the result is a Resource instance
    assert isinstance(result, Resource)

    # Check if the values are correctly subtracted
    assert result.cpu == pytest.approx(2.5)
    assert result.memory == pytest.approx(4.0)
    assert result.pods == 3


def test_resource_subtraction_floor_at_zero():
    # Create two Resource instances
    resource1 = Resource(cpu=1.0, memory=2.0, pods=3)
    resource2 = Resource(cpu=2.0, memory=3.0, pods=4)

    # Subtract the resources
    with pytest.raises(ValidationError):
        _ = resource1 - resource2


def test_resource_subtraction_invalid():
    resource = Resource(cpu=1.0, memory=2.0, pods=1)

    # Try subtracting a non-Resource object
    with pytest.raises(TypeError):
        resource - 5
