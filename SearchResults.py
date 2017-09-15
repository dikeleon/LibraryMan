# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchResults.ui'
#
# Created: Sun Jul 23 17:00:21 2017
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

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        SearchDialog.setObjectName(_fromUtf8("SearchDialog"))
        SearchDialog.resize(282, 277)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        SearchDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/magnifier.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SearchDialog.setWindowIcon(icon)
        SearchDialog.setWindowOpacity(1.0)
        self.gridLayout = QtGui.QGridLayout(SearchDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView = QtGui.QListView(SearchDialog)
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.listView.setFrameShape(QtGui.QFrame.NoFrame)
        self.listView.setFrameShadow(QtGui.QFrame.Plain)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)

        self.retranslateUi(SearchDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchDialog)

    def retranslateUi(self, SearchDialog):
        SearchDialog.setWindowTitle(_translate("SearchDialog", "Search Results", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SearchDialog = QtGui.QDialog()
    ui = Ui_SearchDialog()
    ui.setupUi(SearchDialog)
    SearchDialog.show()
    sys.exit(app.exec_())

