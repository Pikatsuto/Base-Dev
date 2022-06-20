from basedev import command, CommandGroup, __main__


class Demo(CommandGroup):
    """
    This is a command group for demonstration purposes.
    """
    def __init__(self):
        super().__init__()
        self.a = 5894958938

    @command('demo')
    def work(self):
        """
        A work command that shows things are working!
        """
        print(self.a)
        print('work')


if __name__ == '__main__':
    demo = Demo()
    __main__.main()
