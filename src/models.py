from random import randint, random
from dataclasses import dataclass

@dataclass(eq=False, order=False, match_args=False)
class Space:
    dim: int
    size: int

@dataclass(eq=False, order=False, match_args=False)
class Point:
    id: int
    space: Space
    cords: list[float] = None

    def __post_init__(self) -> None:
        if self.cords:
            if len(self.cords) == self.space.dim:
                raise ValueError("Invalid number of dimensions")
        else:
            self.cords = [randint(-self.space.size, self.space.size - 1) + random() for _ in range(self.space.dim)]

    def __str__(self) -> str:
        return str(self.id)

    def __eq__(self, __value: object) -> bool:
        return self.cords == __value.cords
