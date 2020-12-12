# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/gui/layouts/gpu_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(475, 417)
        self.verticalWidget_2 = QtWidgets.QWidget(Form)
        self.verticalWidget_2.setGeometry(QtCore.QRect(10, 10, 451, 391))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.gpu_layout = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.gpu_layout.setContentsMargins(0, 0, 0, 0)
        self.gpu_layout.setObjectName("gpu_layout")
        self.name_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.name_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.name_label.setObjectName("name_label")
        self.gpu_layout.addWidget(self.name_label)
        self.name_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.name_field.setFrame(True)
        self.name_field.setReadOnly(True)
        self.name_field.setObjectName("name_field")
        self.gpu_layout.addWidget(self.name_field)
        self.driver_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.driver_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.driver_label.setObjectName("driver_label")
        self.gpu_layout.addWidget(self.driver_label)
        self.driver_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.driver_field.setFrame(True)
        self.driver_field.setReadOnly(True)
        self.driver_field.setObjectName("driver_field")
        self.gpu_layout.addWidget(self.driver_field)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.memory_util_box = QtWidgets.QVBoxLayout()
        self.memory_util_box.setObjectName("memory_util_box")
        self.memory_util_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.memory_util_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.memory_util_label.setObjectName("memory_util_label")
        self.memory_util_box.addWidget(self.memory_util_label)
        self.memory_util_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.memory_util_field.setReadOnly(True)
        self.memory_util_field.setObjectName("memory_util_field")
        self.memory_util_box.addWidget(self.memory_util_field)
        self.horizontalLayout.addLayout(self.memory_util_box)
        self.gpu_util_box = QtWidgets.QVBoxLayout()
        self.gpu_util_box.setObjectName("gpu_util_box")
        self.gpu_util_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.gpu_util_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.gpu_util_label.setObjectName("gpu_util_label")
        self.gpu_util_box.addWidget(self.gpu_util_label)
        self.gpu_util_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.gpu_util_field.setReadOnly(True)
        self.gpu_util_field.setObjectName("gpu_util_field")
        self.gpu_util_box.addWidget(self.gpu_util_field)
        self.horizontalLayout.addLayout(self.gpu_util_box)
        self.gpu_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.memory_total_box = QtWidgets.QVBoxLayout()
        self.memory_total_box.setObjectName("memory_total_box")
        self.memory_total_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.memory_total_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.memory_total_label.setObjectName("memory_total_label")
        self.memory_total_box.addWidget(self.memory_total_label)
        self.memory_total_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.memory_total_field.setReadOnly(True)
        self.memory_total_field.setObjectName("memory_total_field")
        self.memory_total_box.addWidget(self.memory_total_field)
        self.horizontalLayout_2.addLayout(self.memory_total_box)
        self.memory_used_box = QtWidgets.QVBoxLayout()
        self.memory_used_box.setObjectName("memory_used_box")
        self.memory_used_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.memory_used_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.memory_used_label.setObjectName("memory_used_label")
        self.memory_used_box.addWidget(self.memory_used_label)
        self.memory_used_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.memory_used_field.setReadOnly(True)
        self.memory_used_field.setObjectName("memory_used_field")
        self.memory_used_box.addWidget(self.memory_used_field)
        self.horizontalLayout_2.addLayout(self.memory_used_box)
        self.gpu_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.temp_gpu_box = QtWidgets.QVBoxLayout()
        self.temp_gpu_box.setObjectName("temp_gpu_box")
        self.temp_gpu_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.temp_gpu_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.temp_gpu_label.setObjectName("temp_gpu_label")
        self.temp_gpu_box.addWidget(self.temp_gpu_label)
        self.temp_gpu_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.temp_gpu_field.setReadOnly(True)
        self.temp_gpu_field.setObjectName("temp_gpu_field")
        self.temp_gpu_box.addWidget(self.temp_gpu_field)
        self.horizontalLayout_3.addLayout(self.temp_gpu_box)
        self.temp_mem_box = QtWidgets.QVBoxLayout()
        self.temp_mem_box.setObjectName("temp_mem_box")
        self.temp_mem_label = QtWidgets.QLabel(self.verticalWidget_2)
        self.temp_mem_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.temp_mem_label.setObjectName("temp_mem_label")
        self.temp_mem_box.addWidget(self.temp_mem_label)
        self.temp_mem_field = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.temp_mem_field.setReadOnly(True)
        self.temp_mem_field.setObjectName("temp_mem_field")
        self.temp_mem_box.addWidget(self.temp_mem_field)
        self.horizontalLayout_3.addLayout(self.temp_mem_box)
        self.gpu_layout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_label.setText(_translate("Form", "GPU Name"))
        self.driver_label.setText(_translate("Form", "Driver Version"))
        self.memory_util_label.setText(_translate("Form", "Memory Utilization, %"))
        self.gpu_util_label.setText(_translate("Form", "GPU Utilization, %"))
        self.memory_total_label.setText(_translate("Form", "Total Memory, MiB"))
        self.memory_used_label.setText(_translate("Form", "Used Memory, MiB"))
        self.temp_gpu_label.setText(_translate("Form", "GPU Temperature, C"))
        self.temp_mem_label.setText(_translate("Form", "Memory Temperature, C"))