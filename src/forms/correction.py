# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'correction.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 264)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.notes_dis = QtWidgets.QSpinBox(Dialog)
        self.notes_dis.setMinimum(-10)
        self.notes_dis.setMaximum(10)
        self.notes_dis.setObjectName("notes_dis")
        self.gridLayout.addWidget(self.notes_dis, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.flow_dis = QtWidgets.QDoubleSpinBox(Dialog)
        self.flow_dis.setMinimum(-20.0)
        self.flow_dis.setMaximum(20.0)
        self.flow_dis.setObjectName("flow_dis")
        self.gridLayout.addWidget(self.flow_dis, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.theta_dis = QtWidgets.QDoubleSpinBox(Dialog)
        self.theta_dis.setMinimum(-20.0)
        self.theta_dis.setMaximum(20.0)
        self.theta_dis.setObjectName("theta_dis")
        self.gridLayout.addWidget(self.theta_dis, 1, 1, 1, 1)
        self.r_dis = QtWidgets.QDoubleSpinBox(Dialog)
        self.r_dis.setMinimum(-20.0)
        self.r_dis.setMaximum(20.0)
        self.r_dis.setObjectName("r_dis")
        self.gridLayout.addWidget(self.r_dis, 0, 1, 1, 1)
        self.offset_dis = QtWidgets.QDoubleSpinBox(Dialog)
        self.offset_dis.setMinimum(-20.0)
        self.offset_dis.setMaximum(20.0)
        self.offset_dis.setObjectName("offset_dis")
        self.gridLayout.addWidget(self.offset_dis, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.leadDelayR = QtWidgets.QDoubleSpinBox(Dialog)
        self.leadDelayR.setMinimum(-10.0)
        self.leadDelayR.setMaximum(10.0)
        self.leadDelayR.setObjectName("leadDelayR")
        self.gridLayout.addWidget(self.leadDelayR, 0, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1)
        self.leadDelayTheta = QtWidgets.QDoubleSpinBox(Dialog)
        self.leadDelayTheta.setMinimum(-10.0)
        self.leadDelayTheta.setMaximum(10.0)
        self.leadDelayTheta.setObjectName("leadDelayTheta")
        self.gridLayout.addWidget(self.leadDelayTheta, 1, 3, 1, 1)
        self.leadDelayOffset = QtWidgets.QDoubleSpinBox(Dialog)
        self.leadDelayOffset.setMinimum(-10.0)
        self.leadDelayOffset.setMaximum(10.0)
        self.leadDelayOffset.setObjectName("leadDelayOffset")
        self.gridLayout.addWidget(self.leadDelayOffset, 2, 3, 1, 1)
        self.leadDelayFlow = QtWidgets.QDoubleSpinBox(Dialog)
        self.leadDelayFlow.setMinimum(-10.0)
        self.leadDelayFlow.setMaximum(10.0)
        self.leadDelayFlow.setObjectName("leadDelayFlow")
        self.gridLayout.addWidget(self.leadDelayFlow, 3, 3, 1, 1)
        self.leadDelayNotes = QtWidgets.QDoubleSpinBox(Dialog)
        self.leadDelayNotes.setMinimum(-10.0)
        self.leadDelayNotes.setMaximum(10.0)
        self.leadDelayNotes.setObjectName("leadDelayNotes")
        self.gridLayout.addWidget(self.leadDelayNotes, 4, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "R (mm)"))
        self.label_5.setText(_translate("Dialog", "Notes (semi-tones)"))
        self.label_2.setText(_translate("Dialog", "Theta (°)"))
        self.label_4.setText(_translate("Dialog", "Flow (SLPM)"))
        self.label_3.setText(_translate("Dialog", "Offset (mm)"))
        self.label_6.setText(_translate("Dialog", "Lead or delay R (s)"))
        self.label_7.setText(_translate("Dialog", "Lead or delay Theta (s)"))
        self.label_8.setText(_translate("Dialog", "Lead or delay Offset (s)"))
        self.label_9.setText(_translate("Dialog", "Lead or delay flow (s)"))
        self.label_10.setText(_translate("Dialog", "Lead or delay notes (s)"))