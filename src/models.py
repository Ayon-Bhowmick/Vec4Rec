from random import randint, random
from dataclasses import dataclass
from typing import List

Vector = List[float]

@dataclass(eq=False, order=False, match_args=False)
class Space:
    dim: int
    size: int

@dataclass(eq=False, order=False, match_args=False)
class Point:
    id: int
    space: Space
    cords: Vector = None

    def __post_init__(self) -> None:
        if self.cords:
            if len(self.cords) == self.space.dim:
                raise ValueError("Invalid number of dimensions")
        else:
            self.cords = [randint(-self.space.size, self.space.size - 1) + random() for _ in range(self.space.dim)]

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return str(self.cords)

    def __eq__(self, __value: object) -> bool:
        return self.cords == __value.cords

x = Point(1, Space(1000000, 10))
print(len(repr(x)))
