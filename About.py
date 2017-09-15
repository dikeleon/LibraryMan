
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

class Ui_DialogA(object):
    def setupUi(self, DialogA):
        DialogA.setObjectName(_fromUtf8("DialogA"))
        DialogA.resize(400, 262)
        DialogA.setMinimumSize(QtCore.QSize(400, 262))
        DialogA.setMaximumSize(QtCore.QSize(400, 262))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        DialogA.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/library.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogA.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(DialogA)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setMinimumSize(QtCore.QSize(81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(DialogA)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 61))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/library.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogA)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 331, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DialogA)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 331, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(DialogA)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 331, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(DialogA)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 331, 16))
        self.label_5.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(DialogA)
        self.label_6.setGeometry(QtCore.QRect(200, 210, 151, 20))
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(DialogA)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 331, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(DialogA)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogA.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogA.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogA)

    def retranslateUi(self, DialogA):
        DialogA.setWindowTitle(_translate("DialogA", "About LibMan", None))
        self.label_2.setText(_translate("DialogA", "This piece of software was designed with the ", None))
        self.label_3.setText(_translate("DialogA", " easier and illustrate the  beauty of", None))
        self.label_4.setText(_translate("DialogA", " computers to the community ", None))
        self.label_5.setText(_translate("DialogA", "CONTACT THE DEVELOPER AT:   dikeleon@gmail.com", None))
        self.label_6.setText(_translate("DialogA", ":   +263773850460", None))
        self.label_7.setText(_translate("DialogA", " intention of making a librarian`s life  much", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogA = QtGui.QDialog()
    ui = Ui_DialogA()
    ui.setupUi(DialogA)
    DialogA.show()
    sys.exit(app.exec_())

