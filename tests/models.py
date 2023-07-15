import unittest
from .. import Vec4Rec

class ModelTest(unittest.TestCase):
    """
    class to tests models defined in Vec4Rec\models.py
    """

    def test_space(self):
        """
        unit test for Space data class
        """
        dim = 200
        size = 100
        space = models.Space(dim, size)
        self.assertEqual(space.dim, dim)
        self.assertEqual(space.size, size)

    def test_point(self):
        """
        unit test for Point data class
        """
        id = 1
        dim = 200
        size = 100
        space = models.Space(dim, size)
        point = models.Point(id, space)
        self.assertEqual(point.id, id)
        self.assertEqual(len(point.cords), dim)
        self.assertEqual(point.space, space)
