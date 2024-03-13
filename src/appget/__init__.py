class Plugin:
    def __init__(self, name):
        self.name = name

    def execute(self):
        raise NotImplementedError('Subclass must implement this method')
