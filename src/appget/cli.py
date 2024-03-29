import click

from .appget import AppGet

APPGET = 'APPGET'


@click.group()
@click.help_option('-h', '--help')
@click.version_option('v0.1.0', '-v', '--version', message='appget version v0.1.0  (剑意无痕，千山飞雪。)')
@click.pass_context
def cli(ctx):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj[APPGET] = AppGet()


@cli.command()
@click.pass_context
def show(ctx):
    ctx.obj[APPGET].show()


@cli.command()
@click.argument('appname')
@click.pass_context
def install(ctx, appname):
    ctx.obj[APPGET].install(appname)


@cli.command()
@click.argument('appname')
@click.pass_context
def uninstall(ctx, appname):
    ctx.obj[APPGET].uninstall(appname)


@cli.command()
@click.pass_context
def update(ctx):
    ctx.obj[APPGET].update()


@cli.command()
@click.argument('appname')
@click.pass_context
def upgrade(ctx, appname):
    ctx.obj[APPGET].upgrade(appname)


@cli.command(name='list')
@click.pass_context
def list_alias(ctx):
    ctx.obj[APPGET].list()


@cli.command()
@click.argument('appname')
@click.pass_context
def info(ctx, appname):
    ctx.obj[APPGET].info(appname)


@cli.command()
@click.argument('appname')
@click.pass_context
def search(ctx, appname):
    ctx.obj[APPGET].search(appname)
