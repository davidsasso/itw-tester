# Native Imports
import os

# Custom Imports
from .utilities.datatypes import Parameters

from .sequences import CreateInstrumentsSequence
from .sequences import ConfigureInstrumentsSequence
from .sequences import ResistanceTestSequence
from .sequences import ReportResultsSequence

from .utilities.datatypes import StationSettings, InstrumentSettings, TestSettings
from .utilities.custom_exceptions import exceptions_handler_preuutloop, exceptions_handler_preuut, exceptions_handler_main, exceptions_handler_postuut, exceptions_handler_postuutloop

class AbstractProcessModel:
    
    def __init__(self):
        self.parameters = Parameters()
        print('HERE\n', self.parameters)
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
        self.parameters = Parameters()
        # Define settings paths
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.station_settings_path = os.path.join(self.current_dir, 'settings\\station_settings.ini')
        self.instrument_settings_path = os.path.join(self.current_dir, 'settings\\instrument_settings.ini')
        self.test_settings_path = os.path.join(self.current_dir, 'settings\\test_settings.ini')

    @exceptions_handler_preuutloop    
    def pre_uut_loop(self):
        
        print('\nLoad Parameters')
        self.parameters.StationSettings = StationSettings(filepath=self.station_settings_path)
        self.parameters.InstrumentSettings = InstrumentSettings(filepath=self.instrument_settings_path)
        self.parameters.TestSettings = TestSettings(filepath=self.test_settings_path)
        
        print('\nCreate Instruments')
        Sequence = CreateInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        print('\nConfigure Instruments')
        Sequence = ConfigureInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_preuut
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
    
    @exceptions_handler_main
    def main(self):
        print(f'\n3. Testing Resistance, unit: {self.serial}')
        #TODO main tests
        Sequence = ResistanceTestSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuut
    def post_uut(self):
        print(f'\n4. Report Results, unit: {self.serial}')
        #TODO report generator
        Sequence = ReportResultsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuutloop
    def post_uut_loop(self):
        print('\n5. Closing references and instruments')