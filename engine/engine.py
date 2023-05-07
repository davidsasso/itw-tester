from .process_model import AbstractProcessModel
from .process_model import DummyProcessModel

class Engine:
    
    def __init__(self, sequence_process_model):
        self.process_model = sequence_process_model
        self.continue_testing = True

    def pre_uut_loop(self):
        '''
        
        1.[Initial configuration]
        - Create/Open references from hardware setup.
        
        '''
        self.process_model.pre_uut_loop()
    
    def pre_uut(self, serial):
        '''
        
        2.[Pre-Test configuration]
        - No more hardware configuration left.
        - Serial from unit under test (uut).
        
        '''
        continue_testing = self.process_model.pre_uut(serial=serial)
        return continue_testing
    
    def main(self):
        '''
        
        3.[Tests execution]
        - Hardware interaction.
        - Measurements.
        - Evaluations.
        - test passed/failed
        
        '''
        self.process_model.main()
    
    def post_uut(self):
        '''
        
        4.[Post-Test information]
        - Report general result (passed/failed tests).
        - Create uut's test report.
        
        '''
        self.process_model.post_uut()
    
    def post_uut_loop(self):
        '''
        
        1.[Initial configuration]
        - Close references from hardware setup.
        
        '''
        self.process_model.post_uut_loop()

    def run_sequence(self):
        continue_testing = self.continue_testing
        
        self.pre_uut_loop()
        
        while continue_testing:
            
            continue_testing = self.pre_uut()
            if not continue_testing:
                break
            else:
                self.main()
                self.post_uut()
        self.post_uut_loop()

if __name__ == '__main__':
    Model = DummyProcessModel()
    engine = Engine(sequence_process_model=Model)
    engine.run_sequence()