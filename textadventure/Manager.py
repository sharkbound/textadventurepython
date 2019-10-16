from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .room import Room


class Manager:
    def __init__(self):
        self.history: List['Room'] = []
        self.running = False

    def run(self, initial: str):
        pass
