from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

BOT_TOKEN = config.get('bot', 'BOT_TOKEN')
ADMINS = list(map(int, config.get('chat', 'ADMINS').split(',')))

SERVICES = [s.strip() for s in config.get('main', 'SERVICES').split(',')]
TIMEOUT = int(config.get('main', 'TIMEOUT'))
RETRY_LIM = int(config.get('main', 'RETRY_LIM'))
LOG_FILE = config.get('main', 'LOG_FILE')