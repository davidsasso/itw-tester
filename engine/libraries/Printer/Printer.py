
# Website Support: https://www.zebra.com/us/en/support-downloads/printers/desktop/zd411.html
# Website Supplies: https://www.zebra.com/la/es/products/supplies.html
# Website Quickstart Guide https://www.zebra.com/content/dam/zebra_new_ia/en-us/manuals/printers/desktop/zd411d/zd411d-qsg-en-fr-esla.pdf

import serial
import subprocess
import os
import winreg
from infi.devicemanager import DeviceManager
from zebra import Zebra
try:
    from exceptions import PrinterOpenError, PrinterZPLTemplateError, PrinterDriverError, PrinterZPLFileError
except:
    from .exceptions import PrinterOpenError, PrinterZPLTemplateError, PrinterDriverError, PrinterZPLFileError

class Printer:
    '''Parent/Abstract class'''
    
    def __init__(self, instrument_type: str):
        if instrument_type == "ZD411":
            self.__class__ = ZD411
        self.instrument_type = instrument_type

    def open(self, address):
        self.address = address
        pass
    
    def error_manager(self):
        pass
    
    def close(self):
        pass


class ZD411(Printer):
    '''Child/Implementation class'''
    
    def __init__(self):
        self.handle = Zebra()
        self.template_content = ''
    
    def open(self, address):
        self.address = address
        connected = self.is_connected()
        if connected:
            print(f'Printer Found: {self.address}')
        else:
            raise PrinterOpenError('Printer not connected.')
      
    def is_connected(self):
        device_manager = DeviceManager()
        device_manager.root.rescan()
        devices = device_manager.all_devices
        connected = any(device.description == address for device in devices)
        return connected
          
    def configure(self, template_filepath: str, intensity: int, home_x: int, home_y: int):
        self.template_filepath = template_filepath
        self.intesity = intensity
        self.home_x = home_x
        self.home_y = home_y
       
    def read_template(self):
        try:
            with open(self.template_filepath,"r+") as template:
                content = template.read()
        except:
            raise PrinterOpenError(f'Template file does not exists, location: {self.template_filepath}')
        return content
       
    def generate_label(self,template_filepath: str, parameters: list, label_filepath: str):
        """Fill template file and create final file to print"""
        self.template_filepath = template_filepath
        self.label_filepath = label_filepath

        content = self.read_template()
        
        # Ensure template and parameters match
        template_total_parameters = content.count("%s")
        final_total_parameters = len(parameters)
    
        if not template_total_parameters == final_total_parameters:
            raise PrinterZPLTemplateError(f'Invalid Parameters: Template {template_total_parameters}, Using {final_total_parameters}')
        
        # Modify content with parameters
        modified_content = content
        for parameter in parameters:
            modified_content = modified_content.replace("%s", parameter, 1)  # Third argument, limits 1 replacement for each iteration
        
        self.create_label_file(self.label_filepath, modified_content)
    
    def create_label_file(self, filepath: str, content: str):
        try:
            # Open file in write mode ('w')
            with open(filepath, 'w') as file:
                # Escribir el contenido en el archivo
                file.write(content)
        except:
            raise PrinterZPLTemplateError('Label was not created')
    
    def print(self, filepath: str):
        """Send command via CMD to print"""
        try:
            if not os.path.exists(filepath):
                raise PrinterZPLFileError(f"Label {filepath} does not exists")
            command = "ssdal.exe" ,"/p", f"{self.address}", "send", f"{filepath}"
            print('Print Command: ', command)
            subprocess.call(["ssdal.exe" ,"/p", f"{self.address}", "send", f"{filepath}"])
        except Exception as e:
            raise e
            raise PrinterDriverError(f"Check if SSDAL.EXE is installed in C:\\Windows")
    
    def print_shot(self,template_filepath: str, parameters: list, label_filepath: str):
        connected = self.is_connected()
        if not connected:
            raise PrinterOpenError('Printer not connected.')
        self.generate_label(template_filepath, parameters, label_filepath)
        self.print(label_filepath)

        
    def close(self):
        pass


if __name__ == '__main__':
    address = 'ZDesigner ZD411-203dpi ZPL'
    printer = ZD411()
    printer.open(address)
    template = 'C:\ITW\itw-tester\engine\settings\data\zpl_template.txt'
    parameters = ['40', '10', '70', 'DECALV2', 'DCALV2a', 'asgrhwthtj']
    label = 'C:\ITW\itw-tester\engine\settings\data\zpl_file.txt'
    #printer.generate_label(template, parameters, label)
    printer.print_shot(template, parameters, label)
    
    