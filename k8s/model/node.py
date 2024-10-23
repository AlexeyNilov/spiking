from k8s.data.yamler import load_instance_types
from k8s.model.resource import Resource
from pydantic import BaseModel
from typing import List


class Node(BaseModel):
    """
    A model representing K8S node.
    """

    name: str
    instance_type: str
    pods: List[Resource] = []
    capacity: Resource


def create_node(name: str, instance_type: str) -> Node:
    instance_types = load_instance_types()
    capacity = Resource(
        cpu=float(instance_types[instance_type]["cpu"]),
        memory=float(instance_types[instance_type]["memory"]),
        pods=instance_types[instance_type]["pods"],
    )
    return Node(name=name, instance_type=instance_type, capacity=capacity)
