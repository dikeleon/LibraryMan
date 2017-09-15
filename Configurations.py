# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configurations.ui'
#
# Created: Sat Jul 15 21:41:24 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
# from PyQt4.QtCore import *
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

class Ui_DialogCF(object):

    def oldConfs(self):
        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c = conn.cursor()
        c.execute("SELECT * FROM configs ")
        try:
            data2 = c.fetchone()
            # self.lineEdit.setText(str(data2[0][1]))
            self.lineEdit.setText(_translate("Dialog", str(data2[1]), None))
            self.lineEdit_2.setText(_translate("Dialog", str(data2[3]), None))
            print str(data2[2])
            if (data2[2]) != None:
                self.label.setPixmap(QtGui.QPixmap(_fromUtf8(str(data2[2]))))
            else:
                pass
        except:
            pass

    def UploadImage(self):
        self.Imager = QFileDialog()
        global imgr
        imgr = self.Imager.getOpenFileName()
        if len(imgr) > 0:
            self.label.setPixmap(QtGui.QPixmap(_fromUtf8(imgr)))

    def condetails(self):
        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c = conn.cursor()
        LibName = str(self.lineEdit.text())
        GracePeriod = str(self.lineEdit_2.text())
        c.execute("SELECT * FROM configs")
        data6 = c.fetchall()
        # print data6
        if (len(data6)==0 and len(LibName)>0):
            try:
                photo = str(imgr)
                c.execute("INSERT INTO configs (libname, liblogo, graceperiod) VALUES(%s, %s, %s)", (LibName,photo,GracePeriod,))
                conn.commit()
            except:
                try:
                    c.execute("INSERT INTO configs (libname, liblogo, graceperiod) VALUES(%s, NULL , %s)", (LibName,GracePeriod,))
                    conn.commit()
                except:
                    try:
                        c.execute("INSERT INTO configs (libname) VALUES(%s)", (LibName,))
                        conn.commit()
                    except:
                        pass
        elif (len(data6)==1 and len(LibName)>0):
            try:
                try:
                    photo = str(imgr)
                except:
                    photo = data6[0][2]
                c.execute("UPDATE configs SET libname=(%s), liblogo=(%s), graceperiod=(%s) WHERE id_admin=(%s)",(LibName,photo,GracePeriod,str(data6[0][0]),))
                conn.commit()
            except:
                try:
                    c.execute("UPDATE configs SET libname=(%s), liblogo=NULL , graceperiod=(%s) WHERE id_admin=(%s)",(LibName,GracePeriod,str(data6[0][0]),))
                    conn.commit()
                except:
                    try:
                        c.execute("UPDATE configs SET libname=(%s) WHERE id_admin=%s",(LibName,str(data6[0][0]),))
                        conn.commit()
                        pass
                    except:
                        pass


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(398, 297)
        Dialog.setMinimumSize(QtCore.QSize(398, 297))
        Dialog.setMaximumSize(QtCore.QSize(398, 297))
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/wheel.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(150, 240, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 101))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/image_add.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 91, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 159, 261, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 209, 261, 21))
        self.lineEdit_2.setStyleSheet(_fromUtf8("color:rgb(255, 14, 78);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.condetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.UploadImage)
        self.oldConfs()


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Configurations", None))
        self.label_2.setText(_translate("Dialog", "Library Name :", None))
        self.label_3.setText(_translate("Dialog", "Grace Period :", None))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "enter the number of days (only the number)", None))
        self.pushButton.setText(_translate("Dialog", "Upload", None))
        self.label_4.setText(_translate("Dialog", "Library Logo ", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_DialogCF()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

