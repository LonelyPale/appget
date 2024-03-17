from appget import App


class MyApp1(App):
    name = 'my-app1'
    desc = 'example'
    homepage = ''
    license = ''

    def __init__(self):
        super().__init__()

    def install(self):
        print(f'install: {self.__class__.__name__} ... {self.__class__.__module__}.{self.__class__.__qualname__}')

    def uninstall(self):
        print(f'uninstall: {self.__class__.__name__} ...')
