import os

from .utilities.datatypes import Parameters
from .utilities.datatypes import StationSettings, InstrumentSettings, TestSettings
from .utilities.datatypes import TestResults
from .libraries.DMM.DMM import DMM, Gdm834x

from .utilities.utilities import Timer, Serializer
class AbstractSequence:
    
    def __init__(self, parameters: Parameters):
        self.parameters = parameters
        self.name = type(self).__name__
        print(f'Executed Sequence: [{self.name}]')
        self.run()
    
    def setup(self):
        pass
    
    def main(self):
        pass
    
    def cleanup(self):
        pass
    
    def run(self):
        self.setup()
        self.main()
        self.cleanup()

# [PreUUTLoop Sequences]

class ReadConfigurationFiles(AbstractSequence):
    
    def main(self):
        # Define settings paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        station_settings_path = os.path.join(current_dir, 'settings\\station_settings.ini')
        instrument_settings_path = os.path.join(current_dir, 'settings\\instrument_settings.ini')
        test_settings_path = os.path.join(current_dir, 'settings\\test_settings.ini')
        
        # Load Parameters
        self.parameters.StationSettings = StationSettings(filepath=station_settings_path)
        self.parameters.InstrumentSettings = InstrumentSettings(filepath=instrument_settings_path)
        self.parameters.TestSettings = TestSettings(filepath=test_settings_path)
        
        return super().main()

class CreateInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        if self.parameters.InstrumentSettings.DMM.enabled:
            inst_type = self.parameters.InstrumentSettings.DMM.instrument_type
            self.parameters.InstrumentSettings.DMM.handle = Gdm834x()
            print(f'-\tDMM type is: {self.parameters.InstrumentSettings.DMM.handle}')
        
        #TBD
        
        return super().main()

class InitializeInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            address = dmm.address
            dmm.handle.open(address=address)
            print('-\tDMM opened.')
        
        #TBD
        
        return super().main()

class ConfigureInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            operation_mode = dmm.handle.RESISTANCE_MODE
            operation_range = dmm.handle.RANGE_500
            dmm.handle.configure(mode=operation_mode, range=operation_range)
            print(f'-\tDMM configured\nmode:{operation_mode}\nrange:{operation_range}')
        #TBD
        
        return super().main()

# [PreUUT Sequences]

class WaitTriggerSequence(AbstractSequence):
    
    def main(self):
        print('Waiting for Trigger...')
        timer = Timer()
        timer.reset()
        
        target_time = 5000
        
        timeout = False
        
        while not timeout:
            current_time = timer.elapsed_time()
            
            if current_time >= target_time:
                timeout = True
        print('Trigger Detected!')
        return super().main()
        
    
class SerializeSequence(AbstractSequence):
    
    def main(self):
        #TODO define next serial and create it

        serializer = Serializer()
        serial = serializer.generate()
        del serializer
        
        print("Serial Name:", serial)
        
        self.parameters.current_serial = serial

        return super().main()

# [Main Sequences]

class ResistanceTestSequence(AbstractSequence):
    
    def main(self):
        
        tests = self.parameters.TestSettings
        
        if tests.ResistanceTest.test_active:
            #TODO measure time
            test_timer = Timer()
            test_timer.reset()
            
            dmm = self.parameters.InstrumentSettings.DMM.handle
            response = dmm.measure_resistance()
            measurement = float(response)
            
            time = test_timer.elapsed_time_seconds()
            tests.ResistanceTest.measurement = measurement
            tests.ResistanceTest.test_time = time
        
        
        return super().main()


# [Post Sequences]

class CreateTestResultsSequence(AbstractSequence):
    
    def main(self):
        
        tests = self.parameters.TestSettings
        
        if tests.ResistanceTest.test_active:
            results = TestResults(test=tests.ResistanceTest)
            self.parameters.TestResults.append(results)
            tests.ResistanceTest.measurement = None
            tests.ResistanceTest.test_time = None
        
        print('--------------------- TEST RESULTS ---------------------')
        for test in self.parameters.TestResults:
            print(test)
        return super().main()

class ReportResultsSequence(AbstractSequence):
    
    def main(self):
        #TODO save results to database
        self.parameters.TestResults.clear()
        return super().main()


# [PostUUTLoop Sequences]

class CloseInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            dmm.handle.close()
            print(f'-\tDMM Closed')
        
        #TBD
        
        return super().main()