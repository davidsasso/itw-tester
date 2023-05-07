# Native Imports
from PyQt5.QtGui import QPixmap
from datetime import date, datetime,timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
import sys


# Custom Imports
#from ui.main_window import Ui_MainWindow
from ui.gui import Ui_MainWindow
from engine.datatypes.local_settings import StationSettings
from engine.engine import Engine
from engine.process_model import DummyProcessModel

class Application(QtWidgets.QMainWindow):
    """ Main Application parser for Custom Application """
    
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        #self.showMaximized() # un-comment to show maximized main window
        
    def closeEvent(self, event):
        print("CLOSING APP")
        application_window.close_application()
        event.accept()


class CustomApplication():
    """ Custom application definitions. """

    def __init__(self, app_widgets, app=None):
        ''' Constructor method for custom application.'''
        if app == None:
            self.app = Application()
        self.app = app
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
        Model = DummyProcessModel()
        self.engine = Engine(sequence_process_model=Model)
        self.show_user_message('Instruments Setup')
        self.engine.pre_uut_loop()
        self.show_user_message('Instruments Ready')
        self.show_user_message('Scan Serial')
    
    def test(self):
        print('Test\n')
        serial = self.app.ui.SerialLineEdit.text()
        if serial == '':
            self.show_user_message('Invalid Serial')
        else:
            self.show_user_message('Testing')
            
            self.engine.pre_uut(serial=serial)
            self.engine.main()
            self.engine.post_uut()
            
            self.app.ui.SerialLineEdit.setText('')
            self.show_user_message('Scan Serial')
    
    def stop(self):
        self.show_user_message('Stopped')
        print('Stopped')
        self.engine.post_uut_loop()
        
    def close_application(self):
        self.stop()
        self.app.close()

# Functions

    def show_user_message(self, message: str):
        self.app.ui.UserMessageLabel.setText(message)

if __name__ == '__main__':
    app_widgets = QtWidgets.QApplication(sys.argv)
    app_widgets.setStyle('Fusion')
    app_root = Application()
    application_window = CustomApplication(app_widgets=app_widgets, app=app_root)
    sys.exit(app_widgets.exec())
