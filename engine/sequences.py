class AbstractSequence:
    
    def __init__(self):
        pass
    
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

class DummySequence(AbstractSequence):

    def __init__(self):
        pass
    
    def setup(self):
        print('\t1. Setup')
    
    def main(self):
        print('\t2. Main')
    
    def cleanup(self):
        print(f'\t3. Cleanup')
