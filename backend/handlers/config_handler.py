import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

TOKEN = config["General"]["Token"]
DB_NAME = config["General"]["DB-Name"]

DEBUG = {"frontend": None, "backend": None, "db": None}
DEBUG["frontend"] = config["Debug"].getboolean("Frontend")
DEBUG["backend"] = config["Debug"].getboolean("Backend")
DEBUG["db"] = config["Debug"].getboolean("DB")
