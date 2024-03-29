# Native Imports
from PyQt5.QtGui import QPixmap
from datetime import date, datetime,timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
import os
import sys
import pyvisa

# Custom Imports
#from ui.main_window import Ui_MainWindow
from ui.gui import Ui_MainWindow
from engine.utilities.datatypes import StationSettings
from engine.engine import Engine
from engine.process_model import ITWProcessModel
from engine.libraries.DMM import exceptions as DMMExceptions
from engine.libraries.Printer import exceptions as PrinterExceptions

class Application(QtWidgets.QMainWindow):
    """ Main Application parser for Custom Application """
    
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        #self.showMaximized() # un-comment to show maximized main window
        
    def closeEvent(self, event):
        print("App Closed")
        application_window.close_application()
        event.accept()


class CustomApplication():
    """ Custom application definitions. """

    def __init__(self, app_widgets, app=None):
        ''' Constructor method for custom application.'''
        if app == None:
            self.app = Application()
        self.app = app
        self.Model = None
        self.continue_testing = True
        self.connect_signals()
        self.initialize()
        self.app.show()

    def connect_signals(self):
        ''' Method for connect all signals from widgets'''
        self.app.ui.StartButton.clicked.connect(self.start)
        self.app.ui.StopButton.clicked.connect(self.stop)
        self.app.ui.TestButton.clicked.connect(self.test_trigger)
        # Establecer atajo de teclado para el botón (Enter)
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.app)
        shortcut.activated.connect(self.test_trigger)
        self.app.ui.actionDevicesList.triggered.connect(self.show_devices_list)
    
    def initialize(self):
        self.read_configuration()
        self.initialize_table()
    
    def read_configuration(self):
        # Define settings paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            settings_folder = os.path.join(sys._MEIPASS, 'engine', 'settings')
        else:
            # Running from source code
            settings_folder = os.path.join(current_dir, 'engine\settings')
        
        station_settings_path = os.path.join(current_dir, f'{settings_folder}\\station_settings.ini')
        
        print('STATIONNAME')
        print(station_settings_path)
        
        self.StationSettings = StationSettings(filepath=station_settings_path)
        
        station_name = self.StationSettings.StationData.station_name
        self.app.ui.StationNameLabel.setText(station_name)
    
    def initialize_table(self):
        table = self.app.ui.TestResultsTable
        table.setColumnWidth(0, 150)
        table.setColumnWidth(1, 90)
        table.setColumnWidth(2, 90)
        table.setColumnWidth(3, 90)
        table.setColumnWidth(4, 90)
        table.setColumnWidth(5, 90)
        table.setColumnWidth(6, 90)
        QApplication.processEvents()
        
    def start(self):
        print('Started')
        #TODO pass model from settings
        self.Model = ITWProcessModel()
        self.engine = Engine(sequence_process_model=self.Model)
        self.show_user_message('Configurando Instrumentos')
        #self.engine.pre_uut_loop()
        self.run()
        #self.show_user_message('Instruments Ready')
        #self.show_user_message('Waiting for unit')
    
    def test(self):
        print('Test\n')
    
        self.show_user_message('Probando')
        
        self.engine.pre_uut()
        self.engine.main()
        self.engine.post_uut()
        
        self.app.ui.SerialLineEdit.setText('')
        self.show_user_message('Escanea Serial')
    
    def run(self):
        continue_testing = self.continue_testing
        try:
            self.engine.pre_uut_loop()
            
        except DMMExceptions.OpenError:
            self.showMessageBox('Advertencia', 'Multimetro no detectado, Conectalo y Enciendelo')
            self.stop()
        except PrinterExceptions.PrinterOpenError:
            self.showMessageBox('Advertencia', 'Impresora no detectada, Conectalo y Enciendelo')
            self.stop()
        except Exception as e:
            print(e)
            self.showMessageBox('Warning', 'Error in PreUUTLoop')
            self.stop()
            
        
        self.show_user_message('Instrumentos Listos')
        self.show_user_message('CONECTA LAS TERMINALES')
        self.app.ui.MainMessageLineEdit.setText('PRESIONA ENTER')
        self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: white;')
        self.app.ui.TestButton.setEnabled(True)
        self.app.ui.StopButton.setEnabled(True)
        self.app.ui.StartButton.setEnabled(False)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.test_trigger)
        self.timer_interval = 3000  # 5000 milliseconds = 5 seconds
        
        #self.timer.start(self.timer_interval)
    
    def idle(self):
        pass
    
    def test_trigger(self):
        self.reset_indicators()
        QApplication.processEvents()
        print('-------------------------------------------------------------------------------------------')
        continue_testing = self.continue_testing
        
        if continue_testing:
            
            try:
                continue_testing = self.engine.pre_uut()
                self.app.ui.SerialLineEdit.setText(self.engine.process_model.parameters.current_serial)
                self.engine.main()
                self.engine.post_uut()
                self.update_views()
                
            except PrinterExceptions.PrinterOpenError:
                self.showMessageBox('Advertencia', 'Impresora no detectada, Conectala')
                self.showMessageBox('Advertencia', 'Intenta hacer la prueba')
                self.app.ui.SerialLineEdit.setText('')
                self.show_user_message('CONECTA LAS TERMINALES')
                self.app.ui.MainMessageLineEdit.setText('PRESIONA ENTER')
                self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: white;')
        
        else:
            self.engine.post_uut_loop()
    
    def update_views(self):
        general_result = self.engine.process_model.parameters.general_result
        self.app.ui.MainMessageLineEdit.setText(general_result)
        
        if general_result == 'PASS':
            self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: green;')
            self.app.ui.MainMessageLineEdit.setText('PASA')
            self.app.ui.UserMessageLabel.setText('COLOCA LA ETIQUETA')
        elif general_result == 'FAIL':
            self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: red;')
            self.app.ui.MainMessageLineEdit.setText('FALLA')
            self.app.ui.UserMessageLabel.setText('PRUEBA DE NUEVO')
        else:
            pass
        
        
        self.update_results_table(self.engine.process_model.parameters.TestResults)
    
    def update_results_table(self, test_results_list):
        table = self.app.ui.TestResultsTable
        font = QtGui.QFont("Arial", 10)
        table.setFont(font)
        table.setRowCount(len(test_results_list))
        
        for row, test_result in enumerate(test_results_list):
            for col, value in enumerate([test_result.test_name, str(test_result.low_limit),
                                        str(test_result.high_limit), str(test_result.measure),
                                        test_result.units, test_result.result, str(test_result.time)]):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)  # Center-align the text
                table.setItem(row, col, item)
        
        QApplication.processEvents()
    
    def reset_indicators(self):
        self.app.ui.MainMessageLineEdit.setText('Probando')
        self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: yellow;')
        
        self.app.ui.UserMessageLabel.setText('Probando...')
        
        self.app.ui.SerialLineEdit.setText('')
        
        table = self.app.ui.TestResultsTable
        table.clearContents()
        table.setRowCount(0)
        QApplication.processEvents()
        
    def showMessageBox(self, title, message):
        QMessageBox.information(self.app, title, message, QMessageBox.Ok)

    def show_devices_list(self):
        rm = pyvisa.ResourceManager()
        devices = rm.list_resources()
        rm.close()

        device_list_text = "\n".join(devices)
        QMessageBox.information(self.app, 'Dispositivos Encontrados', device_list_text)
    
    def stop(self):
        #self.timer.stop()
        self.app.ui.MainMessageLineEdit.setText('CERRANDO')
        self.show_user_message('Cerrando Aplicacion')
        QApplication.processEvents()
        print('Stopped')
        try:
            self.engine.post_uut_loop()
        except AttributeError:
            pass
        self.close_application()
        
    def close_application(self):
        self.app.close()

# Functions

    def show_user_message(self, message: str):
        self.app.ui.UserMessageLabel.setText(message)

if __name__ == '__main__':
    #TODO read station settings
    #TODO create error log
    app_widgets = QtWidgets.QApplication(sys.argv)
    app_widgets.setStyle('Fusion')
    app_root = Application()
    application_window = CustomApplication(app_widgets=app_widgets, app=app_root)
    sys.exit(app_widgets.exec())
