import os

from appget.utils import DEBUG

LOCAL_HOME = '/usr/local' if not DEBUG else os.environ['HOME'] + '/PycharmProjects/appget/example'
BIN_HOME = f'{LOCAL_HOME}/bin'
APP_HOME = f'{LOCAL_HOME}/app'
APPGET_HOME = f'{APP_HOME}/appget'
APPGET_BIN = f'{APPGET_HOME}/bin'
APPGET_LIB = f'{APPGET_HOME}/lib'
APPGET_PLUGINS = f'{APPGET_HOME}/plugins'
APPGET_CONFIG = f'{APPGET_HOME}/config/appget.toml'

SCRIPT_DIR = '.appget'

APPLIB_MODULE = 'applib'
MYAPP_MODULE = 'myapp'
APPGET_INSTALLED_MODULE = 'appget.installed'
