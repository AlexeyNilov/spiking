from pydantic import BaseModel, PositiveFloat, PositiveInt


class Resource(BaseModel):
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
