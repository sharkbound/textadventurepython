from enum import auto, Enum

__all__ = [
    'CommandType'
]


class CommandType(Enum):
    QUIT = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    INSPECT = auto()
