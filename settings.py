from private.parse_config import parse

config = dict()
config['token'], config['confirmation_token'], config['access_token'], config['db_password'], config['app'] = parse('private', 'config.yaml')
