# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sat Mar 13 18:07:21 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(257, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings_Dialog.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(Settings_Dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(Settings_Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_inputDevice = QtGui.QComboBox(Settings_Dialog)
        self.comboBox_inputDevice.setObjectName("comboBox_inputDevice")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_inputDevice)
        self.label_2 = QtGui.QLabel(Settings_Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_freqscale = QtGui.QComboBox(Settings_Dialog)
        self.comboBox_freqscale.setObjectName("comboBox_freqscale")
        self.comboBox_freqscale.addItem(QtCore.QString())
        self.comboBox_freqscale.addItem(QtCore.QString())
        self.comboBox_freqscale.addItem(QtCore.QString())
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_freqscale)
        self.label = QtGui.QLabel(Settings_Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_fftsize = QtGui.QComboBox(Settings_Dialog)
        self.comboBox_fftsize.setObjectName("comboBox_fftsize")
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_fftsize)
        self.label_5 = QtGui.QLabel(Settings_Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox_specmin = QtGui.QSpinBox(Settings_Dialog)
        self.spinBox_specmin.setKeyboardTracking(False)
        self.spinBox_specmin.setMinimum(-200)
        self.spinBox_specmin.setMaximum(200)
        self.spinBox_specmin.setProperty("value", QtCore.QVariant(-100))
        self.spinBox_specmin.setObjectName("spinBox_specmin")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox_specmin)
        self.label_6 = QtGui.QLabel(Settings_Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.spinBox_specmax = QtGui.QSpinBox(Settings_Dialog)
        self.spinBox_specmax.setKeyboardTracking(False)
        self.spinBox_specmax.setMinimum(-200)
        self.spinBox_specmax.setMaximum(200)
        self.spinBox_specmax.setProperty("value", QtCore.QVariant(-20))
        self.spinBox_specmax.setObjectName("spinBox_specmax")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBox_specmax)
        self.label_4 = QtGui.QLabel(Settings_Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBox_timerange = QtGui.QDoubleSpinBox(Settings_Dialog)
        self.doubleSpinBox_timerange.setDecimals(1)
        self.doubleSpinBox_timerange.setMinimum(0.1)
        self.doubleSpinBox_timerange.setMaximum(1000.0)
        self.doubleSpinBox_timerange.setProperty("value", QtCore.QVariant(10.0))
        self.doubleSpinBox_timerange.setObjectName("doubleSpinBox_timerange")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.doubleSpinBox_timerange)
        self.label_7 = QtGui.QLabel(Settings_Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.spinBox_minfreq = QtGui.QSpinBox(Settings_Dialog)
        self.spinBox_minfreq.setMinimum(20)
        self.spinBox_minfreq.setMaximum(20000)
        self.spinBox_minfreq.setSingleStep(10)
        self.spinBox_minfreq.setObjectName("spinBox_minfreq")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.spinBox_minfreq)
        self.label_8 = QtGui.QLabel(Settings_Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.spinBox_maxfreq = QtGui.QSpinBox(Settings_Dialog)
        self.spinBox_maxfreq.setMinimum(20)
        self.spinBox_maxfreq.setMaximum(20000)
        self.spinBox_maxfreq.setSingleStep(1000)
        self.spinBox_maxfreq.setProperty("value", QtCore.QVariant(20000))
        self.spinBox_maxfreq.setObjectName("spinBox_maxfreq")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.spinBox_maxfreq)

        self.retranslateUi(Settings_Dialog)
        self.comboBox_fftsize.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QtGui.QApplication.translate("Settings_Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Settings_Dialog", "Sound input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings_Dialog", "Frequency scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_freqscale.setItemText(0, QtGui.QApplication.translate("Settings_Dialog", "Linear", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_freqscale.setItemText(1, QtGui.QApplication.translate("Settings_Dialog", "Logarithmic", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_freqscale.setItemText(2, QtGui.QApplication.translate("Settings_Dialog", "Logarithmic base 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings_Dialog", "FFT Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(0, QtGui.QApplication.translate("Settings_Dialog", "32 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(1, QtGui.QApplication.translate("Settings_Dialog", "64 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(2, QtGui.QApplication.translate("Settings_Dialog", "128 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(3, QtGui.QApplication.translate("Settings_Dialog", "256 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(4, QtGui.QApplication.translate("Settings_Dialog", "512 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(5, QtGui.QApplication.translate("Settings_Dialog", "1024 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(6, QtGui.QApplication.translate("Settings_Dialog", "2048 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(7, QtGui.QApplication.translate("Settings_Dialog", "4096 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(8, QtGui.QApplication.translate("Settings_Dialog", "8192 points", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(9, QtGui.QApplication.translate("Settings_Dialog", "16384 points", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Settings_Dialog", "Min color", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_specmin.setSuffix(QtGui.QApplication.translate("Settings_Dialog", " dB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Settings_Dialog", "Max color", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_specmax.setSuffix(QtGui.QApplication.translate("Settings_Dialog", " dB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Settings_Dialog", "Time range", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBox_timerange.setSuffix(QtGui.QApplication.translate("Settings_Dialog", " s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Settings_Dialog", "Min frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_minfreq.setSuffix(QtGui.QApplication.translate("Settings_Dialog", " Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Settings_Dialog", "Max frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox_maxfreq.setSuffix(QtGui.QApplication.translate("Settings_Dialog", " Hz", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
