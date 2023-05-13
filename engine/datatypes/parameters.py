class Parameters:
    
    def __init__(self):
        self.parameters = {}
        
    def add(self, parameter_name: str, parameter_value):
        self.parameters[parameter_name] = parameter_value
        print(f'[Parameters]\n{self.parameters}')
        parameters_copy = self.parameters #self.parameters.copy()
        return parameters_copy
    
    def get(self, parameter_name: str):
        return self.parameters[parameter_name]