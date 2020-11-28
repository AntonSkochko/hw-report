# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/layouts/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 481, 441))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.main_menu = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.main_menu.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_menu.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.main_menu.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.main_menu.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.main_menu.setFormAlignment(QtCore.Qt.AlignCenter)
        self.main_menu.setContentsMargins(9, 0, 55, 0)
        self.main_menu.setSpacing(50)
        self.main_menu.setObjectName("main_menu")
        self.storage_button = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storage_button.sizePolicy().hasHeightForWidth())
        self.storage_button.setSizePolicy(sizePolicy)
        self.storage_button.setMinimumSize(QtCore.QSize(100, 100))
        self.storage_button.setMaximumSize(QtCore.QSize(200, 100))
        self.storage_button.setObjectName("storage_button")
        self.main_menu.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.storage_button)
        self.gpu_button = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpu_button.sizePolicy().hasHeightForWidth())
        self.gpu_button.setSizePolicy(sizePolicy)
        self.gpu_button.setMinimumSize(QtCore.QSize(100, 100))
        self.gpu_button.setMaximumSize(QtCore.QSize(200, 100))
        self.gpu_button.setDefault(False)
        self.gpu_button.setObjectName("gpu_button")
        self.main_menu.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gpu_button)
        self.other_button = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_button.sizePolicy().hasHeightForWidth())
        self.other_button.setSizePolicy(sizePolicy)
        self.other_button.setMinimumSize(QtCore.QSize(100, 100))
        self.other_button.setMaximumSize(QtCore.QSize(200, 100))
        self.other_button.setObjectName("other_button")
        self.main_menu.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.other_button)
        self.cpu_button = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_button.sizePolicy().hasHeightForWidth())
        self.cpu_button.setSizePolicy(sizePolicy)
        self.cpu_button.setMinimumSize(QtCore.QSize(100, 100))
        self.cpu_button.setMaximumSize(QtCore.QSize(200, 100))
        self.cpu_button.setObjectName("cpu_button")
        self.main_menu.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cpu_button)
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.back_button.setObjectName("back_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.storage_button.setText(_translate("MainWindow", "Storage"))
        self.gpu_button.setText(_translate("MainWindow", "GPU"))
        self.other_button.setText(_translate("MainWindow", "Other"))
        self.cpu_button.setText(_translate("MainWindow", "CPU"))
        self.back_button.setText(_translate("MainWindow", "<-"))
