import configparser
import os

config = configparser.ConfigParser()
try: config.read(os.environ["SHARP_CONFIG_FILE"])
except: config.read("/var/sharp/config.ini")
