# Native Imports
import os

# Custom Imports
from .datatypes.parameters import Parameters

from .sequences import CreateInstrumentsSequence
from .sequences import ConfigureInstrumentsSequence
from .sequences import ResistanceTestSequence
from .sequences import ReportResultsSequence

from .utilities.utilities import StationSettings, InstrumentSettings, TestSettings
from .utilities.custom_exceptions import PreUUTLoopException, PreUUTException, MainException, PostUUTException, PostUUTLoopException

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

    def catch_exceptions(func):
        ''' Decorator to handle all exceptions on process model'''
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PreUUTLoopException as e:
                print(f"[Error] An exception occurred in PreUUTLoop: {str(e)}")
                # handle the exception here, or re-raise it if necessary
            except PreUUTException as e:
                print(f"[Error] An exception occurred in PreUUT: {str(e)}")
                # handle the exception here, or re-raise it if necessary
            except MainException as e:
                print(f"[Error] An exception occurred in Main: {str(e)}")
                # handle the exception here, or re-raise it if necessary
            except PostUUTException as e:
                print(f"[Error] An exception occurred in PostUUT: {str(e)}")
                # handle the exception here, or re-raise it if necessary
            except PostUUTLoopException as e:
                print(f"[Error] An exception occurred in PostUUTLoop: {str(e)}")
                # handle the exception here, or re-raise it if necessary
            except Exception as e:
                print(f"[Error] Unhandled exception occurred: {str(e)}")
                # handle the exception here, or re-raise it if necessary
        return wrapper


    @catch_exceptions    
    def pre_uut_loop(self):
        try:
            print('\n1. Create DMM and connection to database')
            # Read station settings
            self.station_settings = StationSettings(filepath=self.station_settings_path)
            print(self.station_settings)
            # Read instrument settings
            self.instrument_settings = InstrumentSettings(filepath=self.instrument_settings_path)
            print(self.instrument_settings)
            # Read test settings
            self.test_settings = TestSettings(filepath=self.test_settings_path)
            print(self.test_settings)
            Sequence1 = CreateInstrumentsSequence()
            Sequence2 = ConfigureInstrumentsSequence()
        except Exception as exception_message:
            raise PreUUTLoopException(exception_message)
        
    def pre_uut(self, serial):
        try:
            #TODO wait for trigger to create serial
            #TODO serialize (create new serial)
            self.serial = serial
            #TODO serial validations
            
            if self.serial == 'exit':
                continue_testing = False
            else:
                continue_testing = True
            return continue_testing
        except Exception as exception_message:
            raise PreUUTException(exception_message)
    
    def main(self):
        try:
            print(f'\n3. Testing Resistance, unit: {self.serial}')
            #TODO main tests
            Sequence1 = ResistanceTestSequence()
        except Exception as exception_message:
            raise MainException(exception_message)
    
    def post_uut(self):
        try:
            print(f'\n4. Report Results, unit: {self.serial}')
            #TODO report generator
            Sequence1 = ReportResultsSequence()
        except Exception as exception_message:
            raise PostUUTException(exception_message)
    
    def post_uut_loop(self):
        try:
            print('\n5. Closing references and instruments')
        except Exception as exception_message:
            raise PostUUTLoopException(exception_message)