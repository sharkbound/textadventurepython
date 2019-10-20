from contextlib import contextmanager
from importlib import import_module
from inspect import isclass
from os import getcwd
from pathlib import Path

import sys
from typing import Union

__all__ = [
    'temp_syspath',
    'load'
]


def load(folder: Union[Path, str], manager_id: str = 'main'):
    from .room import Room
    from .manager import get_mgr

    if isinstance(folder, str):
        folder = Path(folder)

    if not folder.exists():
        return

    for file in folder.glob('*.py'):
        relative_import_path = (str(file.absolute().relative_to(Path(getcwd()).absolute()))
                                .replace('/', '.')
                                .replace('\\', '.')
                                .strip('. \\/')
                                .replace('.py', ''))
        mod = import_module(relative_import_path)
        for item in mod.__dict__.values():
            if isclass(item) and issubclass(item, Room) and item is not Room:
                Room.mgr = get_mgr(manager_id)
                Room.mgr.add_room(item())


@contextmanager
def temp_syspath(path: Path):
    string_path = str(path.absolute())
    if string_path not in sys.path:
        sys.path.append(string_path)
        yield
        sys.path.remove(string_path)
    else:
        yield
