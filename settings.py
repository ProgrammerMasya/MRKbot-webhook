from private.parse_config import parse

config = dict()
config['token'], config['confirmation_token'], config['access_token'], \
config['db_password'],config['db_name'], config['db_host'], config['db_user'], \
config['app'] = parse('private', 'config.yaml')
