from k8s.data.yamler import load_instance_types
from k8s.model.resource import Resource
from pydantic import BaseModel
from typing import List


class Node(BaseModel):
    """
    A model representing K8S/EKS EC2 node.
    """

    name: str
    instance_type: str
    pods: List[Resource] = []  # TODO validate available resources
    capacity: Resource

    def add_daemon_set(self, daemon_set: dict):
        for daemon_resource in daemon_set.values():
            self.pods.append(Resource(**daemon_resource))

    def __str__(self):
        return f"Node(name={self.name}, instance_type={self.instance_type}, capacity={self.capacity})"

    def get_available_resources(self) -> Resource:
        available_resources = self.capacity
        available_resources.cpu -= 0.08  # Kubelet
        available_resources.memory -= 1.5  # Kubelet
        for pod in self.pods:
            available_resources -= pod
        return available_resources


def create_node(name: str, instance_type: str) -> Node:
    instance_types = load_instance_types()
    capacity = Resource(
        cpu=float(instance_types[instance_type]["cpu"]),
        memory=float(instance_types[instance_type]["memory"]),
        pods=instance_types[instance_type]["pods"],
    )
    return Node(name=name, instance_type=instance_type, capacity=capacity)
