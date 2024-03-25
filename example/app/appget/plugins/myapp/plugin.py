from appget import App


class MyPlugin(App):
    name = 'my-plugin'
    version = '0.0.1'
    desc = 'MyPlugin desc'
    homepage = 'MyPlugin homepage'
    license = 'MyPlugin license'

    def __init__(self):
        super().__init__()

    def install(self):
        super().install()
        print(f'install: {self.__class__.__name__} ...')

    def uninstall(self):
        super().uninstall()
        print(f'uninstall: {self.__class__.__name__} ...')
