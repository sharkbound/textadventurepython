from textadventure import Room


class MainRoom(Room):
    def __init__(self):
        super().__init__('main')

    def ask_input(self):
        return input('MAIN: ')
