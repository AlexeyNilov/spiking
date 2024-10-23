import pytest
from k8s.model.node import create_node, Node
from k8s.model.resource import Resource
from unittest.mock import patch


@pytest.fixture
def mock_instance_types():
    return {
        "t2.micro": {"cpu": 1, "memory": 1, "pods": 5},
        "t2.small": {"cpu": 1, "memory": 2, "pods": 5},
    }


@patch("k8s.model.node.load_instance_types")
def test_create_node(mock_load_instance_types, mock_instance_types):
    mock_load_instance_types.return_value = mock_instance_types

    # Test creating a node with valid instance type
    node = create_node("test-node", "t2.micro")
    assert isinstance(node, Node)
    assert node.name == "test-node"
    assert node.instance_type == "t2.micro"
    assert node.capacity == Resource(cpu=1, memory=1, pods=5)
    assert node.pods == []


@patch("k8s.model.node.load_instance_types")
def test_create_node_invalid_instance_type(
    mock_load_instance_types, mock_instance_types
):
    mock_load_instance_types.return_value = mock_instance_types

    # Test creating a node with an invalid instance type
    with pytest.raises(KeyError):
        create_node("invalid-node", "invalid.instance")
