import configparser
import os
import time
import datetime
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
    
    def elapsed_time_seconds(self):
        """Get the elapsed time in milliseconds since the last reset."""
        return (time.time() - self.start_time)

class Serializer:
    
    def __init__(self):
        self.new_serial = None
    
    def generate(self):
        # Obtain current datetime
        current_datetime = datetime.datetime.now()

        # Format datatime: YYYYMMDDHHMMSS
        serial = current_datetime.strftime("%Y%m%d%H%M%S")
        
        return serial


def create_text_file(path: str):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date in the desired format: year, month (two digits), day (two digits)
    file_name = current_datetime.strftime("%Y%m%d") + ".txt"

    # Combine the path with the file name
    complete_path = os.path.join(path, file_name)

    # Check if the file already exists
    if not os.path.exists(complete_path):
        # Create the file and write something in it (optional)
        with open(complete_path, 'w') as file:
            file.write("serial,general_result\n")
        print(f'File "{file_name}" has been created successfully in the folder "{path}".')
    else:
        print(f'File "{file_name}" already exists in the folder "{path}". No new file has been created.')

    # Return the complete path of the file, whether it was created or not
    return complete_path

def append_line_to_text_file(path: str, line: str):
    # Open the file in append mode and add the specified line
    with open(path, 'a') as file:
        file.write(line + '\n')