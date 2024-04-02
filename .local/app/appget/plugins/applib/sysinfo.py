from appget import App


class SysInfo(App):
    name = 'sysinfo'
    version = '0.0.1-test'
    desc = 'System Info'
    homepage = 'SysInfo homepage'
    license = 'SysInfo license'

    def __init__(self):
        """子类的__init__方法是可选的，如果需要就必须显示的调用父类的__init__方法，否则父类的__init__方法不会被执行"""
        super().__init__()

    def install(self):
        super().install()
        print(f'install: {self.__class__.__name__} ...')


    def uninstall(self):
        super().uninstall()
        print(f'uninstall: {self.__class__.__name__} ...')
