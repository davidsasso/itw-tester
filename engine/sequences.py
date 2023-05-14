import os

from .utilities.datatypes import StationSettings, InstrumentSettings, TestSettings

class AbstractSequence:
    
    def __init__(self, parameters=None):
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
        #TODO create instrument instances
        return super().main()

class InitializeInstrumentsSequence(AbstractSequence):
    
    def main(self):
        #TODO initialize or open instruments
        return super().main()

class ConfigureInstrumentsSequence(AbstractSequence):
    
    def main(self):
        #TODO configure instruments
        return super().main()

# [PreUUT Sequences]

class WaitTriggerSequence(AbstractSequence):
    
    def main(self):
        #TODO use instrument for read every certain time to start test
        return super().main()
    
class SerializeSequence(AbstractSequence):
    
    def main(self):
        #TODO define next serial and create it
        return super().main()

# [Main Sequences]

class ResistanceTestSequence(AbstractSequence):
    
    def main(self):
        #TODO execute the test meaurement
        return super().main()


# [Post Sequences]

class CreateTestResultsSequence(AbstractSequence):
    
    def main(self):
        #TODO create results table
        return super().main()

class ReportResultsSequence(AbstractSequence):
    
    def main(self):
        #TODO save results to database
        return super().main()


# [PostUUTLoop Sequences]

class CloseInstrumentsSequence(AbstractSequence):
    
    def main(self):
        #TODO close all opened instruments
        return super().main()