import configparser
import os
import time
import random
import string

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


class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset the timer and start counting."""
        self.start_time = time.time()

    def elapsed_time(self):
        """Get the elapsed time in milliseconds since the last reset."""
        return (time.time() - self.start_time) * 1000  # Convert seconds to milliseconds

class Serializer:
    
    def __init__(self):
        self.new_serial = None
    
    def generate(self):
        serial = 'TEST_SERIAL_DUMMY'
        return serial