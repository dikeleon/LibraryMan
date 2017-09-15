# -*- coding: utf-8 -*-

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

class Ui_DialogUE(object):
    def setupUi(self, DialogUE):
        DialogUE.setObjectName(_fromUtf8("DialogUE"))
        DialogUE.resize(420, 224)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icoz/Male-User-Warning.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogUE.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(DialogUE)
        self.buttonBox.setGeometry(QtCore.QRect(10, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(DialogUE)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 111))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icoz/Male-User-Warning.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogUE)
        self.label_2.setGeometry(QtCore.QRect(210, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nirmala UI"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DialogUE)
        self.label_3.setGeometry(QtCore.QRect(200, 80, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nirmala UI"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(DialogUE)
        self.label_4.setGeometry(QtCore.QRect(190, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nirmala UI"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(DialogUE)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogUE.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogUE.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogUE)

    def retranslateUi(self, DialogUE):
        DialogUE.setWindowTitle(_translate("DialogUE", "UserName Error", None))
        self.label_2.setText(_translate("DialogUE", "UserName already ", None))
        self.label_3.setText(_translate("DialogUE", "Registered Please try", None))
        self.label_4.setText(_translate("DialogUE", "Using a different Name!", None))

import UserName

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogUE = QtGui.QDialog()
    ui = Ui_DialogUE()
    ui.setupUi(DialogUE)
    DialogUE.show()
    sys.exit(app.exec_())

