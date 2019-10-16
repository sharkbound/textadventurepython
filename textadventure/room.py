__all__ = [
    'Room'
]


class Room:
    def __init__(self, id, left=None, right=None, up=None, down=None):
        self.id = id
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def ask_prompt(self):
        return input('CMD: ')
