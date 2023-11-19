# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1366, 768)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(20, 10, 191, 51))
        self.LogoLabel.setText("")
        self.LogoLabel.setPixmap(QtGui.QPixmap(":/resources/itw.jfif"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setObjectName("LogoLabel")
        self.MainMessageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MainMessageLineEdit.setEnabled(True)
        self.MainMessageLineEdit.setGeometry(QtCore.QRect(220, 0, 951, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        self.MainMessageLineEdit.setFont(font)
        self.MainMessageLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MainMessageLineEdit.setMouseTracking(False)
        self.MainMessageLineEdit.setAcceptDrops(False)
        self.MainMessageLineEdit.setStyleSheet("background-color: orange;\n"
"/*background-color: #00723A;")
        self.MainMessageLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.MainMessageLineEdit.setReadOnly(True)
        self.MainMessageLineEdit.setClearButtonEnabled(False)
        self.MainMessageLineEdit.setObjectName("MainMessageLineEdit")
        self.TestResultsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.TestResultsTable.setGeometry(QtCore.QRect(10, 280, 751, 291))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TestResultsTable.setFont(font)
        self.TestResultsTable.setAutoFillBackground(False)
        self.TestResultsTable.setStyleSheet("QTableWidget {\n"
"    background-color: #f0f0f0; /* Color de fondo */\n"
"    alternate-background-color: #e0e0e0; /* Color de fondo alternativo para filas */\n"
"    selection-background-color: #4CAF50; /* Color de fondo de selección */\n"
"    selection-color: white; /* Color del texto de selección */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 3px; /* Espaciado interno de las celdas */\n"
"    border-bottom: 1px solid #ccc; /* Borde inferior de las celdas */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #4CAF50; /* Color de fondo de la celda seleccionada */\n"
"    color: white; /* Color del texto de la celda seleccionada */\n"
"}\n"
"\n"
"/*border: 1px solid #00723A\n"
"")
        self.TestResultsTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TestResultsTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TestResultsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TestResultsTable.setTabKeyNavigation(False)
        self.TestResultsTable.setAlternatingRowColors(True)
        self.TestResultsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TestResultsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TestResultsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TestResultsTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TestResultsTable.setShowGrid(True)
        self.TestResultsTable.setGridStyle(QtCore.Qt.NoPen)
        self.TestResultsTable.setObjectName("TestResultsTable")
        self.TestResultsTable.setColumnCount(7)
        self.TestResultsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(11, 11, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(6, item)
        self.TestResultsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.TestResultsTable.horizontalHeader().setHighlightSections(True)
        self.TestResultsTable.horizontalHeader().setStretchLastSection(True)
        self.TestResultsTable.verticalHeader().setVisible(False)
        self.TopLineLabel = QtWidgets.QLabel(self.centralwidget)
        self.TopLineLabel.setGeometry(QtCore.QRect(10, 140, 1311, 1))
        self.TopLineLabel.setStyleSheet("background-color: #0b0b0b;\n"
"/*background-color: #00723A;")
        self.TopLineLabel.setText("")
        self.TopLineLabel.setObjectName("TopLineLabel")
        self.SerialLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SerialLineEdit.setGeometry(QtCore.QRect(10, 190, 601, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SerialLineEdit.setFont(font)
        self.SerialLineEdit.setStyleSheet("border: 1px solid #0b0b0b")
        self.SerialLineEdit.setText("")
        self.SerialLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SerialLineEdit.setClearButtonEnabled(False)
        self.SerialLineEdit.setObjectName("SerialLineEdit")
        self.ProductInformationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ProductInformationLineEdit.setGeometry(QtCore.QRect(50, 915, 891, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProductInformationLineEdit.sizePolicy().hasHeightForWidth())
        self.ProductInformationLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProductInformationLineEdit.setFont(font)
        self.ProductInformationLineEdit.setStyleSheet("border: 1px solid #0b0b0b\n"
"/*border: 1px solid #00723A")
        self.ProductInformationLineEdit.setText("")
        self.ProductInformationLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductInformationLineEdit.setReadOnly(True)
        self.ProductInformationLineEdit.setObjectName("ProductInformationLineEdit")
        self.SerialNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.SerialNumberLabel.setGeometry(QtCore.QRect(10, 160, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SerialNumberLabel.setFont(font)
        self.SerialNumberLabel.setStyleSheet("color: #747474;")
        self.SerialNumberLabel.setObjectName("SerialNumberLabel")
        self.ProductInformationLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProductInformationLabel.setGeometry(QtCore.QRect(50, 880, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ProductInformationLabel.setFont(font)
        self.ProductInformationLabel.setStyleSheet("color: #747474;")
        self.ProductInformationLabel.setObjectName("ProductInformationLabel")
        self.StationNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.StationNameLabel.setGeometry(QtCore.QRect(10, 80, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.StationNameLabel.setFont(font)
        self.StationNameLabel.setStyleSheet("color: #747474;")
        self.StationNameLabel.setObjectName("StationNameLabel")
        self.TotalTestTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TotalTestTimeLineEdit.setGeometry(QtCore.QRect(390, 620, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.TotalTestTimeLineEdit.setFont(font)
        self.TotalTestTimeLineEdit.setStyleSheet("border: 1px solid #0b0b0b")
        self.TotalTestTimeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalTestTimeLineEdit.setClearButtonEnabled(False)
        self.TotalTestTimeLineEdit.setObjectName("TotalTestTimeLineEdit")
        self.TotalTestTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalTestTimeLabel.setGeometry(QtCore.QRect(170, 620, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalTestTimeLabel.setFont(font)
        self.TotalTestTimeLabel.setStyleSheet("color: #747474;")
        self.TotalTestTimeLabel.setObjectName("TotalTestTimeLabel")
        self.IPAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.IPAddressLabel.setGeometry(QtCore.QRect(50, 1010, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.IPAddressLabel.setFont(font)
        self.IPAddressLabel.setStyleSheet("")
        self.IPAddressLabel.setObjectName("IPAddressLabel")
        self.StepLabel = QtWidgets.QLabel(self.centralwidget)
        self.StepLabel.setGeometry(QtCore.QRect(50, 1030, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.StepLabel.setFont(font)
        self.StepLabel.setStyleSheet("")
        self.StepLabel.setObjectName("StepLabel")
        self.TestButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestButton.setEnabled(False)
        self.TestButton.setGeometry(QtCore.QRect(640, 190, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("color: #0b0b0b;")
        self.TestButton.setObjectName("TestButton")
        self.SerialNumberLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.SerialNumberLabel_2.setGeometry(QtCore.QRect(10, 250, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SerialNumberLabel_2.setFont(font)
        self.SerialNumberLabel_2.setStyleSheet("color: #747474;")
        self.SerialNumberLabel_2.setObjectName("SerialNumberLabel_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(780, 160, 561, 611))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 411, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.UnitsTestedByHourLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.UnitsTestedByHourLayout.setContentsMargins(0, 0, 0, 0)
        self.UnitsTestedByHourLayout.setObjectName("UnitsTestedByHourLayout")
        self.ValueYieldLabel = QtWidgets.QLabel(self.page)
        self.ValueYieldLabel.setGeometry(QtCore.QRect(40, 50, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.ValueYieldLabel.setFont(font)
        self.ValueYieldLabel.setStyleSheet("color: orange;")
        self.ValueYieldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ValueYieldLabel.setObjectName("ValueYieldLabel")
        self.YieldLabel = QtWidgets.QLabel(self.page)
        self.YieldLabel.setGeometry(QtCore.QRect(90, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.YieldLabel.setFont(font)
        self.YieldLabel.setStyleSheet("color: black;")
        self.YieldLabel.setObjectName("YieldLabel")
        self.UnitsTestedByHourLabel = QtWidgets.QLabel(self.page)
        self.UnitsTestedByHourLabel.setGeometry(QtCore.QRect(20, 310, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.UnitsTestedByHourLabel.setFont(font)
        self.UnitsTestedByHourLabel.setStyleSheet("color: #747474;")
        self.UnitsTestedByHourLabel.setObjectName("UnitsTestedByHourLabel")
        self.TopLineLabel_2 = QtWidgets.QLabel(self.page)
        self.TopLineLabel_2.setGeometry(QtCore.QRect(20, 300, 531, 1))
        self.TopLineLabel_2.setStyleSheet("background-color: #00723A;")
        self.TopLineLabel_2.setText("")
        self.TopLineLabel_2.setObjectName("TopLineLabel_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.TopLineLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.TopLineLabel_3.setGeometry(QtCore.QRect(9, 590, 751, 1))
        self.TopLineLabel_3.setStyleSheet("background-color: #0b0b0b;")
        self.TopLineLabel_3.setText("")
        self.TopLineLabel_3.setObjectName("TopLineLabel_3")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(1180, 0, 161, 71))
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
        self.StopButton.setGeometry(QtCore.QRect(600, 610, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background-color: #FFCDD2;\n"
"color: #0b0b0b;")
        self.StopButton.setObjectName("StopButton")
        self.UserMessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserMessageLabel.setGeometry(QtCore.QRect(350, 90, 691, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.UserMessageLabel.setFont(font)
        self.UserMessageLabel.setStyleSheet("color: red;")
        self.UserMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UserMessageLabel.setObjectName("UserMessageLabel")
        self.LogoLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel_2.setGeometry(QtCore.QRect(10, 570, 141, 141))
        self.LogoLabel_2.setText("")
        self.LogoLabel_2.setPixmap(QtGui.QPixmap(":/resources/smitech.jfif"))
        self.LogoLabel_2.setScaledContents(True)
        self.LogoLabel_2.setObjectName("LogoLabel_2")
        self.TotalTestTimeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.TotalTestTimeLabel_2.setGeometry(QtCore.QRect(510, 620, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalTestTimeLabel_2.setFont(font)
        self.TotalTestTimeLabel_2.setStyleSheet("color: #747474;")
        self.TotalTestTimeLabel_2.setObjectName("TotalTestTimeLabel_2")
        self.stackedWidget.raise_()
        self.MainMessageLineEdit.raise_()
        self.TestResultsTable.raise_()
        self.TopLineLabel.raise_()
        self.SerialLineEdit.raise_()
        self.ProductInformationLineEdit.raise_()
        self.SerialNumberLabel.raise_()
        self.ProductInformationLabel.raise_()
        self.StationNameLabel.raise_()
        self.TotalTestTimeLineEdit.raise_()
        self.TotalTestTimeLabel.raise_()
        self.IPAddressLabel.raise_()
        self.StepLabel.raise_()
        self.TestButton.raise_()
        self.SerialNumberLabel_2.raise_()
        self.StartButton.raise_()
        self.StopButton.raise_()
        self.UserMessageLabel.raise_()
        self.LogoLabel.raise_()
        self.LogoLabel_2.raise_()
        self.TopLineLabel_3.raise_()
        self.TotalTestTimeLabel_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuMaintenance = QtWidgets.QMenu(self.menubar)
        self.menuMaintenance.setObjectName("menuMaintenance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDevicesList = QtWidgets.QAction(MainWindow)
        self.actionDevicesList.setObjectName("actionDevicesList")
        self.menuMaintenance.addAction(self.actionDevicesList)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuMaintenance.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Solution"))
        self.MainMessageLineEdit.setText(_translate("MainWindow", "PRESIONA INICIAR"))
        self.TestResultsTable.setSortingEnabled(True)
        item = self.TestResultsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test Name"))
        item = self.TestResultsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Low Limit"))
        item = self.TestResultsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "High Limit"))
        item = self.TestResultsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Measure"))
        item = self.TestResultsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Unit"))
        item = self.TestResultsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Result"))
        item = self.TestResultsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Time"))
        self.SerialNumberLabel.setText(_translate("MainWindow", "Numero de Serie"))
        self.ProductInformationLabel.setText(_translate("MainWindow", "Part Number:"))
        self.StationNameLabel.setText(_translate("MainWindow", "CELL-1"))
        self.TotalTestTimeLineEdit.setText(_translate("MainWindow", "00:06"))
        self.TotalTestTimeLabel.setText(_translate("MainWindow", "Tiempo de Prueba:"))
        self.IPAddressLabel.setText(_translate("MainWindow", "10.49.72.192"))
        self.StepLabel.setText(_translate("MainWindow", "Idle"))
        self.TestButton.setText(_translate("MainWindow", "Test"))
        self.SerialNumberLabel_2.setText(_translate("MainWindow", "Resultados"))
        self.ValueYieldLabel.setText(_translate("MainWindow", "90"))
        self.YieldLabel.setText(_translate("MainWindow", "Yield"))
        self.UnitsTestedByHourLabel.setText(_translate("MainWindow", "Units Tested By Hour:"))
        self.StartButton.setText(_translate("MainWindow", "Inicializar"))
        self.StopButton.setText(_translate("MainWindow", "Cerrar"))
        self.UserMessageLabel.setText(_translate("MainWindow", "PRUEBA DE RESISTENCIA"))
        self.TotalTestTimeLabel_2.setText(_translate("MainWindow", "seg."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuMaintenance.setTitle(_translate("MainWindow", "Maintenance"))
        self.actionDevicesList.setText(_translate("MainWindow", "Devices List"))
import resources.resources
