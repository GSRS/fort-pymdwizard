# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jupyterstarter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 276)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.help_geoform_2 = QtWidgets.QFrame(Form)
        self.help_geoform_2.setObjectName("help_geoform_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.help_geoform_2)
        self.verticalLayout_15.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_53 = QtWidgets.QLabel(self.help_geoform_2)
        self.label_53.setStyleSheet("font: bold;")
        self.label_53.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_53.setObjectName("label_53")
        self.verticalLayout_15.addWidget(self.label_53)
        self.label_34 = QtWidgets.QLabel(self.help_geoform_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setStyleSheet("font: italic;")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_15.addWidget(self.label_34)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dname = QtWidgets.QComboBox(self.help_geoform_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.dname.setFont(font)
        self.dname.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dname.setEditable(True)
        self.dname.setCurrentText("")
        self.dname.setObjectName("dname")
        self.horizontalLayout_2.addWidget(self.dname)
        self.btn_browse = QtWidgets.QPushButton(self.help_geoform_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout_2.addWidget(self.btn_browse)
        self.verticalLayout_15.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.help_geoform_2)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.help_geoform = QtWidgets.QFrame(Form)
        self.help_geoform.setObjectName("help_geoform")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.help_geoform)
        self.verticalLayout_14.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_52 = QtWidgets.QLabel(self.help_geoform)
        self.label_52.setStyleSheet("font: bold;")
        self.label_52.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_52.setObjectName("label_52")
        self.verticalLayout_14.addWidget(self.label_52)
        self.label_35 = QtWidgets.QLabel(self.help_geoform)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet("font: italic;")
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_14.addWidget(self.label_35)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kernel = QtWidgets.QComboBox(self.help_geoform)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.kernel.setFont(font)
        self.kernel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.kernel.setEditable(True)
        self.kernel.setCurrentText("")
        self.kernel.setObjectName("kernel")
        self.horizontalLayout.addWidget(self.kernel)
        self.verticalLayout_14.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.help_geoform)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.usejupyterframe = QtWidgets.QFrame(Form)
        self.usejupyterframe.setEnabled(False)
        self.usejupyterframe.setObjectName("usejupyterframe")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.usejupyterframe)
        self.verticalLayout_17.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_55 = QtWidgets.QLabel(self.usejupyterframe)
        self.label_55.setStyleSheet("font: bold;")
        self.label_55.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_55.setObjectName("label_55")
        self.verticalLayout_17.addWidget(self.label_55)
        self.label_37 = QtWidgets.QLabel(self.usejupyterframe)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setStyleSheet("font: italic;")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_17.addWidget(self.label_37)
        self.usejupyterlab = QtWidgets.QCheckBox(self.usejupyterframe)
        self.usejupyterlab.setObjectName("usejupyterlab")
        self.verticalLayout_17.addWidget(self.usejupyterlab)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_17.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addWidget(self.usejupyterframe)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_launch = QtWidgets.QPushButton(Form)
        self.btn_launch.setObjectName("btn_launch")
        self.horizontalLayout_3.addWidget(self.btn_launch)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_53.setText(_translate("Form", "What Directory to Start in:"))
        self.label_34.setText(
            _translate(
                "Form", "This is the folder containing the notebooks you want to run. "
            )
        )
        self.btn_browse.setText(_translate("Form", "Browse"))
        self.label_52.setText(_translate("Form", "What Python Kernel to use:"))
        self.label_35.setText(
            _translate(
                "Form",
                "This is instance of Python you want to run Jupyter with.  In addition to the Python version that was installed with the MetadataWizard any available Conda Envs are listed",
            )
        )
        self.label_55.setText(_translate("Form", "Use JupyterLab ?"))
        self.label_37.setText(
            _translate(
                "Form",
                "<html><head/><body><p>Use the new JupyterLab interface instead of the tradional notebook. </p><p>If this is greyed out, JupyterLab is not installed. Download and Reinstall the latest version of the MetadataWizard to obtain it. </p></body></html>",
            )
        )
        self.usejupyterlab.setText(_translate("Form", "Use JupyterLab"))
        self.btn_launch.setText(_translate("Form", "Launch"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
