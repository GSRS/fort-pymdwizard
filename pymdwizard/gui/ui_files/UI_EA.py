# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EA.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1130, 807)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_eainfo = QtWidgets.QTabWidget(Form)
        self.fgdc_eainfo.setTabPosition(QtWidgets.QTabWidget.West)
        self.fgdc_eainfo.setObjectName("fgdc_eainfo")
        self.tab_instructions = QtWidgets.QWidget()
        self.tab_instructions.setObjectName("tab_instructions")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_instructions)
        self.verticalLayout_4.setContentsMargins(25, 15, 0, 25)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_instructions)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(15, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.tab_instructions)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.tab_instructions)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(
            20, 419, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.tab_instructions)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(700, 150))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setStyleSheet(
            "QGroupBox{ \n"
            'font: 75 10pt "Arial";\n'
            "border: 1px solid black;\n"
            "border-radius: 3px;\n"
            "background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eef, stop: 1 #ccf);\n"
            "} "
        )
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setStyleSheet("font: italic;")
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_3.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet("font: italic;")
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_3.addWidget(self.label_35)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_add_detailed = QtWidgets.QPushButton(self.groupBox)
        self.btn_add_detailed.setObjectName("btn_add_detailed")
        self.horizontalLayout_2.addWidget(self.btn_add_detailed)
        spacerItem2 = QtWidgets.QSpacerItem(
            38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.verticalLayout_4.addWidget(self.widget)
        self.fgdc_eainfo.addTab(self.tab_instructions, "")
        self.fgdc_overview = QtWidgets.QWidget()
        self.fgdc_overview.setObjectName("fgdc_overview")
        self.label = QtWidgets.QLabel(self.fgdc_overview)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label.setObjectName("label")
        self.fgdc_eaover = QtWidgets.QPlainTextEdit(self.fgdc_overview)
        self.fgdc_eaover.setGeometry(QtCore.QRect(30, 50, 571, 192))
        self.fgdc_eaover.setObjectName("fgdc_eaover")
        self.label_6 = QtWidgets.QLabel(self.fgdc_overview)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 111, 16))
        self.label_6.setObjectName("label_6")
        self.fgdc_eadetcit = QtWidgets.QPlainTextEdit(self.fgdc_overview)
        self.fgdc_eadetcit.setGeometry(QtCore.QRect(30, 270, 571, 192))
        self.fgdc_eadetcit.setObjectName("fgdc_eadetcit")
        self.fgdc_eainfo.addTab(self.fgdc_overview, "")
        self.verticalLayout.addWidget(self.fgdc_eainfo)

        self.retranslateUi(Form)
        self.fgdc_eainfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setToolTip(_translate("Form", "Required"))
        self.label_5.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:12pt; font-style:italic; color:#55aaff;">Provide Specific Information about the data content, organization, units, and values.</span></p></body></html>',
            )
        )
        self.label_2.setText(
            _translate(
                "Form",
                "If this record describes a CSV, Shapefile, or other tabular or spatial dataset you need to fill out a Detailed section. Use the 'Browse to Dataset' button on a detailed tab  to autopopulate this section with the column labels and values. Then provide definitions for each column (attribute) and values. \n"
                "\n"
                "If this record describes multiple files or sheets, one Detailed section should be created for each, see below.",
            )
        )
        self.label_4.setText(
            _translate(
                "Form",
                "Use both the Overview and one or more Detailed sections if that provides more clarity to data users.",
            )
        )
        self.groupBox.setTitle(_translate("Form", "Additional 'Detailed' tabs"))
        self.label_34.setText(
            _translate(
                "Form",
                "In some cases more than one Detailed section is required.  This could be the case if the metadata record is describing multiple CSV files, multiple worksheets in an Excel Workbook, or a data bundle consisting of multiple files.",
            )
        )
        self.label_35.setText(
            _translate(
                "Form",
                "Use the button below to add additional Detailed sections.  These can be removed from their respective tab, using the 'Remove this Detailed' Button",
            )
        )
        self.btn_add_detailed.setText(_translate("Form", "Add Detailed"))
        self.fgdc_eainfo.setTabText(
            self.fgdc_eainfo.indexOf(self.tab_instructions),
            _translate("Form", "Instructions"),
        )
        self.label.setText(_translate("Form", "Overview Description"))
        self.label_6.setText(_translate("Form", "Citation"))
        self.fgdc_eainfo.setTabText(
            self.fgdc_eainfo.indexOf(self.fgdc_overview), _translate("Form", "Overview")
        )
