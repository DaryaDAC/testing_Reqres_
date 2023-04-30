from enum import Enum

class Enum_map(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda e: e.value, cls))
