# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OverDuebx.ui'
#
# Created: Thu Jul 13 22:22:16 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogO(object):
    def setupUi(self, DialogO):
        DialogO.setObjectName(_fromUtf8("DialogO"))
        DialogO.resize(441, 522)
        DialogO.setMinimumSize(QtCore.QSize(441, 522))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        DialogO.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/product-sales-report.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogO.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DialogO)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(DialogO)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogO)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.label = QtGui.QLabel(DialogO)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(DialogO)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogO.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogO.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogO)

    def retranslateUi(self, DialogO):
        DialogO.setWindowTitle(_translate("DialogO", "Overdue Books List", None))
        self.label.setText(_translate("DialogO", "overdue books :", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogO = QtGui.QDialog()
    ui = Ui_DialogO()
    ui.setupUi(DialogO)
    DialogO.show()
    sys.exit(app.exec_())

