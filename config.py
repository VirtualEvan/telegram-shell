###################
# Config settings #
###################

import configparser
import sys

# Load settings
Config = configparser.ConfigParser()
settings_file = "settings.ini"

if not Config.read(settings_file):
    print("ERROR: Could not find 'settings.ini'")
    sys.exit(1)

if not Config.get("bot", "token"):
    print("ERROR: Token configuration is empty")
    sys.exit(1)

if not Config.get("directory", "logs_directory"):
    print("ERROR: Logs configuration is empty")
    sys.exit(1)


def get_token():
    return Config.get("bot", "token")


def get_logs_dir():
    return Config.get("directory", "logs_directory")


def get_chat_id():
    return Config.get("admin", "chat_id") or False
