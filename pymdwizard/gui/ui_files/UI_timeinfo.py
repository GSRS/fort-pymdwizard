# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 158)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: italic;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: italic;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(15, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radio_single = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_single.sizePolicy().hasHeightForWidth())
        self.radio_single.setSizePolicy(sizePolicy)
        self.radio_single.setChecked(True)
        self.radio_single.setObjectName("radio_single")
        self.horizontalLayout_4.addWidget(self.radio_single)
        self.radio_range = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_range.sizePolicy().hasHeightForWidth())
        self.radio_range.setSizePolicy(sizePolicy)
        self.radio_range.setObjectName("radio_range")
        self.horizontalLayout_4.addWidget(self.radio_range)
        self.radio_multiple = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.radio_multiple.sizePolicy().hasHeightForWidth()
        )
        self.radio_multiple.setSizePolicy(sizePolicy)
        self.radio_multiple.setObjectName("radio_multiple")
        self.horizontalLayout_4.addWidget(self.radio_multiple)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.fgdc_timeinfo = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_timeinfo.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_timeinfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_timeinfo.setFont(font)
        self.fgdc_timeinfo.setObjectName("fgdc_timeinfo")
        self.fgdc_sngdate = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_sngdate.sizePolicy().hasHeightForWidth())
        self.fgdc_sngdate.setSizePolicy(sizePolicy)
        self.fgdc_sngdate.setObjectName("fgdc_sngdate")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fgdc_sngdate)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_10.setContentsMargins(9, 9, 0, 0)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_10.addItem(spacerItem)
        self.fgdc_timeinfo.addWidget(self.fgdc_sngdate)
        self.fgdc_rngdates = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_rngdates.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_rngdates.setSizePolicy(sizePolicy)
        self.fgdc_rngdates.setObjectName("fgdc_rngdates")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fgdc_rngdates)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout_daterange = QtWidgets.QHBoxLayout()
        self.layout_daterange.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_daterange.setSpacing(0)
        self.layout_daterange.setObjectName("layout_daterange")
        self.verticalLayout_3.addLayout(self.layout_daterange)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_7.addItem(spacerItem1)
        self.fgdc_timeinfo.addWidget(self.fgdc_rngdates)
        self.fgdc_mdattim = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_mdattim.sizePolicy().hasHeightForWidth())
        self.fgdc_mdattim.setSizePolicy(sizePolicy)
        self.fgdc_mdattim.setObjectName("fgdc_mdattim")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fgdc_mdattim)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(4, 4, 4, 0)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.layout_multipledates = QtWidgets.QVBoxLayout()
        self.layout_multipledates.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout_multipledates.setContentsMargins(-1, 0, -1, -1)
        self.layout_multipledates.setObjectName("layout_multipledates")
        self.horizontalLayout_6.addLayout(self.layout_multipledates)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.fgdc_timeinfo.addWidget(self.fgdc_mdattim)
        self.verticalLayout_2.addWidget(self.fgdc_timeinfo)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        self.fgdc_timeinfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(
            _translate("Form", "What is the time period represented in the dataset?")
        )
        self.label_3.setText(
            _translate(
                "Form",
                "Select one of 'Single Date', 'Date Range', or 'Multiple Dates'.",
            )
        )
        self.label_9.setToolTip(_translate("Form", "Required"))
        self.label_9.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.radio_single.setText(_translate("Form", "Single"))
        self.radio_range.setText(_translate("Form", "Range"))
        self.radio_multiple.setText(_translate("Form", "Multiple"))
