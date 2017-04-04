# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessStep.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(435, 397)
        Form.setMinimumSize(QtCore.QSize(0, 175))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fgdc_procstep = QtWidgets.QWidget(Form)
        self.fgdc_procstep.setObjectName("fgdc_procstep")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fgdc_procstep)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.fgdc_procstep)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fgdc_procdesc = QtWidgets.QPlainTextEdit(self.fgdc_procstep)
        self.fgdc_procdesc.setObjectName("fgdc_procdesc")
        self.verticalLayout.addWidget(self.fgdc_procdesc)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_37 = QtWidgets.QLabel(self.fgdc_procstep)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.label_37)
        self.fgdc_procdate = QtWidgets.QWidget(self.fgdc_procstep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_procdate.sizePolicy().hasHeightForWidth())
        self.fgdc_procdate.setSizePolicy(sizePolicy)
        self.fgdc_procdate.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_procdate.setMaximumSize(QtCore.QSize(221, 100))
        self.fgdc_procdate.setObjectName("fgdc_procdate")
        self.verticalLayout_2.addWidget(self.fgdc_procdate)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.fgdc_procstep)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.fgdc_srcused = QtWidgets.QLineEdit(self.fgdc_procstep)
        self.fgdc_srcused.setObjectName("fgdc_srcused")
        self.verticalLayout_4.addWidget(self.fgdc_srcused)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.fgdc_procstep)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.fgdc_srcprod = QtWidgets.QLineEdit(self.fgdc_procstep)
        self.fgdc_srcprod.setObjectName("fgdc_srcprod")
        self.verticalLayout_3.addWidget(self.fgdc_srcprod)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.widget_proccont = QtWidgets.QWidget(self.fgdc_procstep)
        self.widget_proccont.setObjectName("widget_proccont")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_proccont)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addWidget(self.widget_proccont)
        self.horizontalLayout_3.addWidget(self.fgdc_procstep)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Describe the processing step or method below:"))
        self.fgdc_procdesc.setPlainText(_translate("Form", "Development of the data set by the agency / individuals identified in the \'Originator\' element in the Identification Info section of the record."))
        self.label_37.setText(_translate("Form", "Process Date (YYYYMMDD)"))
        self.label_3.setText(_translate("Form", "Source Used Citation Abbreviation"))
        self.label_2.setText(_translate("Form", "Source Produced Citation Abbreviation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

