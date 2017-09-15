# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BorrowedBooks.ui'
#
# Created: Thu Jul 13 21:33:50 2017
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

class Ui_DialogB(object):
    def setupUi(self, DialogS):
        DialogS.setObjectName(_fromUtf8("DialogS"))
        DialogS.resize(441, 522)
        DialogS.setMinimumSize(QtCore.QSize(441, 522))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/product-sales-report.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogS.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DialogS)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(DialogS)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(DialogS)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogS)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(DialogS)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogS.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogS.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogS)

    def retranslateUi(self, DialogS):
        DialogS.setWindowTitle(_translate("DialogS", "Borrowed Books List", None))
        self.label.setText(_translate("DialogS", "borrowed books :", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogS = QtGui.QDialog()
    ui = Ui_DialogB()
    ui.setupUi(DialogS)
    DialogS.show()
    sys.exit(app.exec_())

