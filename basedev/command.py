from collections import defaultdict


class Command:

    def __init__(self, name, func):
        self.callback = func
        self.name = name

    def __call__(self, **kwargs):
        return self.callback(**kwargs)

    def __repr__(self):
        return f"Command({self.name} => {self.callback.__name__})"


def command(name):
    def inner(func):
        return Command(name, func)

    return inner


class CommandGroup:
    methods = defaultdict(list)

    def __init_subclass__(cls, **kwargs):
        for key in cls.__dict__.values():
            if isinstance(key, Command):
                cls.methods[key.name].append(key)

        print(f"{cls.__name__} => {cls.methods}")
