import os

import click

from . import log, cmd

BIN_HOME = '/usr/local/bin'
APP_HOME = '/usr/local/app'
APPGET_HOME = '/usr/local/app/appget'
APPGET_BIN = '/usr/local/app/appget/bin'
APPGET_LIB = '/usr/local/app/appget/lib'


@click.group()
@click.help_option('-h', '--help')
@click.version_option('v0.1.0', '-v', '--version', message='appget version v0.1.0  (剑意无痕，千山飞雪。)')
def cli():
    pass


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def install(name, count):
    """
    asdf 测试 docs
    :param name:
    :param count:
    :return:
    """
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
def uninstall():
    return
    cmd.run(f'rm -rf {APPGET_HOME}')


def update():
    return
    cmd.run(f'python3 -m pip install --upgrade --target={APPGET_LIB} appget')


def upgrade():
    pass


def list_():
    pass


def info():
    pass


def search():
    pass
