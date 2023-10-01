import configparser

# station_settings.ini configuration file data structures

class StationData:
    def __init__(self):
        self.station_name = str()
        self.cell_id = str()

class SettingsFile:
    
    def __init__(self, filepath):
        self.filepath = filepath
    
    def get_value(self,section,key):
        filepath = self.filepath
        Sections = [section]
        Keys = [key]
        parser = configparser.ConfigParser()
        try:
            parser.read(filepath)
        except:
            raise Exception('Invalid settings file.')
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
            print('Missing section error.')
            value = values[-1].replace('"',"")
        return value

    def get_bool_value(self,section,key):
        filepath = self.filepath
        Sections = [section]
        Keys = [key]
        parser = configparser.ConfigParser()
        try:
            parser.read(filepath)
        except:
            raise Exception('Invalid settings file.')
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
            # casting
            value = value.upper()
            if value == 'TRUE':
                value = True
            else:
                value = False
        except configparser.NoSectionError as  e:
            print(e)
            print('Missing section error.')
            value = values[-1].replace('"',"")
        return value
    
    def get_int_value(self,section,key):
        filepath = self.filepath
        Sections = [section]
        Keys = [key]
        parser = configparser.ConfigParser()
        try:
            parser.read(filepath)
        except:
            raise Exception('Invalid settings file.')
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
            # casting
            value = int(value)
        except configparser.NoSectionError as  e:
            print(e)
            print('Missing section error.')
            value = values[-1].replace('"',"")
        return value
    
    def get_float_value(self,section,key):
        filepath = self.filepath
        Sections = [section]
        Keys = [key]
        parser = configparser.ConfigParser()
        try:
            parser.read(filepath)
        except:
            raise Exception('Invalid settings file.')
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
            # casting
            value = float(value)
        except configparser.NoSectionError as  e:
            print(e)
            print('Missing section error.')
            value = values[-1].replace('"',"")
        return value
        
class StationSettings(SettingsFile):
    ''' Datastructure for station_settings.ini'''
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.StationData = StationData()
        
        self.read_all()

    
    def read_all(self):
        ''' Read all sections. '''
        self.read_station_data()

    def read_station_data(self):
        ''' Method to read StationData section. '''
        
        section = 'StationData'
        self.StationData.station_name = self.get_value(section, key='station_name')
        self.StationData.cell_id = self.get_value(section, key='cell_id')
    
    def __str__(self):
        print('\n-- station_settings --')
        StationData = f'[StationData]\nstation_name={self.StationData.station_name}\ncell_id={self.StationData.cell_id}\n'
        return_string = StationData
        return return_string


# instrument_settings.ini configuration file data structures

class DMM:
    def __init__(self):
        self.handle = None
        self.enabled = bool()
        self.instrument_type = str()
        self.address = str()

class InstrumentSettings(SettingsFile):
    ''' Datastructure for instrument_settings.ini'''
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.DMM = DMM()
        
        self.read_all()
    
    def read_all(self):
        ''' Read all sections. '''
        self.read_dmm()

    def read_dmm(self):
        ''' Method to read DMM instrumen section. '''
        
        section = 'DMM'
        self.DMM.enabled = self.get_bool_value(section, key='enabled')
        self.DMM.instrument_type = self.get_value(section, key='instrument_type')
        self.DMM.address = self.get_value(section, key='address')
    
    def __str__(self):
        print('\n-- instrument_settings --')
        DMM = f'[DMM]\nenabled={self.DMM.enabled}\ninstrument_type={self.DMM.instrument_type}\naddress={self.DMM.address}\n'
        return_string = DMM
        return return_string

# test_settings.ini configuration file data structures

class ResistanceTest:
    def __init__(self):
        self.test_active = bool()
        self.low_limit = float()
        self.high_limit = float()

class TestSettings(SettingsFile):
    ''' Datastructure for test_settings.ini'''
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.ResistanceTest = ResistanceTest()
        
        self.read_all()
    
    def read_all(self):
        ''' Read all sections. '''
        self.read_resistance_test()

    def read_resistance_test(self):
        ''' Method to read resistance test section. '''
        
        section = 'ResistanceTest'
        self.ResistanceTest.test_active = self.get_bool_value(section, key='test_active')
        self.ResistanceTest.low_limit = self.get_float_value(section, key='low_limit')
        self.ResistanceTest.high_limit = self.get_float_value(section, key='high_limit')
    
    def __str__(self):
        print('\n-- test_settings --')
        ResistanceTest = f'[ResistanceTest]\ntest_active={self.ResistanceTest.test_active}\nlow_limit={self.ResistanceTest.low_limit}\nhigh_limit={self.ResistanceTest.high_limit}\n'
        return_string = ResistanceTest
        return return_string


class Parameters:
    
    def __init__(self):
        self.StationSettings = SettingsFile(filepath='')
        self.InstrumentSettings = SettingsFile(filepath='')
        self.TestSettings = SettingsFile(filepath='')
        self.current_serial = None
    
    def __str__(self):
        return f"Station settings: {self.StationSettings}\nInstrument settings: {self.InstrumentSettings}\nTest settings: {self.TestSettings}"