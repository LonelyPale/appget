from appget import App


class MyApp2(App):
    name = 'my-app2'
    desc = 'example'
    homepage = ''
    license = ''

    def __init__(self):
        super().__init__()

    def install(self):
        print(f'install: {self.__class__.__name__} ...')

    def uninstall(self):
        print(f'uninstall: {self.__class__.__name__} ...')
