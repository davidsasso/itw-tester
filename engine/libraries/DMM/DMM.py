
class DMM:
    '''Parent/Abstract class'''
    
    def __init__(self, instrument_type: str):
        if instrument_type == "GDM834X":
            self.__class__ = GDM834X
        self.instrument_type = instrument_type

    def open(self, address):
        self.address = address
        pass
    
    def configure(self):
        pass
    
    def error_manager(self):
        pass
    
    def close(self):
        pass

class GDM834X(DMM):
    '''Child/Implementation class'''
    pass
