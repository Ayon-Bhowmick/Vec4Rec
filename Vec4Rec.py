from random import randint, random
from dataclasses import dataclass

@dataclass
class Space:
    dim: int
    size: int

@dataclass
class Point:
    id: int
    cords: list[float]

class Vec4Rec:
    def __init__(self, dim, size_of_space):
        self.dim = dim
        self.points = []
        self.size_of_space = size_of_space

    def place_point(self, id: int = None, cords: list[float] = None):
        if cords:
            if len(cords) == self.dim:
                raise ValueError("Invalid number of dimensions")
        else:
            cords = [randint(-self.size_of_space, self.size_of_space - 1) + random() for _ in range(self.dim)]


v = Vec4Rec(4, 100)
v.place_point()
