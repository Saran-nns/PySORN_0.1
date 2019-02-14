from configparser import ConfigParser

parser = ConfigParser()

parser.read('configuration.ini')

nu = int(parser.get('Network_Config', 'Nu'))

print(type(nu))

