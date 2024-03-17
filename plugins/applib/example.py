from appget import App


class MyExample(App):
    name = 'my-example'
    desc = 'example'
    homepage = ''
    license = ''

    def __init__(self):
        super().__init__()

    def install(self):
        print(f'install: {self.__class__.__name__} ...')

    def uninstall(self):
        print(f'uninstall: {self.__class__.__name__} ...')
