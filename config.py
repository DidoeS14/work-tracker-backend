import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the .ini file
config.read('config.ini')

# Access values
admin = config['admin']['uid']
