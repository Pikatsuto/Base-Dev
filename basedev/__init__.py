"""The Base-dev package."""
from .__main__ import start_init


class CommandGroup:
    pass

load_plugin = lambda *_: ...

__all__ = (CommandGroup, start_init, load_plugin)
