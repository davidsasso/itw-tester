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
from.sequences import PrintLabelSequence
from .sequences import SaveResultsSequence
from .sequences import DefineCustomParametersSequence

from .utilities.custom_exceptions import exceptions_handler_preuutloop, PreUUTLoopException
from .utilities.custom_exceptions import exceptions_handler_preuut
from .utilities.custom_exceptions import exceptions_handler_main
from .utilities.custom_exceptions import exceptions_handler_postuut
from .utilities.custom_exceptions import exceptions_handler_postuutloop

from .libraries.DMM import exceptions as ExceptionsDMM
from .libraries.Printer import exceptions as ExceptionsPrinter


class AbstractProcessModel:
    
    def __init__(self):
        self.parameters = Parameters()
        
    def pre_uut_loop(self):
        #print('1. Creating instruments')
        print(f'Running: -- [PreUUTLoop] --')
    
    def pre_uut(self):
        #self.serial = input('2. Scan Serial:')
        print(f'Running: -- [PreUUT] --')
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

    #@exceptions_handler_preuutloop    
    def pre_uut_loop(self):
        super().pre_uut_loop()
        try:
            Sequence = ReadConfigurationFiles(parameters=self.parameters)
            self.parameters = Sequence.parameters
            del Sequence
            
            Sequence = DefineCustomParametersSequence(parameters=self.parameters)
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
            
        except ExceptionsDMM.OpenError:
            raise ExceptionsDMM.OpenError('')
        
        except ExceptionsPrinter.PrinterOpenError:
            raise ExceptionsPrinter.PrinterOpenError('')
        
        except:
            raise PreUUTLoopException('')
    
    @exceptions_handler_preuut
    def pre_uut(self):
        super().pre_uut()
        
        #Sequence = WaitTriggerSequence(parameters=self.parameters)
        #self.parameters = Sequence.parameters
        #del Sequence
        
        Sequence = SerializeSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence
        
        self.serial = self.parameters.current_serial
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
    
    #@exceptions_handler_postuut
    def post_uut(self):
        super().post_uut()
        
        try:
        
            Sequence = CreateTestResultsSequence(parameters=self.parameters)
            self.parameters = Sequence.parameters
            del Sequence
            
            Sequence = SaveResultsSequence(parameters=self.parameters)
            self.parameters = Sequence.parameters
            del Sequence
            
            Sequence = ReportResultsSequence(parameters=self.parameters)
            self.parameters = Sequence.parameters
            del Sequence
            
            Sequence = PrintLabelSequence(parameters=self.parameters)
            self.parameters = Sequence.parameters
            del Sequence
            
        except ExceptionsPrinter.PrinterOpenError:
            raise ExceptionsPrinter.PrinterOpenError('')
        
        except:
            raise PreUUTLoopException('')
            
    
    @exceptions_handler_postuutloop
    def post_uut_loop(self):
        super().post_uut_loop()

        Sequence = CloseInstrumentsSequence(parameters=self.parameters)
        self.parameters = Sequence.parameters
        del Sequence