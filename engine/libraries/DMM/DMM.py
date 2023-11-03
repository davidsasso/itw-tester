import pyvisa
from .exceptions import UnknownError, OpenError, CommandError, ResponseError

class DMM:
    '''Parent/Abstract class'''
    
    def __init__(self, instrument_type: str):
        if instrument_type == "GDM834X":
            self.__class__ = Gdm834x
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


class Gdm834x(DMM):
    '''Child/Implementation class'''
    
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        
        # Private Variables
        self.RESISTANCE_MODE = 'RES'
        self.VOLTAGE_MODE = ''
        self.CURRENT_MODE = ''
        self.RANGE_500 = '50E+1'
        self.RANGE_5000 = ''
        self.RANGE_50000 = ''
    
    
    def open(self, address):
        try:
            self.rm = pyvisa.ResourceManager()
            self.reference = self.rm.open_resource(address)
            id = self.get_id()
        except:
            raise OpenError('Reset DMM')
    
    def __execute_command(func):
        def wrapper(self, *args, **kwargs):
            command = func(self, *args, **kwargs)
            try:
                self.reference.write(command)
            except:
                raise CommandError(f'Command {command} Failed')
            return ''
        return wrapper

    def __execute_command_with_response(func):
        def wrapper(self, *args, **kwargs):
            command = func(self, *args, **kwargs)
            try:
                self.reference.write(command)
                value = self.reference.read()
            except:
                value = None
                raise ResponseError(f'Command {command} Failed')
            return value
        return wrapper
    
    @__execute_command_with_response
    def get_id(self):
        return '*IDN?'
    
    @__execute_command_with_response
    def get_version(self):
        return 'SYST:VERS?'
    

    @__execute_command_with_response
    def get_serial_number(self):
        return 'SYST:SER?'

    def set_mode(self, mode):
        if mode == self.RESISTANCE_MODE:
            self.set_mode_value(mode)
        elif mode == self.VOLTAGE_MODE:
            self.set_mode_value(mode)
        elif mode == self.CURRENT_MODE:
            self.set_mode_value(mode)
        else:
            pass #invalid mode
    
    @__execute_command
    def set_mode_value(self, value):
        return f'CONF:{value}'

    @__execute_command_with_response
    def get_current_mode(self):
        return 'CONF:FUNC?'

    @__execute_command
    def set_auto_range_status(self, status: bool):
        if status:
            return 'CONF:AUTO ON'
        else:
            return 'CONF:AUTO OFF'

    @__execute_command_with_response
    def get_auto_range_status(self):
        return 'CONF:AUTO?'

    
    @__execute_command_with_response
    def get_current_range(self):
        return 'CONF:RANG?'

    def set_range(self, range):
        if range == self.RANGE_500:
            self.set_range_value(range)
        elif range == self.RANGE_5000:
            self.set_range_value(range)
        elif range == self.RANGE_50000:
            self.set_range_value(range)
        else:
            pass #invalid
    
    @__execute_command
    def set_range_value(self, value):
        return f'CONF:RANG {value}'

    @__execute_command_with_response
    def measure_resistance(self):
        return 'MEAS:RES?'

    @__execute_command_with_response
    def get_error_status(self):
        return 'SYST:ERR?'
    
    def configure(self, mode, range):
        
        self.set_mode(mode)
        self.set_auto_range_status(False)
        self.set_range(range)
        
    
    
    def close(self):
        try:
            self.reference.close()
            self.rm.close()
        except:
            pass
