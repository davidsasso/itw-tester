# Native Imports
from PyQt5.QtGui import QPixmap
from datetime import date, datetime,timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import os
import sys


# Custom Imports
#from ui.main_window import Ui_MainWindow
from ui.gui import Ui_MainWindow
from engine.datatypes.local_settings import StationSettings
from engine.engine import Engine
from engine.process_model import ITWProcessModel

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
        self.app.show()

    def connect_signals(self):
        ''' Method for connect all signals from widgets'''
        self.app.ui.StartButton.clicked.connect(self.start)
        self.app.ui.StopButton.clicked.connect(self.stop)
        self.app.ui.TestButton.clicked.connect(self.test)
    
    def start(self):
        print('Started')
        #TODO pass model from settings
        self.Model = ITWProcessModel()
        self.engine = Engine(sequence_process_model=self.Model)
        self.show_user_message('Instruments Setup')
        #self.engine.pre_uut_loop()
        self.run()
        #self.show_user_message('Instruments Ready')
        #self.show_user_message('Waiting for unit')
    
    def test(self):
        print('Test\n')
    
        self.show_user_message('Testing')
        
        self.engine.pre_uut()
        self.engine.main()
        self.engine.post_uut()
        
        self.app.ui.SerialLineEdit.setText('')
        self.show_user_message('Scan Serial')
    
    def run(self):
        continue_testing = self.continue_testing
        
        self.engine.pre_uut_loop()
        self.show_user_message('Instruments Ready')
        self.show_user_message('Waiting for unit')
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.test_by_trigger)
        self.timer_interval = 3000  # 5000 milliseconds = 5 seconds
        
        self.timer.start(self.timer_interval)
        """ while continue_testing:
            
            continue_testing = self.engine.pre_uut()
            if not continue_testing:
                break
            else:
                self.engine.main()
                self.engine.post_uut()
        self.engine.post_uut_loop() """
    
    def test_by_trigger(self):
        self.reset_indicators()
        QApplication.processEvents()
        print('-------------------------------------------------------------------------------------------')
        continue_testing = self.continue_testing
        
        if continue_testing:
            
            continue_testing = self.engine.pre_uut()
            self.app.ui.SerialLineEdit.setText(self.engine.process_model.parameters.current_serial)
            self.engine.main()
            self.engine.post_uut()
            self.update_views()
        
        else:
            self.engine.post_uut_loop()
    
    def update_views(self):
        general_result = self.engine.process_model.parameters.general_result
        self.app.ui.MainMessageLineEdit.setText(general_result)
        
        if general_result == 'PASS':
            self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: green;')
        elif general_result == 'FAIL':
            self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: red;')
        else:
            pass
        
        self.app.ui.UserMessageLabel.setText('Waiting for Trigger..')
        
        self.update_results_table(self.engine.process_model.parameters.TestResults)
    
    def update_results_table(self, test_results_list):
        table = self.app.ui.TestResultsTable
        font = QtGui.QFont("Arial", 10)
        table.setFont(font)
        table.setRowCount(len(test_results_list))
        for row, test_result in enumerate(test_results_list):
            table.setItem(row, 0, QTableWidgetItem(test_result.test_name))
            table.setItem(row, 1, QTableWidgetItem(str(test_result.low_limit)))
            table.setItem(row, 2, QTableWidgetItem(str(test_result.high_limit)))
            table.setItem(row, 3, QTableWidgetItem(str(test_result.measure)))
            table.setItem(row, 4, QTableWidgetItem(test_result.units))
            table.setItem(row, 5, QTableWidgetItem(test_result.result))
            table.setItem(row, 6, QTableWidgetItem(str(test_result.time)))
        QApplication.processEvents()
    
    def reset_indicators(self):
        self.app.ui.MainMessageLineEdit.setText('TESTING')
        self.app.ui.MainMessageLineEdit.setStyleSheet('background-color: yellow;')
        
        self.app.ui.UserMessageLabel.setText('Testing...')
        
        self.app.ui.SerialLineEdit.setText('')
        
        table = self.app.ui.TestResultsTable
        table.clearContents()
        table.setRowCount(0)
        QApplication.processEvents()
        
    
    def stop(self):
        self.timer.stop()
        self.show_user_message('Stopped')
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
