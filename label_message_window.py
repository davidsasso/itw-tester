# Native Imports
from PyQt5.QtGui import QPixmap
from datetime import date, datetime,timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
import time
import sys

# Custom Imports
from ui.label_message import Ui_MainWindow


class SecondaryApplication(QtWidgets.QMainWindow):
    """ Main Application parser for Custom Application """
    
    
    def __init__(self, custom_ui):
        super(SecondaryApplication, self).__init__()
        self.ui = custom_ui()
        self.ui.setupUi(self)
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        #self.showMaximized() # un-comment to show maximized main window
        
    def closeEvent(self, event):
        print("App Closed")
        #application_window.close_application()
        event.accept()


class SecondaryCustomApplication():
    """ Custom application definitions. """

    def __init__(self, app_widgets, app=None):
        ''' Constructor method for custom application.'''
        if app == None:
            self.app = SecondaryApplication()
        self.app = app
        self.app.show()
        QApplication.processEvents()
        self.wait_to_close(timeout=3)

    def wait_to_close(self, timeout: int):
        start_time = time.time()

        while time.time() - start_time < timeout:
            # Do nothing or perform other tasks while waiting
            pass

        # Call the function you want to execute after waiting
        self.stop()
    
    def stop(self):
        self.close_application()
        
    def close_application(self):
        try:
            self.app.close()
        except:
            pass

if __name__ == '__main__':
    app_widgets = QtWidgets.QApplication(sys.argv)
    app_widgets.setStyle('Fusion')
    app_root = SecondaryApplication(Ui_MainWindow)
    application_window = SecondaryCustomApplication(app_widgets=app_widgets, app=app_root)
    sys.exit(app_widgets.exec())
