from .datatypes.parameters import Parameters
from .sequences import DummySequence


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

class DummyProcessModel(AbstractProcessModel):
    
    def __init__(self):
        pass
        
    def pre_uut_loop(self):
        print('1. Creating DUMMY instruments')
        #TODO read configuration files
        self.parameters = Parameters()
        #TODO use defined sequence from configuration files
        self.Sequence = DummySequence()
        
    def pre_uut(self, serial):
        self.serial = serial
        #TODO serial validations
        
        if self.serial == 'exit':
            continue_testing = False
        else:
            continue_testing = True
        return continue_testing
    
    def main(self):
        print(f'3. Testing DUMMY {self.serial}')
        #TODO main tests
        self.Sequence.run()
    
    def post_uut(self):
        print(f'4. Report DUMMY results for {self.serial}')
        #TODO report generator
    
    def post_uut_loop(self):
        print('5. Closing DUMMY instruments')
        #TODO report generator