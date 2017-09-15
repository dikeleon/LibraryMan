# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Blacklisted.ui'
#
# Created: Sat Jul 22 22:21:00 2017
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

class Ui_DialogX(object):
    def setupUi(self, DialogX):
        DialogX.setObjectName(_fromUtf8("DialogX"))
        DialogX.resize(441, 522)
        DialogX.setMinimumSize(QtCore.QSize(441, 522))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        DialogX.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/product-sales-report.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogX.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DialogX)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogX)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.label = QtGui.QLabel(DialogX)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.listView = QtGui.QListView(DialogX)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)

        self.retranslateUi(DialogX)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogX.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogX.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogX)

    def retranslateUi(self, DialogX):
        DialogX.setWindowTitle(_translate("DialogX", "Blacklisted", None))
        self.label.setText(_translate("DialogX", "Blacklisted Students :", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogX = QtGui.QDialog()
    ui = Ui_DialogX()
    ui.setupUi(DialogX)
    DialogX.show()
    sys.exit(app.exec_())

