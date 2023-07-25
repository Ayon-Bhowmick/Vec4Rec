import unittest
import  sys
sys.path.append('..')
# from src import models
from src import storage
import logging

class StorageTest(unittest.TestCase):
    """
    class to test database storage defined in src\storage.py
    """

    @classmethod
    def setUpClass(self) -> None:
        super().setUpClass()
        self.storage = storage.Storage()
        self.log = logging.getLogger("test")

    def test_read_queries(self):
        """
        unit test for read_queries method
        """
        queries = self.storage.read_queries()
        self.log.debug(queries)

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger("test").setLevel(logging.DEBUG)
    unittest.main()
