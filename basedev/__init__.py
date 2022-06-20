"""The Base-dev package."""
from .__main__ import main

from .command import command, CommandGroup


__all__ = (
    'main',
    'command',
    'CommandGroup'
)
