from random import randint, random
from dataclasses import dataclass

@dataclass
class Space:
    dim: int
    size: int

@dataclass
class Point:
    space: Space
    id: int
    cords: list[float] = None

    def __post_init__(self):
        if self.cords:
            if len(self.cords) == self.space.dim:
                raise ValueError("Invalid number of dimensions")
        else:
            self.cords = [randint(-self.space.size, self.space.size - 1) + random() for _ in range(self.space.dim)]

    def __str__(self):
        return f"{self.id}"
