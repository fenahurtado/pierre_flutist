# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_up_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(444, 475)
        Form.setStyleSheet("QWidget {\n"
"        background-color: #BDBDD7;\n"
"    }")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 14, 1, 1, 1)
        self.fingersCheck = QtWidgets.QCheckBox(Form)
        self.fingersCheck.setEnabled(False)
        self.fingersCheck.setCheckable(True)
        self.fingersCheck.setChecked(False)
        self.fingersCheck.setObjectName("fingersCheck")
        self.gridLayout.addWidget(self.fingersCheck, 13, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"        border: 2px solid grey;\n"
"        border-radius: 5px;\n"
"        background-color: #f0f0f0;\n"
"        height: 20px;\n"
"        text-align: center;\n"
"    }\n"
"    \n"
"    QProgressBar::chunk {\n"
"        background-color: #00C853;\n"
"        width: 20px;\n"
"    }")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.flowCheck = QtWidgets.QCheckBox(Form)
        self.flowCheck.setEnabled(False)
        self.flowCheck.setCheckable(True)
        self.flowCheck.setChecked(False)
        self.flowCheck.setObjectName("flowCheck")
        self.gridLayout.addWidget(self.flowCheck, 11, 0, 1, 3)
        self.ZCheck = QtWidgets.QCheckBox(Form)
        self.ZCheck.setEnabled(False)
        self.ZCheck.setCheckable(True)
        self.ZCheck.setChecked(False)
        self.ZCheck.setObjectName("ZCheck")
        self.gridLayout.addWidget(self.ZCheck, 7, 0, 1, 3)
        self.pressureCheck = QtWidgets.QCheckBox(Form)
        self.pressureCheck.setEnabled(False)
        self.pressureCheck.setCheckable(True)
        self.pressureCheck.setChecked(False)
        self.pressureCheck.setObjectName("pressureCheck")
        self.gridLayout.addWidget(self.pressureCheck, 12, 0, 1, 3)
        self.microphoneCheck = QtWidgets.QCheckBox(Form)
        self.microphoneCheck.setEnabled(False)
        self.microphoneCheck.setCheckable(True)
        self.microphoneCheck.setChecked(False)
        self.microphoneCheck.setObjectName("microphoneCheck")
        self.gridLayout.addWidget(self.microphoneCheck, 10, 0, 1, 3)
        self.XCheck = QtWidgets.QCheckBox(Form)
        self.XCheck.setEnabled(False)
        self.XCheck.setCheckable(True)
        self.XCheck.setChecked(False)
        self.XCheck.setObjectName("XCheck")
        self.gridLayout.addWidget(self.XCheck, 6, 0, 1, 3)
        self.AlphaCheck = QtWidgets.QCheckBox(Form)
        self.AlphaCheck.setEnabled(False)
        self.AlphaCheck.setCheckable(True)
        self.AlphaCheck.setChecked(False)
        self.AlphaCheck.setObjectName("AlphaCheck")
        self.gridLayout.addWidget(self.AlphaCheck, 8, 0, 1, 3)
        self.instancesCheck = QtWidgets.QCheckBox(Form)
        self.instancesCheck.setEnabled(False)
        self.instancesCheck.setCheckable(True)
        self.instancesCheck.setChecked(False)
        self.instancesCheck.setObjectName("instancesCheck")
        self.gridLayout.addWidget(self.instancesCheck, 4, 0, 1, 3)
        self.memoryCheck = QtWidgets.QCheckBox(Form)
        self.memoryCheck.setEnabled(False)
        self.memoryCheck.setCheckable(True)
        self.memoryCheck.setChecked(False)
        self.memoryCheck.setObjectName("memoryCheck")
        self.gridLayout.addWidget(self.memoryCheck, 5, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fingersCheck.setText(_translate("Form", "Waiting fingers driver..."))
        self.label.setText(_translate("Form", "Loading..."))
        self.flowCheck.setText(_translate("Form", "Waiting flow driver..."))
        self.ZCheck.setText(_translate("Form", "Waiting Z driver..."))
        self.pressureCheck.setText(_translate("Form", "Waiting pressure driver..."))
        self.microphoneCheck.setText(_translate("Form", "Waiting microphone..."))
        self.XCheck.setText(_translate("Form", "Waiting X driver..."))
        self.AlphaCheck.setText(_translate("Form", "Waiting Alpha driver..."))
        self.instancesCheck.setText(_translate("Form", "Instances created..."))
        self.memoryCheck.setText(_translate("Form", "Creating Memory..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
