import sys
import os.path
import importlib
import inspect

import click
import toml

from . import log, cmd
from .app import App
from .constant import *


class AppGet(App):
    # metadata 元数据
    name = 'appget'  # 名称
    version = '0.1.5-dev3'  # 版本
    desc = 'A tool for installing custom software'  # 描述
    homepage = 'https://github.com/lonelypale/appget'  # 主页
    license = 'MIT'  # 许可证

    # 其他属性
    config = {}  # 配置文件字典
    apps_class = {}  # 全部的app安装脚本类
    installed_apps_class = {}  # 已安装的app脚本类

    def __init__(self):
        super().__init__()
        self.__load_config()
        self.__load_apps_class()
        self.__load_installed_apps_class()

    def __load_config(self):
        if os.path.exists(APPGET_CONFIG):
            self.config = toml.load(APPGET_CONFIG)
        else:
            log.debug(f'config file does not exist: {APPGET_CONFIG}')

    def __load_apps_class(self):
        """加载全部可以用于安装的app脚本类"""
        run_name = f'{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}' if DEBUG else None
        sys.path.append(APPGET_PLUGINS)
        for package in [APPLIB_MODULE, MYAPP_MODULE]:
            module = importlib.import_module(package)
            log.debug(f'{run_name}: module={module}')
            # log.debug(f'{run_name}: module_path={module.__path__[0]}')
            self.__cache_app_class_from_module(module, self.apps_class)

    def __load_installed_apps_class(self):
        """加载已安装的app脚本类"""
        run_name = f'{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}' if DEBUG else None

        for root, dirs, files in os.walk(APP_HOME):
            if not root.endswith(SCRIPT_DIR) or len(files) == 0:
                continue

            # 已安装的app脚本目录.appget
            script_file = files[0]
            script_path = os.path.join(root, script_file)  # app脚本必须是一个独立的文件，不允许拆分为多个文件放到子目录下，这样不方便管理
            script_name = script_file[:-3]

            # 直接导入源文件: 已安装的app脚本文件
            installed_module_name = f'{APPGET_INSTALLED_MODULE}.{script_name}'
            spec = importlib.util.spec_from_file_location(installed_module_name, script_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if installed_module_name not in sys.modules:
                sys.modules[installed_module_name] = module
                log.debug(f'{run_name}: module={module}')
            else:
                log.error(f'The app installed name already exists: name={installed_module_name} module={module}')

            # 缓存已安装的app脚本类
            self.__cache_app_class_from_module(module, self.installed_apps_class)

    def __cache_app_class_from_module(self, module, cache):
        """缓存app脚本类"""
        run_name = f'{self.__class__.__name__}.{inspect.currentframe().f_code.co_name}' if DEBUG else None
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, App) and obj != App:
                if hasattr(obj, 'name'):
                    if obj.name not in cache:
                        cache[obj.name] = obj
                        log.debug(f'{run_name}: class={obj}')
                    else:
                        class_path = f'{obj.__module__}.{obj.__qualname__}'
                        log.error(f'The app name already exists: name={obj.name} class_path={class_path}')
                else:
                    class_path = f'{obj.__module__}.{obj.__qualname__}'
                    log.error(f'App class must set "name": class_path={class_path}')

    def install(self, appname):
        app = self.get_installed_app(appname)
        if app:
            log.error('already installed')
            app.info()
        else:
            app = self.get_app(appname)
            if app:
                app.install()
            else:
                log.info("not found")

    def uninstall(self, appname):
        app = self.get_installed_app(appname)
        if app:
            app.uninstall()
        else:
            log.info("not installed")

    def update(self):
        log.info("update")
        # cmd.run(f'python3 -m pip install --upgrade --target={APPGET_LIB} appget')


    def upgrade(self, appname):
        log.info("upgrade")

    def list(self):
        """显示已安装的app列表"""
        for app in self.installed_apps_class.values():
            log.info(f'{app.name} - {app.version} - {app.desc}')

    def info(self, appname):
        """显示已安装的app"""
        app = self.get_installed_app(appname)
        if app:
            app.info()
        else:
            log.info("not found")

    def search(self, appname):
        """查找可安装的app"""
        app = self.get_app(appname)
        if app:
            app.search()
        else:
            log.info("not found")

    def get_app(self, appname):
        """获取app安装实例对象"""
        return self.apps_class[appname]() if appname in self.apps_class else None

    def get_installed_app(self, appname):
        """获取已安装的app实例对象"""
        return self.installed_apps_class[appname]() if appname in self.installed_apps_class else None


@click.group()
@click.help_option('-h', '--help')
@click.version_option('v0.1.0', '-v', '--version', message='appget version v0.1.0  (剑意无痕，千山飞雪。)')
@click.pass_context
def cli(ctx):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj['APPGET'] = AppGet()


@cli.command()
@click.argument('appname')
@click.pass_context
def install(ctx, name, count, appname):
    ctx.obj['APPGET'].install(appname)


@cli.command()
@click.argument('appname')
@click.pass_context
def uninstall(ctx, appname):
    ctx.obj['APPGET'].uninstall(appname)


@cli.command()
@click.pass_context
def update(ctx):
    ctx.obj['APPGET'].update()


@cli.command()
@click.argument('appname')
@click.pass_context
def upgrade(ctx, appname):
    ctx.obj['APPGET'].upgrade(appname)


@cli.command(name='list')
@click.pass_context
def list_alias(ctx):
    ctx.obj['APPGET'].list()


@cli.command()
@click.argument('appname')
@click.pass_context
def info(ctx, appname):
    ctx.obj['APPGET'].info(appname)


@cli.command()
@click.argument('appname')
@click.pass_context
def search(ctx, appname):
    ctx.obj['APPGET'].search(appname)
