import os
import click

from . import log, cmd, app

BIN_HOME = '/usr/local/bin'
APP_HOME = '/usr/local/app'
APPGET_HOME = '/usr/local/app/appget'
APPGET_BIN = '/usr/local/app/appget/bin'
APPGET_LIB = '/usr/local/app/appget/lib'


class AppGet(app.App):
    def install(self):
        print('install')

    def uninstall(self):
        print('uninstall')

    def update(self):
        print('update')

    def upgrade(self):
        print('upgrade')

    def list(self):
        print('list')

    def info(self):
        print('info')

    def search(self):
        print('search')


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
@click.pass_context
def install(ctx, name, count):
    """
    asdf 测试 docs
    :param ctx:
    :param name:
    :param count:
    :return:
    """
    ctx.obj['APPGET'].install()
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
@click.pass_context
def uninstall(ctx):
    ctx.obj['APPGET'].uninstall()
    return
    cmd.run(f'rm -rf {APPGET_HOME}')


@cli.command()
@click.pass_context
def update(ctx):
    ctx.obj['APPGET'].update()
    return
    cmd.run(f'python3 -m pip install --upgrade --target={APPGET_LIB} appget')


@cli.command()
@click.pass_context
def upgrade(ctx):
    ctx.obj['APPGET'].upgrade()


@cli.command(name='list')
@click.pass_context
def list_alias(ctx):
    ctx.obj['APPGET'].list()


@cli.command()
@click.pass_context
def info(ctx):
    ctx.obj['APPGET'].info()


@cli.command()
@click.pass_context
def search(ctx):
    ctx.obj['APPGET'].search()
