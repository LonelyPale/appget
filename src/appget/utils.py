import os

# develop
DEBUG = os.environ.get('APPGET_MODE', '').lower() == 'debug'
