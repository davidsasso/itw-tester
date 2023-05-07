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
        MainWindow.resize(1920, 1017)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(50, 40, 411, 61))
        self.LogoLabel.setText("")
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setObjectName("LogoLabel")
        self.MainMessageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MainMessageLineEdit.setEnabled(True)
        self.MainMessageLineEdit.setGeometry(QtCore.QRect(510, 40, 951, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        self.MainMessageLineEdit.setFont(font)
        self.MainMessageLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MainMessageLineEdit.setMouseTracking(False)
        self.MainMessageLineEdit.setAcceptDrops(False)
        self.MainMessageLineEdit.setStyleSheet("background-color: #00723A;")
        self.MainMessageLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.MainMessageLineEdit.setReadOnly(True)
        self.MainMessageLineEdit.setClearButtonEnabled(False)
        self.MainMessageLineEdit.setObjectName("MainMessageLineEdit")
        self.TestResultsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.TestResultsTable.setGeometry(QtCore.QRect(80, 360, 891, 501))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TestResultsTable.setFont(font)
        self.TestResultsTable.setAutoFillBackground(False)
        self.TestResultsTable.setStyleSheet("border: 1px solid #00723A")
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
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
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TestResultsTable.setHorizontalHeaderItem(6, item)
        self.TestResultsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.TestResultsTable.horizontalHeader().setStretchLastSection(True)
        self.TestResultsTable.verticalHeader().setVisible(False)
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(1660, 50, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("color: #00723A;")
        self.StartButton.setObjectName("StartButton")
        self.TopLineLabel = QtWidgets.QLabel(self.centralwidget)
        self.TopLineLabel.setGeometry(QtCore.QRect(50, 170, 1801, 1))
        self.TopLineLabel.setStyleSheet("background-color: #00723A;")
        self.TopLineLabel.setText("")
        self.TopLineLabel.setObjectName("TopLineLabel")
        self.SerialLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SerialLineEdit.setGeometry(QtCore.QRect(80, 215, 761, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SerialLineEdit.setFont(font)
        self.SerialLineEdit.setStyleSheet("border: 1px solid #00723A")
        self.SerialLineEdit.setText("")
        self.SerialLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SerialLineEdit.setClearButtonEnabled(False)
        self.SerialLineEdit.setObjectName("SerialLineEdit")
        self.ProductInformationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ProductInformationLineEdit.setGeometry(QtCore.QRect(80, 275, 891, 71))
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
        self.ProductInformationLineEdit.setStyleSheet("border: 1px solid #00723A")
        self.ProductInformationLineEdit.setText("")
        self.ProductInformationLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductInformationLineEdit.setReadOnly(True)
        self.ProductInformationLineEdit.setObjectName("ProductInformationLineEdit")
        self.SerialNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.SerialNumberLabel.setGeometry(QtCore.QRect(80, 190, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SerialNumberLabel.setFont(font)
        self.SerialNumberLabel.setStyleSheet("color: #747474;")
        self.SerialNumberLabel.setObjectName("SerialNumberLabel")
        self.ProductInformationLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProductInformationLabel.setGeometry(QtCore.QRect(80, 250, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ProductInformationLabel.setFont(font)
        self.ProductInformationLabel.setStyleSheet("color: #747474;")
        self.ProductInformationLabel.setObjectName("ProductInformationLabel")
        self.StationNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.StationNameLabel.setGeometry(QtCore.QRect(60, 120, 561, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.StationNameLabel.setFont(font)
        self.StationNameLabel.setStyleSheet("color: #747474;")
        self.StationNameLabel.setObjectName("StationNameLabel")
        self.UserMessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserMessageLabel.setGeometry(QtCore.QRect(650, 120, 691, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.UserMessageLabel.setFont(font)
        self.UserMessageLabel.setStyleSheet("color: red;")
        self.UserMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UserMessageLabel.setObjectName("UserMessageLabel")
        self.TotalTestTimeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TotalTestTimeLineEdit.setGeometry(QtCore.QRect(740, 890, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.TotalTestTimeLineEdit.setFont(font)
        self.TotalTestTimeLineEdit.setStyleSheet("border: 1px solid #00723A")
        self.TotalTestTimeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalTestTimeLineEdit.setClearButtonEnabled(False)
        self.TotalTestTimeLineEdit.setObjectName("TotalTestTimeLineEdit")
        self.TotalTestTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TotalTestTimeLabel.setGeometry(QtCore.QRect(590, 890, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalTestTimeLabel.setFont(font)
        self.TotalTestTimeLabel.setStyleSheet("color: #747474;")
        self.TotalTestTimeLabel.setObjectName("TotalTestTimeLabel")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(860, 880, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("color: #00723A;")
        self.StopButton.setObjectName("StopButton")
        self.TopLineLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.TopLineLabel_2.setGeometry(QtCore.QRect(990, 640, 871, 1))
        self.TopLineLabel_2.setStyleSheet("background-color: #00723A;")
        self.TopLineLabel_2.setText("")
        self.TopLineLabel_2.setObjectName("TopLineLabel_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1000, 690, 841, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.UnitsTestedByHourLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.UnitsTestedByHourLayout.setContentsMargins(0, 0, 0, 0)
        self.UnitsTestedByHourLayout.setObjectName("UnitsTestedByHourLayout")
        self.UnitsTestedByHourLabel = QtWidgets.QLabel(self.centralwidget)
        self.UnitsTestedByHourLabel.setGeometry(QtCore.QRect(1000, 650, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.UnitsTestedByHourLabel.setFont(font)
        self.UnitsTestedByHourLabel.setStyleSheet("color: #747474;")
        self.UnitsTestedByHourLabel.setObjectName("UnitsTestedByHourLabel")
        self.TopFailuresLabel = QtWidgets.QLabel(self.centralwidget)
        self.TopFailuresLabel.setGeometry(QtCore.QRect(1080, 420, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TopFailuresLabel.setFont(font)
        self.TopFailuresLabel.setStyleSheet("color: #747474;")
        self.TopFailuresLabel.setObjectName("TopFailuresLabel")
        self.HourlyYieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.HourlyYieldLabel.setGeometry(QtCore.QRect(1420, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.HourlyYieldLabel.setFont(font)
        self.HourlyYieldLabel.setStyleSheet("color: #747474;")
        self.HourlyYieldLabel.setObjectName("HourlyYieldLabel")
        self.YieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.YieldLabel.setGeometry(QtCore.QRect(1090, 210, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.YieldLabel.setFont(font)
        self.YieldLabel.setStyleSheet("color: black;")
        self.YieldLabel.setObjectName("YieldLabel")
        self.ValueYieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.ValueYieldLabel.setGeometry(QtCore.QRect(1030, 250, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.ValueYieldLabel.setFont(font)
        self.ValueYieldLabel.setStyleSheet("color: orange;")
        self.ValueYieldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ValueYieldLabel.setObjectName("ValueYieldLabel")
        self.TopFailuresTable = QtWidgets.QTableWidget(self.centralwidget)
        self.TopFailuresTable.setGeometry(QtCore.QRect(1000, 450, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TopFailuresTable.setFont(font)
        self.TopFailuresTable.setAutoFillBackground(False)
        self.TopFailuresTable.setStyleSheet("border: 1px solid #00723A")
        self.TopFailuresTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFailuresTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TopFailuresTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TopFailuresTable.setTabKeyNavigation(False)
        self.TopFailuresTable.setAlternatingRowColors(True)
        self.TopFailuresTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TopFailuresTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TopFailuresTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TopFailuresTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TopFailuresTable.setShowGrid(True)
        self.TopFailuresTable.setGridStyle(QtCore.Qt.NoPen)
        self.TopFailuresTable.setObjectName("TopFailuresTable")
        self.TopFailuresTable.setColumnCount(2)
        self.TopFailuresTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TopFailuresTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 114, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.TopFailuresTable.setHorizontalHeaderItem(1, item)
        self.TopFailuresTable.horizontalHeader().setCascadingSectionResizes(False)
        self.TopFailuresTable.horizontalHeader().setStretchLastSection(True)
        self.TopFailuresTable.verticalHeader().setVisible(False)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1320, 250, 501, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.HourlyYieldLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.HourlyYieldLayout.setContentsMargins(0, 0, 0, 0)
        self.HourlyYieldLayout.setObjectName("HourlyYieldLayout")
        self.DomainLabel = QtWidgets.QLabel(self.centralwidget)
        self.DomainLabel.setGeometry(QtCore.QRect(80, 870, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.DomainLabel.setFont(font)
        self.DomainLabel.setStyleSheet("")
        self.DomainLabel.setObjectName("DomainLabel")
        self.IPAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.IPAddressLabel.setGeometry(QtCore.QRect(80, 890, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.IPAddressLabel.setFont(font)
        self.IPAddressLabel.setStyleSheet("")
        self.IPAddressLabel.setObjectName("IPAddressLabel")
        self.StepLabel = QtWidgets.QLabel(self.centralwidget)
        self.StepLabel.setGeometry(QtCore.QRect(80, 910, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.StepLabel.setFont(font)
        self.StepLabel.setStyleSheet("")
        self.StepLabel.setObjectName("StepLabel")
        self.TestButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestButton.setGeometry(QtCore.QRect(850, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TestButton.setFont(font)
        self.TestButton.setStyleSheet("color: #00723A;")
        self.TestButton.setObjectName("TestButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuMaintenance.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Solution"))
        self.MainMessageLineEdit.setText(_translate("MainWindow", "PASS"))
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
        self.StartButton.setText(_translate("MainWindow", "Start Test"))
        self.SerialNumberLabel.setText(_translate("MainWindow", "Serial Number"))
        self.ProductInformationLabel.setText(_translate("MainWindow", "Product Information"))
        self.StationNameLabel.setText(_translate("MainWindow", "STATION_NAME"))
        self.UserMessageLabel.setText(_translate("MainWindow", "Test Solution"))
        self.TotalTestTimeLineEdit.setText(_translate("MainWindow", "00:06"))
        self.TotalTestTimeLabel.setText(_translate("MainWindow", "Total Test Time"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.UnitsTestedByHourLabel.setText(_translate("MainWindow", "Units Tested By Hour"))
        self.TopFailuresLabel.setText(_translate("MainWindow", "Top 5 Failures"))
        self.HourlyYieldLabel.setText(_translate("MainWindow", "Hourly Yield"))
        self.YieldLabel.setText(_translate("MainWindow", "Yield"))
        self.ValueYieldLabel.setText(_translate("MainWindow", "73"))
        self.TopFailuresTable.setSortingEnabled(True)
        item = self.TopFailuresTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test"))
        item = self.TopFailuresTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Qty"))
        self.DomainLabel.setText(_translate("MainWindow", "-----------------------"))
        self.IPAddressLabel.setText(_translate("MainWindow", "10.49.72.192"))
        self.StepLabel.setText(_translate("MainWindow", "Idle"))
        self.TestButton.setText(_translate("MainWindow", "Test"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuMaintenance.setTitle(_translate("MainWindow", "Maintenance"))
import resources.resources