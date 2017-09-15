# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProfile.ui'
#
# Created: Wed Jun 21 15:17:34 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from UsrNameError import Ui_DialogUE
from PyQt4.QtGui import *
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

class Ui_Dialog(object):

    def UploadImage(self):
        self.Imager = QFileDialog()
        global img
        img = self.Imager.getOpenFileName()
        if len(img) > 0:
            self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(img)))

    def Duplicated(self):
        self.Dups = QtGui.QDialog()
        self.ui = Ui_DialogUE()
        self.ui.setupUi(self.Dups)
        self.Dups.show()

    def newStud(self):
        self.name = self.lineEdit.text()
        if self.radioButton.isChecked():
            self.gender = self.radioButton.text()
        else:
            self.gender = self.radioButton_2.text()
        self.facaulty = self.lineEdit_3.text()
        self.dob = str(self.dateEdit.text())
        nguwa = []
        nguwa.append(self.dob[6:])
        nguwa.append('-')
        nguwa.append(self.dob[3:5])
        nguwa.append('-')
        nguwa.append(self.dob[:2])
        nguwa = ''.join(nguwa)
        self.dob = nguwa[0:4]
        print nguwa

        try:
            self.photo = img
        except:
            pass

        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c = conn.cursor()
        try:
	        try:
	            c.execute('INSERT INTO students(name,gender,class,dob,photo) VALUES(%s, %s, %s, %s, %s)',
	                      (str(self.name), str(self.gender), str(self.facaulty), str(self.dob), str(self.photo)))
	            c.execute('INSERT INTO books(id_students) VALUES(LAST_INSERT_ID())')
	            conn.commit()
	            conn.close()
	        except AttributeError:
	            c.execute('INSERT INTO students(name,gender,class,dob) VALUES(%s, %s, %s, %s)',
	                      (str(self.name), str(self.gender), str(self.facaulty), str(self.dob)))
	            c.execute('INSERT INTO books(id_students) VALUES(LAST_INSERT_ID())')
	            conn.commit()
	            conn.close()
        except MySQLdb.MySQLError:
            self.Duplicated()
            print "username already registered please choose another name"

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(581, 460)
        Dialog.setMinimumSize(QtCore.QSize(581, 460))
        Dialog.setMaximumSize(QtCore.QSize(581, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/OfficePack/Add-Male-User.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 351, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 351, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(130, 210, 101, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 210, 171, 151))
        self.label_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/OfficePack/image_add.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 370, 91, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/OfficePack/image_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(130, 110, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 110, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.newStud)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.UploadImage)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create A New Profile", None))
        self.label.setText(_translate("Dialog", "Name  :", None))
        self.label_2.setText(_translate("Dialog", "Gender  :", None))
        self.label_3.setText(_translate("Dialog", "Class  :", None))
        self.label_4.setText(_translate("Dialog", "Date_Of_Birth :", None))
        self.pushButton.setText(_translate("Dialog", "Upload Pic", None))
        self.radioButton.setText(_translate("Dialog", "Male", None))
        self.radioButton_2.setText(_translate("Dialog", "Female", None))
        self.label_6.setText(_translate("Dialog", "New Profile", None))

import dialogico1

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

