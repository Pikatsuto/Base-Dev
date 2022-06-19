from basedev import load_plugin, start_init, CommandGroup


class Demo(CommandGroup):
    """
    This is a command group for demonstration purposes.
    """

    @staticmethod
    def work(bar=False):
        """
        A work command that shows things are working!

        :param bar: False or True
            A bar argument that shows if set to True
            Default: False
        """
        print('work', '(bar)' * bar)


load_plugin(Demo)
start_init()
