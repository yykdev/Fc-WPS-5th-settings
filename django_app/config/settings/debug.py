"""
debug 에서 사용할 settings
runserver 시 명령은 : ./manage.py runserver --settings=config.settings.debug
"""

from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']