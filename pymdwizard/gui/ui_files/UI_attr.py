# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attr.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_attribute_widget(object):
    def setupUi(self, attribute_widget):
        attribute_widget.setObjectName("attribute_widget")
        attribute_widget.resize(325, 679)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(attribute_widget)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fgdc_attr = QtWidgets.QFrame(attribute_widget)
        self.fgdc_attr.setFrameShape(QtWidgets.QFrame.Panel)
        self.fgdc_attr.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fgdc_attr.setLineWidth(2)
        self.fgdc_attr.setMidLineWidth(2)
        self.fgdc_attr.setObjectName("fgdc_attr")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_attr)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.fgdc_attr)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_attrlabl = QtWidgets.QLineEdit(self.fgdc_attr)
        self.fgdc_attrlabl.setStyleSheet("font: bold 12pt ;")
        self.fgdc_attrlabl.setObjectName("fgdc_attrlabl")
        self.horizontalLayout.addWidget(self.fgdc_attrlabl)
        self.label_20 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(15, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_20.setIndent(0)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_21 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(15, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setScaledContents(True)
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_21.setIndent(0)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.fgdc_attrdef = QtWidgets.QPlainTextEdit(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_attrdef.sizePolicy().hasHeightForWidth())
        self.fgdc_attrdef.setSizePolicy(sizePolicy)
        self.fgdc_attrdef.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fgdc_attrdef.setObjectName("fgdc_attrdef")
        self.verticalLayout.addWidget(self.fgdc_attrdef)
        self.label_3 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fgdc_attrdefs = QtWidgets.QLineEdit(self.fgdc_attr)
        self.fgdc_attrdefs.setObjectName("fgdc_attrdefs")
        self.horizontalLayout_5.addWidget(self.fgdc_attrdefs)
        self.label_24 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(15, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_24.setIndent(0)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_5.addWidget(self.label_24)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_7 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.nodata_content = QtWidgets.QFrame(self.fgdc_attr)
        self.nodata_content.setObjectName("nodata_content")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.nodata_content)
        self.verticalLayout_24.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_24.setSpacing(3)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_49 = QtWidgets.QLabel(self.nodata_content)
        self.label_49.setStyleSheet("font: bold;")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_8.addWidget(self.label_49)
        spacerItem1 = QtWidgets.QSpacerItem(
            0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem1)
        self.rbtn_nodata_yes = QtWidgets.QRadioButton(self.nodata_content)
        self.rbtn_nodata_yes.setChecked(True)
        self.rbtn_nodata_yes.setObjectName("rbtn_nodata_yes")
        self.horizontalLayout_8.addWidget(self.rbtn_nodata_yes)
        self.rbtn_nodata_no = QtWidgets.QRadioButton(self.nodata_content)
        self.rbtn_nodata_no.setChecked(False)
        self.rbtn_nodata_no.setObjectName("rbtn_nodata_no")
        self.horizontalLayout_8.addWidget(self.rbtn_nodata_no)
        self.verticalLayout_24.addLayout(self.horizontalLayout_8)
        self.nodata_section = QtWidgets.QWidget(self.nodata_content)
        self.nodata_section.setObjectName("nodata_section")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.nodata_section)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_24.addWidget(self.nodata_section)
        self.verticalLayout.addWidget(self.nodata_content)
        self.attrdomv_contents = QtWidgets.QWidget(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.attrdomv_contents.sizePolicy().hasHeightForWidth()
        )
        self.attrdomv_contents.setSizePolicy(sizePolicy)
        self.attrdomv_contents.setObjectName("attrdomv_contents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.attrdomv_contents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.attrdomv_contents)
        self.place_holder = QtWidgets.QWidget(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.place_holder.sizePolicy().hasHeightForWidth())
        self.place_holder.setSizePolicy(sizePolicy)
        self.place_holder.setObjectName("place_holder")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.place_holder)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout.addWidget(self.place_holder)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_6.addWidget(self.fgdc_attr)

        self.retranslateUi(attribute_widget)
        QtCore.QMetaObject.connectSlotsByName(attribute_widget)

    def retranslateUi(self, attribute_widget):
        _translate = QtCore.QCoreApplication.translate
        attribute_widget.setWindowTitle(_translate("attribute_widget", "Form"))
        self.label_2.setText(_translate("attribute_widget", "Column Label"))
        self.label_20.setToolTip(_translate("attribute_widget", "Required"))
        self.label_20.setText(
            _translate(
                "attribute_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label.setText(_translate("attribute_widget", "Column Definition"))
        self.label_21.setToolTip(_translate("attribute_widget", "Required"))
        self.label_21.setText(
            _translate(
                "attribute_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_3.setText(_translate("attribute_widget", "Definition Source"))
        self.fgdc_attrdefs.setText(_translate("attribute_widget", "Producer defined"))
        self.label_24.setToolTip(_translate("attribute_widget", "Required"))
        self.label_24.setText(
            _translate(
                "attribute_widget",
                '<html><head/><body><p align="center"><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_7.setText(_translate("attribute_widget", "Column Contents Type"))
        self.comboBox.setItemText(
            0, _translate("attribute_widget", "Enumerated (Categorical Data)")
        )
        self.comboBox.setItemText(
            1, _translate("attribute_widget", "Range (Numeric data)")
        )
        self.comboBox.setItemText(
            2, _translate("attribute_widget", "Codeset (Published Categories)")
        )
        self.comboBox.setItemText(
            3, _translate("attribute_widget", "Unrepresentable (None of the above)")
        )
        self.label_49.setText(
            _translate("attribute_widget", "Is there a NoData (NaN, etc) Value?")
        )
        self.rbtn_nodata_yes.setText(_translate("attribute_widget", "Yes"))
        self.rbtn_nodata_no.setText(_translate("attribute_widget", "No"))
