import models
import typing
import sqlite3
import os
import logging
import sys

class Storage:
    def __init__(self):
        self._conn = sqlite3.connect('v_store.db')
        self._cursor = self._conn.cursor()
        self._queries: dict[str, str] = self.read_queries()
        logging.basicConfig(stream=sys.stdout)
        logging.getLogger("[storage]").setLevel(logging.DEBUG)
        self.log = logging.getLogger("[storage]")

    def __del__(self):
        self._cursor.close()
        self._conn.close()

    def read_queries(self) -> dict[str, str]:
        queries = {}
        current_key = None
        current_query = []
        self.log.debug(os.path.dirname(os.path.realpath(__file__)))
        with open("./queries.sql", "r") as f:
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

    def make_table(self) -> int:
        try:
            self._cursor.execute(self._queries["make_vector_table"])
            return 0
        except Exception as e:
            raise e

    def add_point(self, point: models.Point) -> int:
        try:
            query = self._queries["add_point"].format(str(point), repr(point))
            self._cursor.execute(query)
            return 0
        except Exception as e:
            raise e

    def get_point(self, id) -> int | models.Vector:
        try:
            query = self._queries["get_point_by_id"].format(id)
            self._cursor.execute(query)
            vec: models.Vector =  self._cursor.fetchone()
            if vec:
                return exec(vec)
            else:
                raise ValueError("Point with that id does not exist")
        except Exception as e:
            raise e

    def delete_point(self, id) -> int:
        try:
            query = self._queries["delete_point_by_id"].format(id)
            self._cursor.execute(query)
            return 0
        except Exception as e:
            raise e

s = Storage()
print(s.read_queries())
