class AbstractSequence:
    
    def __init__(self):
        self.name = type(self).__name__
        print(f'[{self.name}]')
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

class CreateInstrumentsSequence(AbstractSequence):
    
    def setup(self):
        print('\t\t- read instrument settings')
        return super().setup()
    
    def main(self):
        print('\t\t- create instruments')
        return super().main()
    
    def cleanup(self):
        return super().cleanup()

class ConfigureInstrumentsSequence(AbstractSequence):
    
    def main(self):
        print('\t\t- configure instruments')
        return super().main()

# [PreUUT Sequences]



# [Main Sequences]

class ResistanceTestSequence(AbstractSequence):
    
    def main(self):
        print('\t\t- Executing resistance test')
        return super().main()


# [Post Sequences]

class ReportResultsSequence(AbstractSequence):
    
    def main(self):
        print('\t\t- Reporting results to database')
        return super().main()


# [PostUUTLoop Sequences]