# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MetadataDate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 260)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fgdc_timeperd = QtWidgets.QGroupBox(Form)
        self.fgdc_timeperd.setObjectName("fgdc_timeperd")
        self.label_2 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fgdc_timeinfo = QtWidgets.QStackedWidget(self.fgdc_timeperd)
        self.fgdc_timeinfo.setGeometry(QtCore.QRect(10, 80, 361, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_timeinfo.setFont(font)
        self.fgdc_timeinfo.setObjectName("fgdc_timeinfo")
        self.timeinfoPage1 = QtWidgets.QWidget()
        self.timeinfoPage1.setObjectName("timeinfoPage1")
        self.label_4 = QtWidgets.QLabel(self.timeinfoPage1)
        self.label_4.setGeometry(QtCore.QRect(120, 20, 101, 16))
        self.label_4.setObjectName("label_4")
        self.single_date_content = QtWidgets.QWidget(self.timeinfoPage1)
        self.single_date_content.setGeometry(QtCore.QRect(94, 40, 171, 31))
        self.single_date_content.setObjectName("single_date_content")
        self.fgdc_timeinfo.addWidget(self.timeinfoPage1)
        self.timeinfoPage2 = QtWidgets.QWidget()
        self.timeinfoPage2.setObjectName("timeinfoPage2")
        self.widget = QtWidgets.QWidget(self.timeinfoPage2)
        self.widget.setGeometry(QtCore.QRect(5, 20, 351, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.range_date_content_1 = QtWidgets.QWidget(self.widget)
        self.range_date_content_1.setObjectName("range_date_content_1")
        self.horizontalLayout.addWidget(self.range_date_content_1)
        self.range_date_content_2 = QtWidgets.QWidget(self.widget)
        self.range_date_content_2.setMinimumSize(QtCore.QSize(166, 0))
        self.range_date_content_2.setObjectName("range_date_content_2")
        self.horizontalLayout.addWidget(self.range_date_content_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.fgdc_timeinfo.addWidget(self.timeinfoPage2)
        self.timeinfoPage3 = QtWidgets.QWidget()
        self.timeinfoPage3.setObjectName("timeinfoPage3")
        self.label_7 = QtWidgets.QLabel(self.timeinfoPage3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 184, 16))
        self.label_7.setObjectName("label_7")
        self.SA_multi_dates = QtWidgets.QScrollArea(self.timeinfoPage3)
        self.SA_multi_dates.setGeometry(QtCore.QRect(30, 30, 181, 101))
        self.SA_multi_dates.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SA_multi_dates.setWidgetResizable(True)
        self.SA_multi_dates.setObjectName("SA_multi_dates")
        self.sa_multi_dates_content = QtWidgets.QWidget()
        self.sa_multi_dates_content.setGeometry(QtCore.QRect(0, 0, 181, 101))
        self.sa_multi_dates_content.setObjectName("sa_multi_dates_content")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sa_multi_dates_content)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.SA_multi_dates.setWidget(self.sa_multi_dates_content)
        self.widget1 = QtWidgets.QWidget(self.timeinfoPage3)
        self.widget1.setGeometry(QtCore.QRect(220, 40, 104, 54))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.fgdc_timeinfo.addWidget(self.timeinfoPage3)
        self.label_3 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_3.setGeometry(QtCore.QRect(380, 100, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.fgdc_current = QtWidgets.QComboBox(self.fgdc_timeperd)
        self.fgdc_current.setGeometry(QtCore.QRect(410, 50, 131, 21))
        self.fgdc_current.setEditable(True)
        self.fgdc_current.setObjectName("fgdc_current")
        self.fgdc_current.addItem("")
        self.fgdc_current.setItemText(0, "")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.label_8 = QtWidgets.QLabel(self.fgdc_timeperd)
        self.label_8.setGeometry(QtCore.QRect(410, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.fgdc_timeperd)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 361, 31))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 10, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 10, 101, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2.raise_()
        self.fgdc_timeinfo.raise_()
        self.label_3.raise_()
        self.fgdc_current.raise_()
        self.label_8.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.horizontalLayout_3.addWidget(self.fgdc_timeperd)

        self.retranslateUi(Form)
        self.fgdc_timeinfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_timeperd.setTitle(_translate("Form", "Time Period Information"))
        self.label_2.setText(_translate("Form", "What is the time period of the information represented in the data set?"))
        self.label_4.setText(_translate("Form", "Date (YYYYMMDD)"))
        self.label_5.setText(_translate("Form", "Beginning Date (YYYYMMDD)"))
        self.label_6.setText(_translate("Form", "End Date (YYYYMMDD)"))
        self.label_7.setText(_translate("Form", "Add Series of Dates (YYYYMMDD)"))
        self.pushButton.setText(_translate("Form", "Add Another Date"))
        self.pushButton_2.setText(_translate("Form", "Delete Last"))
        self.label_3.setText(_translate("Form", "Enter information for only one option, either \'Single Date\', \'Date Range\', or \'Multiple Dates\'."))
        self.fgdc_current.setItemText(1, _translate("Form", "ground condition"))
        self.fgdc_current.setItemText(2, _translate("Form", "observed"))
        self.fgdc_current.setItemText(3, _translate("Form", "publication date"))
        self.fgdc_current.setItemText(4, _translate("Form", "See Supplemental Info"))
        self.label_8.setText(_translate("Form", "Currentness Reference"))
        self.radioButton.setText(_translate("Form", "Single Date"))
        self.radioButton_2.setText(_translate("Form", "Date Range"))
        self.radioButton_3.setText(_translate("Form", "Multiple Dates"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

