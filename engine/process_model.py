from .datatypes.parameters import Parameters

from .sequences import CreateInstrumentsSequence
from .sequences import ConfigureInstrumentsSequence
from .sequences import ResistanceTestSequence
from .sequences import ReportResultsSequence


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
        self.parameters = Parameters()
        
    def pre_uut_loop(self):
        print('\n1. Create DMM and connection to database')
        #TODO read station settings
        #TODO read instrument settings
        #TODO read test settings
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