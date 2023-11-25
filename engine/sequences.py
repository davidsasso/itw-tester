import os
import sys

from .utilities.datatypes import Parameters
from .utilities.datatypes import StationSettings, InstrumentSettings, TestSettings
from .utilities.datatypes import TestResults
from .libraries.DMM.DMM import DMM, Gdm834x
from .libraries.Printer.Printer import Printer, ZD411
from .libraries.DAQ.DAQ import DAQ, FX3U
from .libraries.Printer import exceptions as PrinterExceptions
from .utilities import utilities as utils

from .utilities.utilities import Timer, Serializer
class AbstractSequence:
    
    def __init__(self, parameters: Parameters):
        self.parameters = parameters
        self.name = type(self).__name__
        print(f'Executed Sequence: [{self.name}]')
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

class ReadConfigurationFiles(AbstractSequence):
    
    def main(self):
        # Define settings paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            settings_folder = os.path.join(sys._MEIPASS, 'engine', 'settings')
        else:
            # Running from source code
            settings_folder = os.path.join(current_dir, 'settings')
        
        station_settings_path = os.path.join(current_dir, f'{settings_folder}\\station_settings.ini')
        instrument_settings_path = os.path.join(current_dir, f'{settings_folder}\\instrument_settings.ini')
        test_settings_path = os.path.join(current_dir, f'{settings_folder}\\test_settings.ini')
        
        # Load Parameters
        self.parameters.StationSettings = StationSettings(filepath=station_settings_path)
        self.parameters.InstrumentSettings = InstrumentSettings(filepath=instrument_settings_path)
        self.parameters.TestSettings = TestSettings(filepath=test_settings_path)
        
        return super().main()

class DefineCustomParametersSequence(AbstractSequence):
    
    def main(self):
        # Define settings paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            settings_folder = os.path.join(sys._MEIPASS, 'engine', 'settings')
        else:
            # Running from source code
            settings_folder = os.path.join(current_dir, 'settings')
        print('Settings:')
        print(settings_folder)
        
        # Main Folder
        self.parameters.main_folder = 'C:\ITW' # ITW Main Folder
        
        # Printer
        printer = self.parameters.InstrumentSettings.Printer
        printer.zpl_absolute_template = f'{settings_folder}\\{printer.zpl_template}'
        printer.zpl_absolute_file = f'{settings_folder}\\{printer.zpl_file}'
        
        return super().main()

class AddonsSequence(AbstractSequence):
    
    def main(self):
        # Define settings paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            settings_folder = os.path.join(sys._MEIPASS, 'engine', 'settings')
        else:
            # Running from source code
            settings_folder = os.path.join(current_dir, 'settings')
        
        ITW_PATH = self.parameters.main_folder
        history_filepath = utils.create_text_file(ITW_PATH)
        self.parameters.TraceInformation.current_history_filepath = history_filepath
        
        return super().main()

class CreateInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            inst_type = dmm.instrument_type
            dmm.handle = Gdm834x()
            print(f'-\tDMM type is: {dmm.handle}')
        
        # Printer
        printer = self.parameters.InstrumentSettings.Printer
        if printer.enabled:
            printer.handle = ZD411()
            print(f'-\tPrinter type is: {printer.handle}')
        
        # DMM
        daq = self.parameters.InstrumentSettings.DAQ
        if daq.enabled:
            inst_type = daq.instrument_type
            daq.handle = FX3U()
            print(f'-\tDAQ type is: {daq.handle}')
            
        #TBD
        
        return super().main()

class InitializeInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            address = dmm.address
            dmm.handle.open(address=address)
            print('-\tDMM opened.')
            
        # DAQ
        daq = self.parameters.InstrumentSettings.DAQ
        if daq.enabled:
            address = daq.address
            daq.handle.open(address=address)
            print('-\tDAQ opened.')
            
        try:  
            # Printer
            printer = self.parameters.InstrumentSettings.Printer
            if printer.enabled:
                address = printer.address
                print(address)
                printer.handle.open(address=address)
        except Exception as e:
            raise e
        #TBD
        
        return super().main()

class ConfigureInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            operation_mode = dmm.handle.RESISTANCE_MODE
            operation_range = dmm.handle.RANGE_500
            dmm.handle.configure(mode=operation_mode, range=operation_range)
            print(f'-\tDMM configured\nMode:{operation_mode}\nRange:{operation_range}')
        #TBD
        
        return super().main()

# [PreUUT Sequences]

class WaitTriggerSequence(AbstractSequence):
    
    def main(self):
        print('Waiting for Trigger...')
        daq = self.parameters.InstrumentSettings.DAQ
        wait = True
        
        while wait:
            print(daq.handle)
            response = daq.handle.read_coil(address=1)
            print('response', response)
            #response = not response # invert polarity
            
            trigger_signal = self.parameters.InstrumentSettings.DAQ.signal
            
            if response == trigger_signal:
                print('Trigger Detected!')
                break
            else:
                print('Waiting for DAQ...')
        return super().main()

class WaitTimeTriggerSequence(AbstractSequence):
    
    def main(self):
        print('Waiting for Trigger...')
        timer = Timer()
        timer.reset()
        
        target_time = 5000
        
        timeout = False
        
        while not timeout:
            current_time = timer.elapsed_time()
            
            if current_time >= target_time:
                timeout = True
        print('Trigger Detected!')
        return super().main()    
    
class SerializeSequence(AbstractSequence):
    
    def main(self):
        # Part Number
        part_number = self.parameters.StationSettings.Product.part_number
        
        # Consecutive
        ITW_PATH = self.parameters.main_folder
        history_filepath = utils.create_text_file(ITW_PATH)
        self.parameters.TraceInformation.current_history_filepath = history_filepath
        last_result = utils.get_last_line(filepath=history_filepath)
        
        try:
            information = last_result.split(',') #[DECALV32023111114102200001, 0.0 FAIL]
            last_serial = information[0] # DECALV32023111114102200001
            consecutive = last_serial[-5:-1]
            consecutive = int(consecutive)
            incremented_consecutive = consecutive + 1
        except:
            incremented_consecutive = 1
            
        new_consecutive = str(incremented_consecutive).zfill(4)
        print('Este es el consecutivo: ', new_consecutive)
            
        # Datecode
        serializer = Serializer()
        datecode = serializer.generate()
        del serializer
        
        # Cell ID
        cell_id = self.parameters.StationSettings.StationData.cell_id
        
        # Full Serial
        serial = f'{part_number}{datecode}{new_consecutive}{cell_id}'
        
        print("Serial Name:", serial)
        
        self.parameters.current_serial = serial

        return super().main()

# [Main Sequences]

class ResistanceTestSequence(AbstractSequence):
    
    def main(self):
        
        tests = self.parameters.TestSettings
        dmm = self.parameters.InstrumentSettings.DMM
        
        if tests.ResistanceTest.test_active and dmm.enabled:
            #TODO measure time
            test_timer = Timer()
            test_timer.reset()
            
            dmm = self.parameters.InstrumentSettings.DMM.handle
            response = dmm.measure_resistance()
            response = dmm.measure_resistance()
            response = dmm.measure_resistance()
            measurement = float(response)
            
            time = test_timer.elapsed_time_seconds()
            time = round(time, 2)
            tests.ResistanceTest.measurement = measurement
            tests.ResistanceTest.test_time = time
        
        
        return super().main()


# [Post Sequences]

class CreateTestResultsSequence(AbstractSequence):
    
    def main(self):
        
        self.parameters.TestResults.clear() # resets results
        
        tests = self.parameters.TestSettings
        
        if tests.ResistanceTest.test_active:
            results = TestResults(test=tests.ResistanceTest)
            self.parameters.TestResults.append(results)
            tests.ResistanceTest.measurement = None
            tests.ResistanceTest.test_time = None
        
        general_result = 'FAIL'
        all_results = []
        for test in self.parameters.TestResults:
            all_results.append(test.result)
            
        if not 'FAIL' in all_results:
            general_result = 'PASS'
        
        self.parameters.general_result = general_result
        return super().main()

class SaveResultsSequence(AbstractSequence):
    
    def main(self):
        """Save serial and general result into a textfile for traceability"""
        try:
            ITW_PATH = 'C:\ITW'
            serial = self.parameters.current_serial
            general_result = self.parameters.general_result
            measurement = self.parameters.TestResults[0].measure # Using just 1 test
            line = f"{serial},{measurement},{general_result}"
            history_filepath = utils.create_text_file(ITW_PATH)
            utils.append_line_to_text_file(path=history_filepath, line=line)
            print("Added result to History textfile")
        except:
            print('No se pudo guardar nada en el archivo de texto')
        return super().main()

class ReportResultsSequence(AbstractSequence):
    
    def main(self):
        #TODO save results to database
        #self.parameters.TestResults.clear()
        return super().main()

class PrintLabelSequence(AbstractSequence):
    
    def main(self):
        
        # Printer
        printer = self.parameters.InstrumentSettings.Printer
        if printer.enabled:
            passed = self.parameters.general_result == "PASS"
            
            template = self.parameters.InstrumentSettings.Printer.zpl_absolute_template  #C:\ITW\itw-tester\engine\settings\data\zpl_template.txt'
            label = self.parameters.InstrumentSettings.Printer.zpl_absolute_file         #'C:\ITW\itw-tester\engine\settings\data\zpl_file.txt'
            current_serial = self.parameters.current_serial
            
            parameters = ['30', '0', '0', current_serial, current_serial]
            
            if passed:
                try:
                    
                    printer.handle.print_shot(template, parameters, label)
                
                except PrinterExceptions.PrinterOpenError:
                    raise PrinterExceptions.PrinterOpenError('Printer Disconected: Please Reset')
        #TBD
            #self.parameters.TestResults.clear()
            return super().main()

# [PostUUTLoop Sequences]

class CloseInstrumentsSequence(AbstractSequence):
    
    def main(self):
        
        # DMM
        dmm = self.parameters.InstrumentSettings.DMM
        if dmm.enabled:
            try:
                dmm.handle.close()
                print(f'-\tDMM Closed')
            except:
                pass
        # DAQ
        daq = self.parameters.InstrumentSettings.DAQ
        if daq.enabled:
            try:
                daq.handle.close()
                print(f'-\tDAQ Closed')
            except:
                pass
        #TBD
        
        return super().main()
