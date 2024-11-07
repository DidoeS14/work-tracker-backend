import configparser
"""
Simple config parser that reads the .ini file and returns variable with the uid of defined admin
"""

config = configparser.ConfigParser()
config.read('config.ini')

admin = config['admin']['uid']
