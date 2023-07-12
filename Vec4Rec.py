from random import randint, random

class Vec4Rec:
    def __init__(self, dim, size_of_space):
        self.dim = dim
        self.points = []
        self.size_of_space = size_of_space

    def place_point(self, cords = None):
        if cords:
            if len(cords) == self.dim:
                raise ValueError("Invalid number of dimensions")
        else:
            cords = [randint(-self.size_of_space, self.size_of_space - 1) + random() for _ in range(self.dim)]
