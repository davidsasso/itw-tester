# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part_number_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 664)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(320, 250, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 250, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/resources/QR.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(40, 20, 171, 61))
        self.LogoLabel.setText("")
        self.LogoLabel.setPixmap(QtGui.QPixmap(":/resources/itw.jfif"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setObjectName("LogoLabel")
        self.StationNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.StationNameLabel.setGeometry(QtCore.QRect(270, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.StationNameLabel.setFont(font)
        self.StationNameLabel.setStyleSheet("color: #747474;")
        self.StationNameLabel.setObjectName("StationNameLabel")
        self.UserMessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserMessageLabel.setGeometry(QtCore.QRect(150, 100, 561, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.UserMessageLabel.setFont(font)
        self.UserMessageLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.UserMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UserMessageLabel.setObjectName("UserMessageLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.UserMessageLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.UserMessageLabel_2.setGeometry(QtCore.QRect(20, 170, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.UserMessageLabel_2.setFont(font)
        self.UserMessageLabel_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.UserMessageLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.UserMessageLabel_2.setObjectName("UserMessageLabel_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 340, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 420, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 490, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 490, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(40, 570, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: #ABF7B1;\n"
"color: #0b0b0b;")
        self.StartButton.setObjectName("StartButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setEnabled(False)
        self.StopButton.setGeometry(QtCore.QRect(220, 570, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background-color: #FFCDD2;\n"
"color: #0b0b0b;")
        self.StopButton.setObjectName("StopButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(490, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message"))
        self.label.setText(_translate("MainWindow", "Escanea QR:"))
        self.StationNameLabel.setText(_translate("MainWindow", "Tester Configuracion "))
        self.UserMessageLabel.setText(_translate("MainWindow", "Por favor rellene los siguientes campos"))
        self.UserMessageLabel_2.setText(_translate("MainWindow", "Numero de orden "))
        self.label_3.setText(_translate("MainWindow", "Modelo:"))
        self.label_4.setText(_translate("MainWindow", "Limites de  resistencia:"))
        self.label_7.setText(_translate("MainWindow", "Cantidad de piezas:"))
        self.StartButton.setText(_translate("MainWindow", "Aceptar"))
        self.StopButton.setText(_translate("MainWindow", "Reiniciar"))
        self.label_9.setText(_translate("MainWindow", "Fecha:"))
import resources.resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
