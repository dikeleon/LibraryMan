# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentsList.ui'
#
# Created: Fri Jul 21 09:37:11 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb

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

class Ui_DialogS(object):


    # def stdnts(self):
    #     connek = MySQLdb.connect(host='localhost', user='root', passwd='leondike23', db='librarysys')
    #     c4 = connek.cursor()
    #     c4.execute("SELECT name FROM students")
    #     data5 = c4.fetchall()
    #     # indx = 1
    #     global allstudents
    #     allstudents = []
    #     for i in data5:
    #         # indxdname = str(indx)+". "+ str(i[0])
    #         # # self.ui.textEdit.insertPlainText()
    #         # self.ui.textEdit.insertPlainText(indxdname)
    #         # self.ui.textEdit.insertPlainText("\n")
    #         # indx += 1
    #         allstudents.append(i[0])
    #         # print i[0]
    #     print allstudents
    #     model2 = QtGui.QStringListModel(allstudents)
    #     blist2 = QtGui.QListView(self.listView)
    #     blist2.setFixedSize(342,485)
    #     blist2.setModel(model2)
    #     blist2.clicked.connect(self.ClickedStd)
    #
    # def ClickedStd(self, QModelIndex):
    #     print allstudents[QModelIndex.row()]

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
        self.buttonBox = QtGui.QDialogButtonBox(DialogS)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.listView = QtGui.QListView(DialogS)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)

        self.retranslateUi(DialogS)
        # self.stdnts()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogS.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogS.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogS)

    def retranslateUi(self, DialogS):
        DialogS.setWindowTitle(_translate("DialogS", "Students List", None))
        self.label.setText(_translate("DialogS", "students", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogS = QtGui.QDialog()
    ui = Ui_DialogS()
    ui.setupUi(DialogS)
    DialogS.show()
    sys.exit(app.exec_())

