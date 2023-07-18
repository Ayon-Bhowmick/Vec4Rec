import models
import typing
import sqlite3

class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('v_store.db')
        self.cursor = self.conn.cursor()
        self.queries: dict[str, str] = self.read_queries()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def read_queries(self) -> dict[str, str]:
        queries = {}
        current_key = None
        current_query = []
        with open("queries.sql", "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("--"):
                    if current_key is not None:
                        queries[current_key] = "\n".join(current_query)
                        current_query = []
                    current_key = line[2:].strip()
                else:
                    current_query.append(line)
        if current_key is not None:
            queries[current_key] = "\n".join(current_query)
        return queries



def place_point(point: models.Point, space: models.Space):
    """
    places a point into storage
    """
    with open("store.txt", "a") as f:
        _write_point(f, point)

def _write_point(f: typing.TextIO, point: models.Point):
    """
    writes a point to a file
    """
    f.write(f"{point.id}: ")
