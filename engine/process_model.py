# Native Imports
import os

# Custom Imports
from .datatypes.parameters import Parameters

from .sequences import CreateInstrumentsSequence
from .sequences import ConfigureInstrumentsSequence
from .sequences import ResistanceTestSequence
from .sequences import ReportResultsSequence

from .utilities.utilities import StationSettings


class AbstractProcessModel:
    
    def __init__(self):
        pass
    
    def pre_uut_loop(self):
        print('1. Creating instruments')
    
    def pre_uut(self):
        self.serial = input('2. Scan Serial:')
        
        if self.serial == 'exit':
            continue_testing = False
        else:
            continue_testing = True
        return continue_testing
    
    def main(self):
        print(f'3. Testing {self.serial}')
    
    def post_uut(self):
        print(f'4. Report results for {self.serial}')
    
    def post_uut_loop(self):
        print('5. Closing instruments')

class ITWProcessModel(AbstractProcessModel):
    
    def __init__(self):
        # Define settings paths
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.station_settings_path = os.path.join(self.current_dir, 'settings\\station_settings.ini')
        self.instrument_settings_path = os.path.join(self.current_dir, 'settings\\instrument_settings.ini')
        self.test_settings_path = os.path.join(self.current_dir, 'settings\\test_settings.ini')
        
        self.parameters = Parameters()
        
    def pre_uut_loop(self):
        print('\n1. Create DMM and connection to database')
        #TODO read station settings
        self.station_settings = StationSettings(filepath=self.station_settings_path)
        #TODO read instrument settings
        #self.instrument_settings = ConfigManager(config_file_path=self.instrument_settings_path)
        #TODO read test settings
        #self.test_settings = ConfigManager(config_file_path=self.test_settings_path)
        Sequence1 = CreateInstrumentsSequence()
        Sequence2 = ConfigureInstrumentsSequence()
        
    def pre_uut(self, serial):
        #TODO wait for trigger to create serial
        #TODO serialize (create new serial)
        self.serial = serial
        #TODO serial validations
        
        if self.serial == 'exit':
            continue_testing = False
        else:
            continue_testing = True
        return continue_testing
    
    def main(self):
        print(f'\n3. Testing Resistance, unit: {self.serial}')
        #TODO main tests
        Sequence1 = ResistanceTestSequence()
    
    def post_uut(self):
        print(f'\n4. Report Results, unit: {self.serial}')
        #TODO report generator
        Sequence1 = ReportResultsSequence()
    
    def post_uut_loop(self):
        print('\n5. Closing references and instruments')