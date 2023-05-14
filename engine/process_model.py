# Native Imports
import os

# Custom Imports
from .utilities.datatypes import Parameters

from .sequences import ReadConfigurationFiles
from .sequences import CreateInstrumentsSequence
from .sequences import InitializeInstrumentsSequence
from .sequences import ConfigureInstrumentsSequence
from .sequences import WaitTriggerSequence
from .sequences import SerializeSequence
from .sequences import ResistanceTestSequence
from .sequences import CreateTestResultsSequence
from .sequences import ReportResultsSequence
from .sequences import CloseInstrumentsSequence

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

    @exceptions_handler_preuutloop    
    def pre_uut_loop(self):
        
        Sequence = ReadConfigurationFiles(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        Sequence = CreateInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
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
        
        Sequence = ResistanceTestSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuut
    def post_uut(self):

        Sequence = ReportResultsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuutloop
    def post_uut_loop(self):
        print('\n5. Closing references and instruments')