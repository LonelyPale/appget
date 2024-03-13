from appget import Plugin


class MyPlugin(Plugin):
    def execute(self):
        print(f"\nExecuting plugin 123321: {self.name}\n")
        print('除了使用 之外click.group()，您还可以构建自己的自定义多命令。当您想要支持从插件延迟加载命令时，这非常有用。')
