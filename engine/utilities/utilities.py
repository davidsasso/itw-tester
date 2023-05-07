import configparser


def read_config_file():
    config = configparser.ConfigParser()
    config.readfp(open(r'abc.txt'))
    path1 = config.get('My Section', 'path1')
    path2 = config.get('My Section', 'path2')
    path3 = config.get('My Section', 'path3')