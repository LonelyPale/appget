from appget import App


class MyApp2(App):
    name = 'my-app2'
    version = '0.0.1'
    desc = 'MyApp2 desc'
    homepage = 'MyApp2 homepage'
    license = 'MyApp2 license'

    def __init__(self):
        super().__init__()

    def install(self):
        super().install()
        print(f'install: {self.__class__.__name__} ...')

    def uninstall(self):
        super().uninstall()
        print(f'uninstall: {self.__class__.__name__} ...')
