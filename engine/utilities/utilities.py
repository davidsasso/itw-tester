import configparser
import os

class ConfigManager:
    def __init__(self, config_file_path):
        self.path = config_file_path
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
        self.load_config()

    def load_config(self):
        for section_name in self.config.sections():
            section = self.config[section_name]
            for key in section:
                setattr(self, key, section[key])
