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

from .utilities.custom_exceptions import exceptions_handler_preuutloop
from .utilities.custom_exceptions import exceptions_handler_preuut
from .utilities.custom_exceptions import exceptions_handler_main
from .utilities.custom_exceptions import exceptions_handler_postuut
from .utilities.custom_exceptions import exceptions_handler_postuutloop

class AbstractProcessModel:
    
    def __init__(self):
        self.parameters = Parameters()
        
    def pre_uut_loop(self):
        #print('1. Creating instruments')
        print(f'Running: -- [PreUUTLoop] --')
    
    def pre_uut(self):
        #self.serial = input('2. Scan Serial:')
        print(f'Running: -- [PreUUT] --')
        
        if self.serial == 'exit':
            continue_testing = False
        else:
            continue_testing = True
        return continue_testing
    
    def main(self):
        #print(f'3. Testing {self.serial}')
        print(f'Running: -- [Main] --')
    
    def post_uut(self):
        #print(f'4. Report results for {self.serial}')
        print(f'Running: -- [PostUUT] --')
    
    def post_uut_loop(self):
        #print('5. Closing instruments')
        print(f'Running: -- [PostUUTLoop] --')

class ITWProcessModel(AbstractProcessModel):
    
    def __init__(self):
        self.parameters = Parameters()

    @exceptions_handler_preuutloop    
    def pre_uut_loop(self):
        super().pre_uut_loop()
        
        Sequence = ReadConfigurationFiles(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        Sequence = CreateInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
        Sequence = InitializeInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        Sequence = ConfigureInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_preuut
    def pre_uut(self, serial):
        super().pre_uut()
        #TODO wait for trigger to create serial
        Sequence = WaitTriggerSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        #TODO serialize (create new serial)
        Sequence = SerializeSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        self.serial = serial
        #TODO serial validations
        
        if self.serial == 'exit':
            continue_testing = False
        else:
            continue_testing = True
        return continue_testing
    
    @exceptions_handler_main
    def main(self):
        super().main()
        
        Sequence = ResistanceTestSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuut
    def post_uut(self):
        super().post_uut()
        
        Sequence = CreateTestResultsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        Sequence = ReportResultsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
    
    @exceptions_handler_postuutloop
    def post_uut_loop(self):
        super().post_uut_loop()

        Sequence = CloseInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence