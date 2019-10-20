from typing import TYPE_CHECKING, List, Dict

__all__ = [
    'Manager',
    'get_mgr',
    'has_mgr',
    'managers'
]

if TYPE_CHECKING:
    from .room import Room


class Manager:
    def __init__(self, id):
        self.id = id
        self.history: List['Room'] = []
        self.running = False
        self.rooms: Dict[str, 'Room'] = {}

    @property
    def current(self):
        return self.history[-1]

    @current.setter
    def current(self, room_id):
        self.history.append(self.rooms[room_id])

    def add_room(self, room: 'Room'):
        self.rooms[room.id] = room

    def run(self, initial: str):
        self.current = initial
        self.running = True
        while self.running:
            value = self.current.ask_input()


managers: Dict[str, Manager] = {}


def has_mgr(manager_id) -> bool:
    return manager_id in managers


def get_mgr(manager_id: str = 'main'):
    if not has_mgr(manager_id):
        managers[manager_id] = Manager(manager_id)
    return managers[manager_id]
