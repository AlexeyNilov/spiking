from pydantic import BaseModel, PositiveFloat, PositiveInt


class Resource(BaseModel):
    """
    A model representing a resource requests.
    """

    cpu: PositiveFloat
    memory: PositiveFloat
    pods: PositiveInt

    def __add__(self, other):
        if not isinstance(other, Resource):
            return NotImplemented
        return Resource(
            cpu=self.cpu + other.cpu,
            memory=self.memory + other.memory,
            pods=self.pods + other.pods,
        )

    def __sub__(self, other):
        if not isinstance(other, Resource):
            return NotImplemented
        return Resource(
            cpu=max(0, self.cpu - other.cpu),
            memory=max(0, self.memory - other.memory),
            pods=max(0, self.pods - other.pods),
        )

    def __str__(self):
        return f"Resource(cpu={self.cpu}, memory={self.memory}, pods={self.pods})"
