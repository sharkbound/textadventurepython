from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .manager import Manager

__all__ = [
    'Room'
]


class Room:
    mgr: 'Manager'

    def __init__(self, id, **rooms: str):
        self.id = id
        self.rooms = rooms

    def ask_input(self):
        return input('CMD: ')

    @property
    def description(self):
        return ''

    @property
    def options(self):
        return ''

    def __getitem__(self, room_id):
        return self.rooms.get(room_id)
