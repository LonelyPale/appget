import os
import sys
import inspect
import importlib

import toml
import click

from . import log, cmd
from .app import App

BIN_HOME = '/usr/local/bin'
# APP_HOME = '/usr/local/app'  # prod
APP_HOME = os.environ['HOME'] + '/PycharmProjects'  # dev
APPGET_HOME = f'{APP_HOME}/appget'
APPGET_BIN = f'{APPGET_HOME}/bin'
APPGET_LIB = f'{APPGET_HOME}/lib'
APPGET_PLUGINS = f'{APPGET_HOME}/plugins'
APPGET_CONFIG = f'{APPGET_HOME}/config/appget.toml'

APPLIB_MODULE = 'applib'
MYAPP_MODULE = 'myapp'


class AppGet(App):
    # metadata 元数据
    name = 'appget'  # 名称
    version = '0.1.5-dev3'  # 版本
    desc = 'A tool for installing custom software'  # 描述
    homepage = 'https://github.com/lonelypale/appget'  # 主页
    license = 'MIT'  # 许可证

    # 其他属性
    config = {}  # 配置文件字典
    apps = {}  # app安装脚本类

    def __init__(self):
        super().__init__()
        self.__load_config()
        self.__load_app_class()

    def __load_config(self):
        if os.path.exists(APPGET_CONFIG):
            self.config = toml.load(APPGET_CONFIG)
        else:
            log.debug(f'config file does not exist: {APPGET_CONFIG}')

    def __load_app_class(self):
        sys.path.append(APPGET_PLUGINS)
        for package in [APPLIB_MODULE, MYAPP_MODULE]:
            module = importlib.import_module(package)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, App) and obj != App:
                    if hasattr(obj, 'name'):
                        if obj.name not in self.apps:
                            self.apps[obj.name] = obj()  # 实例化App类
                        else:
                            class_path = f'{obj.__module__}.{obj.__qualname__}'
                            log.error(f'The app name already exists: name={obj.name} class_path={class_path}')
                    else:
                        class_path = f'{obj.__module__}.{obj.__qualname__}'
                        log.error(f'App class must set "name": class_path={class_path}')

    def install(self, appname):
        log.info("install")

    def uninstall(self, appname):
        log.info("uninstall")

    def update(self):
        log.info("update")

    def upgrade(self, appname):
        log.info("upgrade")

    def list(self):
        for app in self.apps.values():
            log.info(f'{app.name} --- {app.version} --- {app.desc}')

    def info(self, appname):
        # TODO: 应显示已安装app
        if appname in self.apps:
            app = self.apps[appname]
            log.info(f'Name: {app.name}')
            log.info(f'Version: {app.version}')
            log.info(f'Description: {app.desc}')
            log.info(f'Homepage: {app.homepage}')
            log.info(f'License: {app.license}')
        else:
            log.info("not found")

    def search(self, appname):
        if appname in self.apps:
            self.info(appname)
        else:
            log.info("not found")


@click.group()
@click.help_option('-h', '--help')
@click.version_option('v0.1.0', '-v', '--version', message='appget version v0.1.0  (剑意无痕，千山飞雪。)')
@click.pass_context
def cli(ctx):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj['APPGET'] = AppGet()


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.argument('appname')
@click.pass_context
def install(ctx, name, count, appname):
    """
    asdf 测试 docs
    """
    ctx.obj['APPGET'].install(appname)
    return
    try:
        statinfo = os.stat(APPGET_HOME)
    except FileNotFoundError:
        try:
            # xattr -d com.apple.provenance ./appget
            os.makedirs(APPGET_HOME)
            statinfo = os.stat(APPGET_HOME)
            log.info(f'created directory: {APPGET_HOME}')
        except PermissionError as err:
            raise Exception(err.__str__())
    except Exception:
        raise
    print(statinfo)


@cli.command()
@click.argument('appname')
@click.pass_context
def uninstall(ctx, appname):
    ctx.obj['APPGET'].uninstall(appname)
    return
    cmd.run(f'rm -rf {APPGET_HOME}')


@cli.command()
@click.pass_context
def update(ctx):
    ctx.obj['APPGET'].update()
    return
    cmd.run(f'python3 -m pip install --upgrade --target={APPGET_LIB} appget')


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
