# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spdom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fgdc_spdom(object):
    def setupUi(self, fgdc_spdom):
        fgdc_spdom.setObjectName("fgdc_spdom")
        fgdc_spdom.resize(838, 441)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(fgdc_spdom)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.group = QtWidgets.QGroupBox(fgdc_spdom)
        self.group.setObjectName("group")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.group)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.group)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.descgeog_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.descgeog_label.sizePolicy().hasHeightForWidth()
        )
        self.descgeog_label.setSizePolicy(sizePolicy)
        self.descgeog_label.setMinimumSize(QtCore.QSize(0, 0))
        self.descgeog_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.descgeog_label.setFont(font)
        self.descgeog_label.setStyleSheet("")
        self.descgeog_label.setScaledContents(False)
        self.descgeog_label.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.descgeog_label.setWordWrap(False)
        self.descgeog_label.setIndent(0)
        self.descgeog_label.setObjectName("descgeog_label")
        self.verticalLayout_2.addWidget(self.descgeog_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_descgeog = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fgdc_descgeog.sizePolicy().hasHeightForWidth()
        )
        self.fgdc_descgeog.setSizePolicy(sizePolicy)
        self.fgdc_descgeog.setMinimumSize(QtCore.QSize(217, 0))
        self.fgdc_descgeog.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_descgeog.setToolTip("")
        self.fgdc_descgeog.setText("")
        self.fgdc_descgeog.setPlaceholderText("")
        self.fgdc_descgeog.setObjectName("fgdc_descgeog")
        self.horizontalLayout.addWidget(self.fgdc_descgeog)
        self.descgeog_star = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.descgeog_star.sizePolicy().hasHeightForWidth()
        )
        self.descgeog_star.setSizePolicy(sizePolicy)
        self.descgeog_star.setMinimumSize(QtCore.QSize(15, 0))
        self.descgeog_star.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.descgeog_star.setFont(font)
        self.descgeog_star.setScaledContents(True)
        self.descgeog_star.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.descgeog_star.setIndent(0)
        self.descgeog_star.setObjectName("descgeog_star")
        self.horizontalLayout.addWidget(self.descgeog_star)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.fgdc_bounding = QtWidgets.QGroupBox(self.layoutWidget)
        self.fgdc_bounding.setObjectName("fgdc_bounding")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_bounding)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_cntper_2 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cntper_2.sizePolicy().hasHeightForWidth())
        self.lbl_cntper_2.setSizePolicy(sizePolicy)
        self.lbl_cntper_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_cntper_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_cntper_2.setFont(font)
        self.lbl_cntper_2.setToolTip("")
        self.lbl_cntper_2.setStyleSheet("")
        self.lbl_cntper_2.setScaledContents(False)
        self.lbl_cntper_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_cntper_2.setWordWrap(False)
        self.lbl_cntper_2.setIndent(0)
        self.lbl_cntper_2.setObjectName("lbl_cntper_2")
        self.horizontalLayout_2.addWidget(self.lbl_cntper_2)
        self.fgdc_westbc = QtWidgets.QLineEdit(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_westbc.sizePolicy().hasHeightForWidth())
        self.fgdc_westbc.setSizePolicy(sizePolicy)
        self.fgdc_westbc.setMinimumSize(QtCore.QSize(217, 0))
        self.fgdc_westbc.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_westbc.setToolTip("")
        self.fgdc_westbc.setText("")
        self.fgdc_westbc.setPlaceholderText("")
        self.fgdc_westbc.setObjectName("fgdc_westbc")
        self.horizontalLayout_2.addWidget(self.fgdc_westbc)
        self.label_4 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(15, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_cntper_3 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cntper_3.sizePolicy().hasHeightForWidth())
        self.lbl_cntper_3.setSizePolicy(sizePolicy)
        self.lbl_cntper_3.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_cntper_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_cntper_3.setFont(font)
        self.lbl_cntper_3.setToolTip("")
        self.lbl_cntper_3.setStyleSheet("")
        self.lbl_cntper_3.setScaledContents(False)
        self.lbl_cntper_3.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_cntper_3.setWordWrap(False)
        self.lbl_cntper_3.setIndent(0)
        self.lbl_cntper_3.setObjectName("lbl_cntper_3")
        self.horizontalLayout_3.addWidget(self.lbl_cntper_3)
        self.fgdc_eastbc = QtWidgets.QLineEdit(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_eastbc.sizePolicy().hasHeightForWidth())
        self.fgdc_eastbc.setSizePolicy(sizePolicy)
        self.fgdc_eastbc.setMinimumSize(QtCore.QSize(217, 0))
        self.fgdc_eastbc.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_eastbc.setToolTip("")
        self.fgdc_eastbc.setText("")
        self.fgdc_eastbc.setPlaceholderText("")
        self.fgdc_eastbc.setObjectName("fgdc_eastbc")
        self.horizontalLayout_3.addWidget(self.fgdc_eastbc)
        self.label_5 = QtWidgets.QLabel(self.fgdc_bounding)
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
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_cntper_4 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cntper_4.sizePolicy().hasHeightForWidth())
        self.lbl_cntper_4.setSizePolicy(sizePolicy)
        self.lbl_cntper_4.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_cntper_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_cntper_4.setFont(font)
        self.lbl_cntper_4.setToolTip("")
        self.lbl_cntper_4.setStyleSheet("")
        self.lbl_cntper_4.setScaledContents(False)
        self.lbl_cntper_4.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_cntper_4.setWordWrap(False)
        self.lbl_cntper_4.setIndent(0)
        self.lbl_cntper_4.setObjectName("lbl_cntper_4")
        self.horizontalLayout_4.addWidget(self.lbl_cntper_4)
        self.fgdc_northbc = QtWidgets.QLineEdit(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_northbc.sizePolicy().hasHeightForWidth())
        self.fgdc_northbc.setSizePolicy(sizePolicy)
        self.fgdc_northbc.setMinimumSize(QtCore.QSize(217, 0))
        self.fgdc_northbc.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_northbc.setToolTip("")
        self.fgdc_northbc.setText("")
        self.fgdc_northbc.setPlaceholderText("")
        self.fgdc_northbc.setObjectName("fgdc_northbc")
        self.horizontalLayout_4.addWidget(self.fgdc_northbc)
        self.label_6 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(15, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_cntper_5 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cntper_5.sizePolicy().hasHeightForWidth())
        self.lbl_cntper_5.setSizePolicy(sizePolicy)
        self.lbl_cntper_5.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_cntper_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_cntper_5.setFont(font)
        self.lbl_cntper_5.setToolTip("")
        self.lbl_cntper_5.setStyleSheet("")
        self.lbl_cntper_5.setScaledContents(False)
        self.lbl_cntper_5.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
        )
        self.lbl_cntper_5.setWordWrap(False)
        self.lbl_cntper_5.setIndent(0)
        self.lbl_cntper_5.setObjectName("lbl_cntper_5")
        self.horizontalLayout_5.addWidget(self.lbl_cntper_5)
        self.fgdc_southbc = QtWidgets.QLineEdit(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_southbc.sizePolicy().hasHeightForWidth())
        self.fgdc_southbc.setSizePolicy(sizePolicy)
        self.fgdc_southbc.setMinimumSize(QtCore.QSize(217, 0))
        self.fgdc_southbc.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fgdc_southbc.setToolTip("")
        self.fgdc_southbc.setText("")
        self.fgdc_southbc.setPlaceholderText("")
        self.fgdc_southbc.setObjectName("fgdc_southbc")
        self.horizontalLayout_5.addWidget(self.fgdc_southbc)
        self.label_7 = QtWidgets.QLabel(self.fgdc_bounding)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(15, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.fgdc_bounding)
        self.map_display = QtWidgets.QFrame(self.splitter)
        self.map_display.setMinimumSize(QtCore.QSize(400, 400))
        self.map_display.setFrameShape(QtWidgets.QFrame.Box)
        self.map_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.map_display.setLineWidth(1)
        self.map_display.setObjectName("map_display")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.map_display)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.group)

        self.retranslateUi(fgdc_spdom)
        QtCore.QMetaObject.connectSlotsByName(fgdc_spdom)

    def retranslateUi(self, fgdc_spdom):
        _translate = QtCore.QCoreApplication.translate
        fgdc_spdom.setWindowTitle(_translate("fgdc_spdom", "Form"))
        self.group.setTitle(_translate("fgdc_spdom", "Spatial Domain"))
        self.descgeog_label.setToolTip(
            _translate("fgdc_spdom", "The name of the person to contact")
        )
        self.descgeog_label.setText(
            _translate("fgdc_spdom", "Description of Geographic Extent")
        )
        self.descgeog_star.setToolTip(_translate("fgdc_spdom", "Required"))
        self.descgeog_star.setText(
            _translate(
                "fgdc_spdom",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.fgdc_bounding.setTitle(_translate("fgdc_spdom", "Bounding Coordinates"))
        self.lbl_cntper_2.setText(_translate("fgdc_spdom", "West (-180 - 180) "))
        self.label_4.setToolTip(_translate("fgdc_spdom", "Required"))
        self.label_4.setText(
            _translate(
                "fgdc_spdom",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.lbl_cntper_3.setText(_translate("fgdc_spdom", "East (-180 - 180)  "))
        self.label_5.setToolTip(_translate("fgdc_spdom", "Required"))
        self.label_5.setText(
            _translate(
                "fgdc_spdom",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.lbl_cntper_4.setText(_translate("fgdc_spdom", "North (-90 - 90)     "))
        self.label_6.setToolTip(_translate("fgdc_spdom", "Required"))
        self.label_6.setText(
            _translate(
                "fgdc_spdom",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.lbl_cntper_5.setText(_translate("fgdc_spdom", "South (-90 - 90)    "))
        self.label_7.setToolTip(_translate("fgdc_spdom", "Required"))
        self.label_7.setText(
            _translate(
                "fgdc_spdom",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
