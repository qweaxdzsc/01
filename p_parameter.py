# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parameter(object):
    def setupUi(self, parameter):
        parameter.setObjectName("parameter")
        parameter.resize(768, 512)
        parameter.setMinimumSize(QtCore.QSize(768, 512))
        parameter.setMaximumSize(QtCore.QSize(768, 512))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        parameter.setFont(font)
        self.para = QtWidgets.QFrame(parameter)
        self.para.setGeometry(QtCore.QRect(30, 20, 711, 461))
        self.para.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para.setObjectName("para")
        self.pushButton_geometry = QtWidgets.QPushButton(self.para)
        self.pushButton_geometry.setGeometry(QtCore.QRect(90, 420, 121, 41))
        self.pushButton_geometry.setObjectName("pushButton_geometry")
        self.scrollArea = QtWidgets.QScrollArea(self.para)
        self.scrollArea.setGeometry(QtCore.QRect(60, 50, 144, 341))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 142, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_base = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_base.setObjectName("radioButton_base")
        self.verticalLayout.addWidget(self.radioButton_base)
        self.radioButton_fan = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_fan.setObjectName("radioButton_fan")
        self.verticalLayout.addWidget(self.radioButton_fan)
        self.radioButton_filter = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_filter.setObjectName("radioButton_filter")
        self.verticalLayout.addWidget(self.radioButton_filter)
        self.radioButton_evap = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_evap.setObjectName("radioButton_evap")
        self.verticalLayout.addWidget(self.radioButton_evap)
        self.radioButton_heater = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_heater.setObjectName("radioButton_heater")
        self.verticalLayout.addWidget(self.radioButton_heater)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.data = QtWidgets.QScrollArea(self.para)
        self.data.setGeometry(QtCore.QRect(290, 50, 371, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data.sizePolicy().hasHeightForWidth())
        self.data.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.data.setFont(font)
        self.data.setLineWidth(0)
        self.data.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.data.setWidgetResizable(True)
        self.data.setObjectName("data")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 345, 1285))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(345, 1600))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.base = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.base.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base.setObjectName("base")
        self.formLayout = QtWidgets.QFormLayout(self.base)
        self.formLayout.setContentsMargins(10, 0, 5, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.base)
        self.label_3.setMinimumSize(QtCore.QSize(140, 0))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_massflow = QtWidgets.QLineEdit(self.base)
        self.lineEdit_massflow.setObjectName("lineEdit_massflow")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_massflow)
        self.label_12 = QtWidgets.QLabel(self.base)
        self.label_12.setMinimumSize(QtCore.QSize(140, 0))
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_num = QtWidgets.QLineEdit(self.base)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_num)
        self.label_18 = QtWidgets.QLabel(self.base)
        self.label_18.setMinimumSize(QtCore.QSize(140, 0))
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_inloos = QtWidgets.QLineEdit(self.base)
        self.lineEdit_inloos.setObjectName("lineEdit_inloos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_inloos)
        self.verticalLayout_2.addWidget(self.base)
        self.fan = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.fan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan.setObjectName("fan")
        self.formLayout_42 = QtWidgets.QFormLayout(self.fan)
        self.formLayout_42.setContentsMargins(10, 0, 5, 0)
        self.formLayout_42.setObjectName("formLayout_42")
        self.label_44 = QtWidgets.QLabel(self.fan)
        self.label_44.setMinimumSize(QtCore.QSize(140, 0))
        self.label_44.setObjectName("label_44")
        self.formLayout_42.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.lineEdit_rpm = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_rpm.setObjectName("lineEdit_rpm")
        self.formLayout_42.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_rpm)
        self.label_46 = QtWidgets.QLabel(self.fan)
        self.label_46.setMinimumSize(QtCore.QSize(140, 0))
        self.label_46.setObjectName("label_46")
        self.formLayout_42.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.lineEdit_fanox = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fanox.setObjectName("lineEdit_fanox")
        self.formLayout_42.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fanox)
        self.label_43 = QtWidgets.QLabel(self.fan)
        self.label_43.setMinimumSize(QtCore.QSize(140, 0))
        self.label_43.setObjectName("label_43")
        self.formLayout_42.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.lineEdit_fanoy = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fanoy.setObjectName("lineEdit_fanoy")
        self.formLayout_42.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fanoy)
        self.label_42 = QtWidgets.QLabel(self.fan)
        self.label_42.setMinimumSize(QtCore.QSize(140, 0))
        self.label_42.setObjectName("label_42")
        self.formLayout_42.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.lineEdit_fanoz = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fanoz.setObjectName("lineEdit_fanoz")
        self.formLayout_42.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fanoz)
        self.label_45 = QtWidgets.QLabel(self.fan)
        self.label_45.setMinimumSize(QtCore.QSize(140, 0))
        self.label_45.setObjectName("label_45")
        self.formLayout_42.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.lineEdit_fandx = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fandx.setObjectName("lineEdit_fandx")
        self.formLayout_42.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fandx)
        self.label_39 = QtWidgets.QLabel(self.fan)
        self.label_39.setMinimumSize(QtCore.QSize(140, 0))
        self.label_39.setObjectName("label_39")
        self.formLayout_42.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.label_41 = QtWidgets.QLabel(self.fan)
        self.label_41.setMinimumSize(QtCore.QSize(140, 0))
        self.label_41.setObjectName("label_41")
        self.formLayout_42.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.lineEdit_fandy = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fandy.setObjectName("lineEdit_fandy")
        self.formLayout_42.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fandy)
        self.lineEdit_fandz = QtWidgets.QLineEdit(self.fan)
        self.lineEdit_fandz.setObjectName("lineEdit_fandz")
        self.formLayout_42.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fandz)
        self.verticalLayout_2.addWidget(self.fan)
        self.evap = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.evap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.evap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.evap.setObjectName("evap")
        self.formLayout_12 = QtWidgets.QFormLayout(self.evap)
        self.formLayout_12.setContentsMargins(10, 0, 5, 0)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_14 = QtWidgets.QLabel(self.evap)
        self.label_14.setMinimumSize(QtCore.QSize(140, 0))
        self.label_14.setObjectName("label_14")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_ec1 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ec1.setObjectName("lineEdit_ec1")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ec1)
        self.label_19 = QtWidgets.QLabel(self.evap)
        self.label_19.setMinimumSize(QtCore.QSize(140, 0))
        self.label_19.setObjectName("label_19")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_ec2 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ec2.setObjectName("lineEdit_ec2")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ec2)
        self.label_15 = QtWidgets.QLabel(self.evap)
        self.label_15.setMinimumSize(QtCore.QSize(140, 0))
        self.label_15.setObjectName("label_15")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_ex1 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ex1.setObjectName("lineEdit_ex1")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ex1)
        self.label_16 = QtWidgets.QLabel(self.evap)
        self.label_16.setMinimumSize(QtCore.QSize(140, 0))
        self.label_16.setObjectName("label_16")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_ey1 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ey1.setObjectName("lineEdit_ey1")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ey1)
        self.label_24 = QtWidgets.QLabel(self.evap)
        self.label_24.setMinimumSize(QtCore.QSize(140, 0))
        self.label_24.setObjectName("label_24")
        self.formLayout_12.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_ez1 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ez1.setObjectName("lineEdit_ez1")
        self.formLayout_12.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ez1)
        self.label_17 = QtWidgets.QLabel(self.evap)
        self.label_17.setMinimumSize(QtCore.QSize(140, 0))
        self.label_17.setObjectName("label_17")
        self.formLayout_12.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_ex2 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ex2.setObjectName("lineEdit_ex2")
        self.formLayout_12.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ex2)
        self.label_20 = QtWidgets.QLabel(self.evap)
        self.label_20.setMinimumSize(QtCore.QSize(140, 0))
        self.label_20.setObjectName("label_20")
        self.formLayout_12.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_ey2 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ey2.setObjectName("lineEdit_ey2")
        self.formLayout_12.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ey2)
        self.label_25 = QtWidgets.QLabel(self.evap)
        self.label_25.setMinimumSize(QtCore.QSize(140, 0))
        self.label_25.setObjectName("label_25")
        self.formLayout_12.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_ez2 = QtWidgets.QLineEdit(self.evap)
        self.lineEdit_ez2.setObjectName("lineEdit_ez2")
        self.formLayout_12.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ez2)
        self.verticalLayout_2.addWidget(self.evap)
        self.heater = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.heater.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heater.setFrameShadow(QtWidgets.QFrame.Raised)
        self.heater.setObjectName("heater")
        self.formLayout_29 = QtWidgets.QFormLayout(self.heater)
        self.formLayout_29.setContentsMargins(10, 0, 5, 0)
        self.formLayout_29.setObjectName("formLayout_29")
        self.lineEdit_hc1 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hc1.setObjectName("lineEdit_hc1")
        self.formLayout_29.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hc1)
        self.label_31 = QtWidgets.QLabel(self.heater)
        self.label_31.setMinimumSize(QtCore.QSize(140, 0))
        self.label_31.setObjectName("label_31")
        self.formLayout_29.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.label_35 = QtWidgets.QLabel(self.heater)
        self.label_35.setMinimumSize(QtCore.QSize(140, 0))
        self.label_35.setObjectName("label_35")
        self.formLayout_29.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.lineEdit_hc2 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hc2.setObjectName("lineEdit_hc2")
        self.formLayout_29.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hc2)
        self.label_37 = QtWidgets.QLabel(self.heater)
        self.label_37.setMinimumSize(QtCore.QSize(140, 0))
        self.label_37.setObjectName("label_37")
        self.formLayout_29.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.lineEdit_hx1 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hx1.setObjectName("lineEdit_hx1")
        self.formLayout_29.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hx1)
        self.label_33 = QtWidgets.QLabel(self.heater)
        self.label_33.setMinimumSize(QtCore.QSize(140, 0))
        self.label_33.setObjectName("label_33")
        self.formLayout_29.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.lineEdit_hy1 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hy1.setObjectName("lineEdit_hy1")
        self.formLayout_29.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hy1)
        self.label_36 = QtWidgets.QLabel(self.heater)
        self.label_36.setMinimumSize(QtCore.QSize(140, 0))
        self.label_36.setObjectName("label_36")
        self.formLayout_29.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.lineEdit_hz1 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hz1.setObjectName("lineEdit_hz1")
        self.formLayout_29.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hz1)
        self.label_34 = QtWidgets.QLabel(self.heater)
        self.label_34.setMinimumSize(QtCore.QSize(140, 0))
        self.label_34.setObjectName("label_34")
        self.formLayout_29.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.lineEdit_hx2 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hx2.setObjectName("lineEdit_hx2")
        self.formLayout_29.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hx2)
        self.label_32 = QtWidgets.QLabel(self.heater)
        self.label_32.setMinimumSize(QtCore.QSize(140, 0))
        self.label_32.setObjectName("label_32")
        self.formLayout_29.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.lineEdit_hy2 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hy2.setObjectName("lineEdit_hy2")
        self.formLayout_29.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hy2)
        self.label_38 = QtWidgets.QLabel(self.heater)
        self.label_38.setMinimumSize(QtCore.QSize(140, 0))
        self.label_38.setObjectName("label_38")
        self.formLayout_29.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.lineEdit_hz2 = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_hz2.setObjectName("lineEdit_hz2")
        self.formLayout_29.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_hz2)
        self.label_40 = QtWidgets.QLabel(self.heater)
        self.label_40.setMinimumSize(QtCore.QSize(140, 0))
        self.label_40.setObjectName("label_40")
        self.formLayout_29.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.lineEdit_htemp = QtWidgets.QLineEdit(self.heater)
        self.lineEdit_htemp.setObjectName("lineEdit_htemp")
        self.formLayout_29.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_htemp)
        self.verticalLayout_2.addWidget(self.heater)
        self.filter = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter.setObjectName("filter")
        self.formLayout_28 = QtWidgets.QFormLayout(self.filter)
        self.formLayout_28.setContentsMargins(10, 0, 5, 0)
        self.formLayout_28.setObjectName("formLayout_28")
        self.lineEdit_fc1 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fc1.setObjectName("lineEdit_fc1")
        self.formLayout_28.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fc1)
        self.label_30 = QtWidgets.QLabel(self.filter)
        self.label_30.setMinimumSize(QtCore.QSize(140, 0))
        self.label_30.setObjectName("label_30")
        self.formLayout_28.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.label_22 = QtWidgets.QLabel(self.filter)
        self.label_22.setMinimumSize(QtCore.QSize(140, 0))
        self.label_22.setObjectName("label_22")
        self.formLayout_28.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_fc2 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fc2.setObjectName("lineEdit_fc2")
        self.formLayout_28.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fc2)
        self.label_23 = QtWidgets.QLabel(self.filter)
        self.label_23.setMinimumSize(QtCore.QSize(140, 0))
        self.label_23.setObjectName("label_23")
        self.formLayout_28.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.lineEdit_fx1 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fx1.setObjectName("lineEdit_fx1")
        self.formLayout_28.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fx1)
        self.label_28 = QtWidgets.QLabel(self.filter)
        self.label_28.setMinimumSize(QtCore.QSize(140, 0))
        self.label_28.setObjectName("label_28")
        self.formLayout_28.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEdit_fy1 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fy1.setObjectName("lineEdit_fy1")
        self.formLayout_28.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fy1)
        self.label_29 = QtWidgets.QLabel(self.filter)
        self.label_29.setMinimumSize(QtCore.QSize(140, 0))
        self.label_29.setObjectName("label_29")
        self.formLayout_28.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.lineEdit_fz1 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fz1.setObjectName("lineEdit_fz1")
        self.formLayout_28.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fz1)
        self.label_21 = QtWidgets.QLabel(self.filter)
        self.label_21.setMinimumSize(QtCore.QSize(140, 0))
        self.label_21.setObjectName("label_21")
        self.formLayout_28.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_fx2 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fx2.setObjectName("lineEdit_fx2")
        self.formLayout_28.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fx2)
        self.label_27 = QtWidgets.QLabel(self.filter)
        self.label_27.setMinimumSize(QtCore.QSize(140, 0))
        self.label_27.setObjectName("label_27")
        self.formLayout_28.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_fy2 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fy2.setObjectName("lineEdit_fy2")
        self.formLayout_28.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fy2)
        self.label_26 = QtWidgets.QLabel(self.filter)
        self.label_26.setMinimumSize(QtCore.QSize(140, 0))
        self.label_26.setObjectName("label_26")
        self.formLayout_28.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_fz2 = QtWidgets.QLineEdit(self.filter)
        self.lineEdit_fz2.setObjectName("lineEdit_fz2")
        self.formLayout_28.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fz2)
        self.verticalLayout_2.addWidget(self.filter)
        self.data.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_import = QtWidgets.QPushButton(self.para)
        self.pushButton_import.setGeometry(QtCore.QRect(70, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.pushButton_import.setFont(font)
        self.pushButton_import.setObjectName("pushButton_import")
        self.pushButton_export = QtWidgets.QPushButton(self.para)
        self.pushButton_export.setGeometry(QtCore.QRect(540, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setObjectName("pushButton_export")
        self.pushButton_mesh = QtWidgets.QPushButton(self.para)
        self.pushButton_mesh.setGeometry(QtCore.QRect(290, 420, 121, 41))
        self.pushButton_mesh.setObjectName("pushButton_mesh")
        self.pushButton_solve = QtWidgets.QPushButton(self.para)
        self.pushButton_solve.setGeometry(QtCore.QRect(500, 420, 121, 41))
        self.pushButton_solve.setObjectName("pushButton_solve")

        self.retranslateUi(parameter)
        self.radioButton_filter.clicked.connect(self.filter.show)
        self.radioButton_fan.clicked.connect(self.fan.show)
        self.radioButton_base.clicked.connect(self.base.show)
        self.radioButton_heater.clicked.connect(self.heater.show)
        self.radioButton_evap.clicked.connect(self.evap.show)
        QtCore.QMetaObject.connectSlotsByName(parameter)

    def retranslateUi(self, parameter):
        _translate = QtCore.QCoreApplication.translate
        parameter.setWindowTitle(_translate("parameter", "Form"))
        self.pushButton_geometry.setText(_translate("parameter", "geometry"))
        self.radioButton_base.setText(_translate("parameter", "base"))
        self.radioButton_fan.setText(_translate("parameter", "fan"))
        self.radioButton_filter.setText(_translate("parameter", "filter"))
        self.radioButton_evap.setText(_translate("parameter", "evap"))
        self.radioButton_heater.setText(_translate("parameter", "heater"))
        self.label_3.setText(_translate("parameter", "massflow"))
        self.label_12.setText(_translate("parameter", "iterate_num"))
        self.label_18.setText(_translate("parameter", "inlet_loos_coef"))
        self.label_44.setText(_translate("parameter", "fan_speed"))
        self.label_46.setText(_translate("parameter", "fan_origin_x"))
        self.label_43.setText(_translate("parameter", "fan_origin_y"))
        self.label_42.setText(_translate("parameter", "fan_origin_z"))
        self.label_45.setText(_translate("parameter", "fan_dx"))
        self.label_39.setText(_translate("parameter", "fan_dy"))
        self.label_41.setText(_translate("parameter", "fan_dz"))
        self.label_14.setText(_translate("parameter", "evap_C1"))
        self.label_19.setText(_translate("parameter", "evap_C2"))
        self.label_15.setText(_translate("parameter", "evap_dx1"))
        self.label_16.setText(_translate("parameter", "evap_dy1"))
        self.label_24.setText(_translate("parameter", "evap_dz1"))
        self.label_17.setText(_translate("parameter", "evap_dx2"))
        self.label_20.setText(_translate("parameter", "evap_dy2"))
        self.label_25.setText(_translate("parameter", "evap_dz2"))
        self.label_31.setText(_translate("parameter", "heater_C1"))
        self.label_35.setText(_translate("parameter", "heater_C2"))
        self.label_37.setText(_translate("parameter", "heater_dx1"))
        self.label_33.setText(_translate("parameter", "heater_dy1"))
        self.label_36.setText(_translate("parameter", "heater_dz1"))
        self.label_34.setText(_translate("parameter", "heater_dx2"))
        self.label_32.setText(_translate("parameter", "heater_dy2"))
        self.label_38.setText(_translate("parameter", "heater_dz2"))
        self.label_40.setText(_translate("parameter", "heater_temp"))
        self.label_30.setText(_translate("parameter", "filter_C1"))
        self.label_22.setText(_translate("parameter", "filter_C2"))
        self.label_23.setText(_translate("parameter", "filter_dx1"))
        self.label_28.setText(_translate("parameter", "filter_dy1"))
        self.label_29.setText(_translate("parameter", "filter_dz1"))
        self.label_21.setText(_translate("parameter", "filter_dx2"))
        self.label_27.setText(_translate("parameter", "filter_dy2"))
        self.label_26.setText(_translate("parameter", "filter_dz2"))
        self.pushButton_import.setText(_translate("parameter", "import"))
        self.pushButton_export.setText(_translate("parameter", "export"))
        self.pushButton_mesh.setText(_translate("parameter", "mesh"))
        self.pushButton_solve.setText(_translate("parameter", "solve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_parameter()  # 这里改成你自己的项目名称，如果你没特意改过，就默认就行
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
    # new test