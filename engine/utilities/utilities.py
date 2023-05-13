import configparser

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


class StationData:
    def __init__(self):
        self.station_name = str()
        self.cell_id = str()
        
class StationSettings:
    ''' Datastructure for StationSettings.ini'''
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.StationData = StationData()
        
        self.read_all()
    
    def get_value(self,section,key):
        """
        RETURN VALUES FROM SECTION KEY
        """
        Path = self.filepath
        Sections = [section]
        Keys = [key]
        parser = configparser.ConfigParser()
        try:
            parser.read(Path)
        except:
            print('Path not found')
        assert type(Sections) == type(Keys) == type([]), 'DataType must be list'
    
        values = []
        len_sections = len(Sections)
        len_options = len(Keys)

        if len_options == len_sections:
            pass
        elif len_sections > len_options:
            len_sections = len_options
            print('Data trimmed, different input lenght')
        elif len_sections < len_options:
            len_options = len_sections
            print('Data trimmed, different input lenght')
        
        try:
            for n in range(0,len_sections):
                actual_section = Sections[n]
                actual_key = Keys[n]
                value = parser.get(section = actual_section, option = actual_key ).replace('"',"")
                values.append(value)
        except configparser.NoSectionError as  e:
            print(e)
            print('Data or Path not found')
            value = values[-1].replace('"',"")
        return value #values
    
    def read_all(self):
        ''' Read all sections. '''
        self.read_station_data()

    def read_station_data(self):
        ''' Method to read StationData section. '''
        
        section = 'StationData'
        self.StationData.station_name = self.get_value(section, key='station_name')
        self.StationData.wait_inspection_time = self.get_value(section, key='cell_id')


class InstrumentSettings:
    pass

class TestSettings:
    pass