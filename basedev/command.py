from collections import defaultdict


class CommandGroup:
    methods = defaultdict(list)

    def __init__(self):
        print(' Trying hook on', self.__class__.__name__)
        for k, v in self.methods.items():
            for cmd in v:
                if cmd.cls_name == self.__class__.__name__:
                    cmd.hook(self)

    def __init_subclass__(cls, **kwargs):
        for key in cls.__dict__.values():
            if isinstance(key, Command):
                cls.methods[key.name].append(key)

        print(f"{cls.__name__} => {cls.methods}")


class Command:

    def __init__(self, name, func):
        self.callback = func
        self.name = name

        self.cls_self = None
        self.cls_name = func.__qualname__.split('.')[0]

    def hook(self, cls_self):
        self.cls_self = cls_self

    def __call__(self, *args, **kwargs):
        return self.callback(self.cls_self, **kwargs)

    def __repr__(self):
        return f"Command({self.name} => {self.callback.__name__})"


def command(name):
    def inner(func):
        return Command(name, func)

    return inner

