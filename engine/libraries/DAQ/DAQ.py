
# Website Support Pymodbus : https://pymodbus.readthedocs.io/en/latest/

import time
from infi.devicemanager import DeviceManager
from pymodbus.client import ModbusSerialClient

try:
    from exceptions import DAQOpenError, DAQConnectionError, DAQResponseError
except:
    from .exceptions import DAQOpenError, DAQConnectionError, DAQResponseError

class DAQ:
    '''Parent/Abstract class'''
    
    def __init__(self, instrument_type: str):
        if instrument_type == "FX3U":
            self.__class__ = FX3U
        self.instrument_type = instrument_type

    def open(self, address):
        self.address = address
        pass
    
    def error_manager(self):
        pass
    
    def close(self):
        pass


class FX3U(DAQ):
    '''Child/Implementation class'''
    
    def __init__(self):
        self.client = None
    
    def open(self, address: str):
        self.address = address
        self.client = ModbusSerialClient(method='rtu', port=address, baudrate=19200, timeout=1)
        self.handle = self.client.connect()
        
        if self.handle:
            print(f'PLC Found: {self.address}')
        else:
            raise DAQOpenError('PLC not connected.')
      
    def is_connected(self):
        connected = False
        if not self.client.is_socket_open():
            print("Not connected to the Modbus server.")
        else:
            print("Good connection to the Modbus server.")
            connected = True
        return connected
  
    def read_coil(self, address: int):
        try:
            result = self.client.read_coils(address=address, count=1, slave=1)
            
            # Check if the request was successful
            if result.isError():
                raise DAQConnectionError('')
            else:
                print(f"Coil Response: {address}:", result.bits[0])
                return result.bits[0]
        except:
            raise DAQConnectionError('')

    def write_coil(self, address: int, value: bool):
        try:
            result = self.client.write_coil(address=address, value=value, slave=1)

            # Check if the request was successful
            if result.isError():
                print('modbus error')
                raise DAQConnectionError('')
            else:
                print(f"Coil Write Response: {address}: {value}")
                return True
        except:
           raise DAQConnectionError('')

        
    def close(self):
        self.client.close()


if __name__ == '__main__':
    # Puerto COM del RS-485
    address = 'COM9'
    
    plc = FX3U()
    plc.open(address)
    plc.is_connected()

    # Estado Actual de las Salidas Y0 y Y1
    value = plc.read_coil(address=0)
    value = plc.read_coil(address=1)

    # Activa Salida Y0, espera y la apaga
    plc.write_coil(address=0, value=True)
    time.sleep(2)
    plc.write_coil(address=0, value=False)
    time.sleep(2)

    # Activa Salida Y1, espera y la apaga
    plc.write_coil(address=1, value=True)
    time.sleep(2)
    plc.write_coil(address=1, value=False)
    time.sleep(2)
    
    # Cierra comunication
    plc.close()
    
    """ plc.read_coil(address=1)
    time.sleep(1)
    plc.read_coil(address=1)
    time.sleep(1)
    plc.read_coil(address=1)
    time.sleep(1)
    plc.read_coil(address=1)
    time.sleep(1)
    plc.read_coil(address=1)
    time.sleep(1) """
    
    