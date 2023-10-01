import pyvisa
from exceptions import UnknownError, OpenError, CommandError, ResponseError, CloseError

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
    
    
    def open(self, address):
        try:
            self.rm = pyvisa.ResourceManager()
            self.reference = self.rm.open_resource(address)
        except:
            raise OpenError('Connection Failed')
    
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

    @__execute_command
    def set_mode(self, mode):
        # Send the instrument resistance mode
        return 'CONF:RES'

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

    @__execute_command
    def set_range_value(self, value):
        return 'CONF:RANG 50E+1'

    @__execute_command_with_response
    def measure_resistance(self):
        return 'MEAS:RES?'

    @__execute_command_with_response
    def get_error_status(self):
        return 'SYST:ERR?'
    
    def close(self):
        self.reference.close()
        self.rm.close()
