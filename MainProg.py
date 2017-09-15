# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Wed Jul 05 17:00:41 2017
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
# from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import datetime, time, os
from NewProfile import Ui_Dialog
from UpdateNotify import Ui_DialogU
from deletordial import Ui_DialogD
from StudentsList import  Ui_DialogS
from BorrowedBooks import Ui_DialogB
from OverDuebx import Ui_DialogO
from Blacklisted import Ui_DialogX
from Configurations import Ui_DialogCF
from About import Ui_DialogA
from SearchResults import Ui_SearchDialog

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

class Ui_mainWindow(object):

    current = 0

    def read_from_db(self):
        #CONNECTING TO THE STUDENTS DATABASE
        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c = conn.cursor()
        c.execute('SELECT * FROM students')
        global data
        try:
            data = c.fetchall()
            Name = data[self.current][1]
            Age = data[self.current][4]
            facaulty = data[self.current][3]
            gender = data[self.current][2]
            #CALCULATING AGE
            nguwa = int(str(Age)[:4])
            currentDate = int(str(datetime.date.today())[:4])
            Age = str(currentDate - nguwa)
            photo = data[self.current][5]
            if photo != None:
                if os.path.isfile(photo):
                    self.ImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(photo)))
                else:
                    self.ImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/image_add.png")))
            elif photo == None:
                self.ImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/image_add.png")))
            #INSERTING THE DATA ONTO THE GUI
            self.AgeEdit.setText(Age)
            self.NameEdit.setText(Name)
            self.ClassEdit.setText(facaulty)
            self.GenderEdit.setText(gender)
        except:
            self.ImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/image_add.png")))
            pass
        conn.close()
        self.StatusEdit.clear()
        self.StatusEdit.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setText(str(self.current + 1))
        self.ShowBooks()
        self.TitleLogo()

    def TitleLogo(self):
        try:
            connC = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
            cC = connC.cursor()
            cC.execute("SELECT * FROM configs")
            data6 = cC.fetchall()
            connC.close()
            if len(data6[0][1])>0:
                self.LibName.setText(str(data6[0][1]))
            else:
                pass
            if len(data6[0][2])>0:
                self.LogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(data6[0][2])))
            else:
                pass
        except:
            pass

    def NewUser(self):
        self.read_from_db()
        self.current = len(data)-1
        self.read_from_db()

    def NewStudent(self):
        self.NewstdDialog = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.NewstdDialog)
        self.NewstdDialog.show()
        self.ui.buttonBox.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.NewUser)

    def AboutPage(self):
    	self.aboutstuff = QtGui.QDialog()
    	self.ui = Ui_DialogA()
    	self.ui.setupUi(self.aboutstuff)
    	self.aboutstuff.show()

    def Configurator(self):
        self.confs = QtGui.QDialog()
        self.ui = Ui_DialogCF()
        self.ui.setupUi(self.confs)
        self.confs.show()
        self.ui.buttonBox.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ui.condetails)
        self.ui.buttonBox.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.refresh)

    def UpdateNote(self):
        self.UpdateDone = QtGui.QDialog()
        self.ui = Ui_DialogU()
        self.ui.setupUi(self.UpdateDone)
        self.UpdateDone.show()

    def DelConfirm(self):
        self.DelNote = QtGui.QDialog()
        self.ui = Ui_DialogD()
        self.ui.setupUi(self.DelNote)
        self.DelNote.show()
        self.ui.buttonBox.Ok.conjugate()
        self.ui.buttonBox.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.EraseProfile)

    def next_clicked(self):
        if self.current < len(data)-1:
            self.current += 1
            self.IssuedLabel.setText(_translate("mainWindow", '00-00-00', None))
            self.DueLabel.setText(_translate("mainWindow", '00-00-00', None))
            self.read_from_db()

    def back_clicked(self):
        if self.current > 0 :
            self.current -= 1
            self.IssuedLabel.setText(_translate("mainWindow", '00-00-00', None))
            self.DueLabel.setText(_translate("mainWindow", '00-00-00', None))
            self.read_from_db()

    def refresh(self):
        self.IssuedLabel.setText(_translate("mainWindow", "00-00-00", None))
        self.DueLabel.setText(_translate("mainWindow", "00-00-00", None))
        self.read_from_db()

    def EraseProfile(self):
        try:
            conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
            c = conn.cursor()
            c.execute("DELETE FROM students WHERE id_students=(%s)", (str(data[self.current][0]),))
            conn.commit()
            if len(data)==1:
                self.NameEdit.clear()
                self.AgeEdit.clear()
                self.ClassEdit.clear()
                self.GenderEdit.clear()
                self.StatusEdit.clear()
                self.refresh()
                self.read_from_db()
                print "done"
            else:
                self.read_from_db()
            if self.current==len(data)-1:
                self.current -= 1
                self.read_from_db()
            else:
                self.current = len(data)-1
                self.read_from_db()
        except:
            print "u have no profiles"
        conn.close()

    def UploadImager(self):
        self.Imagor = QFileDialog()
        global imgr
        imgr = self.Imagor.getOpenFileName()
        if len(imgr) > 0:
            self.ImageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(imgr)))

    def Updator(self):
        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c = conn.cursor()
        try:
            try:
                self.foto = imgr
                c.execute("UPDATE students SET name=(%s), gender=(%s), class=(%s), photo=(%s) WHERE id_students=(%s)",\
                    (self.NameEdit.text(), self.GenderEdit.text(), self.ClassEdit.text(), self.foto, data[self.current][0]))
                conn.commit()
            except:
                c.execute("UPDATE students SET name=(%s), gender=(%s), class=(%s) WHERE id_students=(%s)",\
                    (self.NameEdit.text(), self.GenderEdit.text(), self.ClassEdit.text(), data[self.current][0]))
                conn.commit()
                self.UpdateNote()
        except IndexError:
            print "you have no profiles to update"
            pass
        conn.close()
        self.UpdateNote()

    def BorrowBooks(self):
        conne = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c2 = conne.cursor()
        c2.execute("SELECT * FROM books")
        data2 = c2.fetchall()
        try:
            connex = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
            c7 = connex.cursor()
            c7.execute("SELECT graceperiod FROM configs")
            data7 = c7.fetchall()[0][0]
            thisDay = str(time.time())
            dueDay = str(float(thisDay) + (int(data7)* 24*3600))
        except:
            thisDay = str(time.time())
            dueDay = str(float(thisDay) + (7* 24*3600))
        #WORKING AROUND WITH DATES FOR THE DUEDATE AND THE DATE OF ISSUE
        if len(self.BorrowEdit.toPlainText())>0:
            if data2[self.current][2]!=None:
                c2.execute("INSERT INTO books(id_students, bk_titles, doi, duedate) VALUES \
                (%s, %s, %s, %s)",(data[self.current][0], self.BorrowEdit.toPlainText(), thisDay, dueDay))
                conne.commit()
            elif data2[self.current][2]==None:
                c2.execute("UPDATE books SET bk_titles=(%s), doi=(%s), duedate=(%s) WHERE id_students=(%s)",
                    (str(self.BorrowEdit.toPlainText()), thisDay, dueDay, data[self.current][0]))
                conne.commit()
        else:
            print "Nothing in the textfield"
        conne.close()
        self.BorrowEdit.clear()
        self.read_from_db()

    def ShowBooks(self):
        conne = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c2 = conne.cursor()
        try:
            x = str(data[self.current][0])
            c2.execute("SELECT * FROM books WHERE id_students = (%s)", (x,))
            global data2
            data2 = c2.fetchall()
            self.booklist = []
            if len(data2)>0:
                for i in data2:
                    if i[2]!=None:
                        self.booklist.append(i[2])
                    elif i[2]==None:
                        pass
                self.listView = QtGui.QListView(self.centralwidget)
                self.listView.setObjectName(_fromUtf8("listView"))
                self.listView.setFixedSize(306,111)
                self.gridLayout.addWidget(self.listView, 10, 1, 2, 5)
                self.listView.setStatusTip(_translate("mainWindow", "Select book to view date details", None))
                self.model = QtGui.QStringListModel(self.booklist)
                blist = QtGui.QListView(self.listView)
                blist.setFixedSize(306,111)
                blist.setModel(self.model)
                blist.clicked.connect(self.yesiah)
                blist.clicked.connect(self.bookdates)
        except:
            self.listView = QtGui.QListView(self.centralwidget)
            self.listView.setObjectName(_fromUtf8("listView"))
            self.listView.setFixedSize(306,111)
            self.gridLayout.addWidget(self.listView, 10, 1, 2, 5)
            self.listView.setStatusTip(_translate("mainWindow", "Select book to view date details", None))
        self.bookdates
        conne.close()

    def yesiah(self, QModelIndex):
        self.scrapy = self.booklist[QModelIndex.row()]
        global bkname
        bkname = self.booklist[QModelIndex.row()]

    def bookdates(self, QModelIndex):
        connez = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c8 = connez.cursor()
        try:
            y = str(data[self.current][0])
            c8.execute("SELECT doi,duedate FROM books WHERE id_students = (%s)", (y,))
            data8 = c8.fetchall()
            preDoi = str(datetime.datetime.fromtimestamp(data8[QModelIndex.row()][0]).strftime("%d-%m-%Y %H:%M"))
            preDuedate = str(datetime.datetime.fromtimestamp(data8[QModelIndex.row()][1]).strftime("%d-%m-%Y %H:%M"))
            self.IssuedLabel.setText(_translate("mainWindow", preDoi, None))
            self.DueLabel.setText(_translate("mainWindow", preDuedate, None))
            thisDay = time.time()
            if (float(data8[QModelIndex.row()][1]) - thisDay) > 0:
                print "good"
                self.Status = "GOOD"
            elif (float(data8[QModelIndex.row()][1]) - thisDay) == 0:
                self.Status = 'Due Today'
            elif (float(data8[QModelIndex.row()][1]) - thisDay) < 0:
                self.Status = "OVERDUE"
            self.StatusEdit.setText(_translate("mainWindow", self.Status, None))
        except:
            pass
        connez.close()

    def ClearBooks(self):
        connec = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c3 = connec.cursor()
        #THE ERASOR FUNCTION IS MEANT TO DELETE SOME DATABASE ENTRIES LEAVING ONLY ONE ROW FOR EACH STUDENT WITH VALUES SET TO NULL
        self.yesiah
        def TheErasor():
            try:
                y = str(data[self.current][0])
                c3.execute("SELECT bk_titles FROM books WHERE id_students = (%s)", (y,))
                data3 = c3.fetchall()
                if len(data3)==1 :
                    c3.execute("UPDATE books SET bk_titles=Null, doi=Null, duedate=Null WHERE id_students=(%s)", (str(data[self.current][0]),))
                    connec.commit()
                    print "first condition satisfied"
                elif len(data3)>1:
                    c3.execute("DELETE FROM books WHERE bk_titles=(%s)", (str(bkname),))
                    connec.commit()
                    print 'second condition satisfied'
            except:
                print "Please select a book"
                pass
        TheErasor()
        connec.close()
        self.read_from_db()

    def StudList(self):
        self.Studlisted = QtGui.QDialog()
        self.ui = Ui_DialogS()
        self.ui.setupUi(self.Studlisted)
        self.Studlisted.show()
        connek = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c4 = connek.cursor()
        c4.execute("SELECT name FROM students")
        data5 = c4.fetchall()
        self.allstudents = []
        for i in data5:
            self.allstudents.append(i[0])
        model2 = QtGui.QStringListModel(self.allstudents)
        blist2 = QtGui.QListView(self.ui.listView)
        blist2.setFixedSize(340,481)
        blist2.setModel(model2)
        blist2.show()
        blist2.clicked.connect(self.ClickedStd)
        connek.close()

    def ClickedStd(self, QModelIndex):
        try:
            klikdStd = self.allstudents[QModelIndex.row()]
            data12=[]
            for i in data:
                data12.append(i[1])
            self.current = data12.index((str(klikdStd)))
            self.read_from_db()
        except:
            pass

    def BukList(self):
        self.bkList = QtGui.QDialog()
        self.ui = Ui_DialogB()
        self.ui.setupUi(self.bkList)
        self.bkList.show()
        self.ui.textEdit.setReadOnly(True)
        connek = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c4 = connek.cursor()
        c4.execute("SELECT bk_titles FROM books")
        try:
            data5 = c4.fetchall()
            indx = 1
            for i in data5:
                if i[0] != None:
                    indxdname = str(indx)+". "+ str(i[0])
                    self.ui.textEdit.insertPlainText(indxdname)
                    self.ui.textEdit.insertPlainText("\n")
                    indx += 1
                else:
                    continue
        except:
            pass

    def Overdew(self):
        self.OvaDew = QtGui.QDialog()
        self.ui = Ui_DialogO()
        self.ui.setupUi(self.OvaDew)
        self.OvaDew.show()
        connek = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c4 = connek.cursor()
        c4.execute("SELECT duedate,bk_titles FROM books")
        data5 = c4.fetchall()
        indx = 1
        thisDay = time.time()
        self.ui.textEdit.setReadOnly(True)
        for i in data5:
            if i[0] != None:
                status = float(i[0]) - thisDay
                if status < 0 :
                    indxdname = str(indx)+". "+ str(i[1])
                    self.ui.textEdit.insertPlainText(indxdname)
                    self.ui.textEdit.insertPlainText("\n")
                    indx += 1
                else:
                    continue
            else:
                continue
        connek.close()

    def BlacListed(self):
        self.blaqlisted = QtGui.QDialog()
        self.ui = Ui_DialogX()
        self.ui.setupUi(self.blaqlisted)
        self.blaqlisted.show()
        connek = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c4 = connek.cursor()
        c4.execute("SELECT duedate,bk_titles, id_students FROM books")
        try:
            data5 = c4.fetchall()
            print data5
            thisDay = time.time()
            self.blacked = []
            for i in data5:
                if i[0] != None:
                    status = float(i[0]) - thisDay
                    # print status
                    if status < 0 :
                        conn = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
                        c45 = conn.cursor()
                        c45.execute("SELECT name FROM students WHERE id_students=(%s)", (str(i[2]),))
                        data6 = c45.fetchall()
                        for i in data6:
                            if i[0] not in self.blacked:
                                self.blacked.append(i[0])
            model3 = QtGui.QStringListModel(self.blacked)
            blist3 = QtGui.QListView(self.ui.listView)
            blist3.setFixedSize(340,478)
            blist3.setModel(model3)
            blist3.show()
            blist3.clicked.connect(self.KlickedStd)
            connek.close()
        except:
            pass

    def SearchThem(self):
        self.lookout = QtGui.QDialog()
        self.ui = Ui_SearchDialog()
        self.ui.setupUi(self.lookout)
        self.lookout.show()
        connek = MySQLdb.connect(host='localhost', user='LibMan', passwd='libman23', db='librarysys')
        c4 = connek.cursor()
        c4.execute("SELECT name FROM students WHERE name REGEXP(%s)",(str(self.SearchEdit.text()),))
        Sdata = c4.fetchall()
        self.foundStd=[]
        for i in Sdata:
            self.foundStd.append(i[0])
        print self.foundStd
        model4 = QtGui.QStringListModel(self.foundStd)
        Slist4 = QtGui.QListView(self.ui.listView)
        Slist4.setFixedSize(262,270)
        Slist4.setModel(model4)
        Slist4.show()
        Slist4.clicked.connect(self.FoundKlikd)

    def FoundKlikd(self, QModelIndex):
        try:
            klikdStdnt = self.foundStd[QModelIndex.row()]
            dataF = []
            for i in data:
                dataF.append(i[1])
            self.current = dataF.index((str(klikdStdnt)))
            self.read_from_db()
        except:
            pass

    def KlickedStd(self, QModelIndex):
        try:
            klikdStd = self.blacked[QModelIndex.row()]
            data12=[]
            for i in data:
                data12.append(i[1])
            self.current = data12.index((str(klikdStd)))
            self.read_from_db()
        except:
            pass

    def QuitClicked(self):
        sys.exit()
        
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(760, 586)
        mainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        mainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/library.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setStatusTip(_fromUtf8(""))
        mainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.DeleteButton = QtGui.QPushButton(self.centralwidget)
        self.DeleteButton.setMaximumSize(QtCore.QSize(91, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/Remove-Male-User.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon1)
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.gridLayout.addWidget(self.DeleteButton, 17, 8, 1, 1)
        self.BorrowEdit = QtGui.QTextEdit(self.centralwidget)
        self.BorrowEdit.setMaximumSize(QtCore.QSize(16777215, 111))
        self.BorrowEdit.setStyleSheet(_fromUtf8("color:rgb(255, 170, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";"))
        self.BorrowEdit.setObjectName(_fromUtf8("BorrowEdit"))
        self.gridLayout.addWidget(self.BorrowEdit, 10, 8, 2, 4)
        self.UpdateButton = QtGui.QPushButton(self.centralwidget)
        self.UpdateButton.setMaximumSize(QtCore.QSize(91, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/Edit-Male-User.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpdateButton.setIcon(icon2)
        self.UpdateButton.setObjectName(_fromUtf8("UpdateButton"))
        self.gridLayout.addWidget(self.UpdateButton, 17, 5, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(64, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 8, 4, 1, 1)
        self.RefreshButton = QtGui.QPushButton(self.centralwidget)
        self.RefreshButton.setMaximumSize(QtCore.QSize(91, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/arrow_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RefreshButton.setIcon(icon3)
        self.RefreshButton.setObjectName(_fromUtf8("RefreshButton"))
        self.gridLayout.addWidget(self.RefreshButton, 17, 3, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 9, 0, 1, 12)
        ######################################################################
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.NameEdit = QtGui.QLineEdit(self.centralwidget)
        self.NameEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NameEdit.setFont(font)
        self.NameEdit.setStyleSheet(_fromUtf8("color:rgb(0, 0, 255)"))
        self.NameEdit.setObjectName(_fromUtf8("NameEdit"))
        self.gridLayout.addWidget(self.NameEdit, 3, 1, 1, 8)
        self.SearchButton = QtGui.QPushButton(self.centralwidget)
        self.SearchButton.setMaximumSize(QtCore.QSize(41, 31))
        self.SearchButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/magnifier.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon4)
        self.SearchButton.setObjectName(_fromUtf8("SearchButton"))
        self.gridLayout.addWidget(self.SearchButton, 1, 11, 1, 1)
        self.LogoLabel = QtGui.QLabel(self.centralwidget)
        self.LogoLabel.setMaximumSize(QtCore.QSize(91, 81))
        self.LogoLabel.setFrameShape(QtGui.QFrame.Panel)
        self.LogoLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.LogoLabel.setText(_fromUtf8(""))
        self.LogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/library.ico")))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setObjectName(_fromUtf8("LogoLabel"))
        self.gridLayout.addWidget(self.LogoLabel, 0, 0, 2, 1)
        self.LibName = QtGui.QLabel(self.centralwidget)
        self.LibName.setMaximumSize(QtCore.QSize(16777215, 41))
        self.LibName.setFrameShape(QtGui.QFrame.Box)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.LibName.setFont(font)
        self.LibName.setFrameShadow(QtGui.QFrame.Sunken)
        self.LibName.setObjectName(_fromUtf8("LibName"))
        self.gridLayout.addWidget(self.LibName, 0, 1, 1, 11)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.AgeEdit = QtGui.QLineEdit(self.centralwidget)
        self.AgeEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AgeEdit.setFont(font)
        self.AgeEdit.setStyleSheet(_fromUtf8("color:rgb(0, 0, 255)"))
        self.AgeEdit.setObjectName(_fromUtf8("AgeEdit"))
        self.gridLayout.addWidget(self.AgeEdit, 4, 1, 1, 8)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.GenderEdit = QtGui.QLineEdit(self.centralwidget)
        self.GenderEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GenderEdit.setFont(font)
        self.GenderEdit.setStyleSheet(_fromUtf8("color:rgb(0, 0, 255)"))
        self.GenderEdit.setObjectName(_fromUtf8("GenderEdit"))
        self.gridLayout.addWidget(self.GenderEdit, 6, 1, 1, 8)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.ClassEdit = QtGui.QLineEdit(self.centralwidget)
        self.ClassEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClassEdit.setFont(font)
        self.ClassEdit.setStyleSheet(_fromUtf8("color:rgb(0, 0, 255)"))
        self.ClassEdit.setObjectName(_fromUtf8("ClassEdit"))
        self.gridLayout.addWidget(self.ClassEdit, 5, 1, 1, 8)
        self.StatusEdit = QtGui.QLineEdit(self.centralwidget)
        self.StatusEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StatusEdit.setFont(font)
        self.StatusEdit.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)"))
        self.StatusEdit.setObjectName(_fromUtf8("StatusEdit"))
        self.gridLayout.addWidget(self.StatusEdit, 7, 1, 1, 6)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(207, 20))
        self.lineEdit_7.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);\n"
"font: 11pt \"Virtual DJ\";"))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 2, 3, 1, 1)
        self.UploadButton = QtGui.QPushButton(self.centralwidget)
        self.UploadButton.setMaximumSize(QtCore.QSize(81, 23))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/image_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UploadButton.setIcon(icon5)
        self.UploadButton.setObjectName(_fromUtf8("UploadButton"))
        self.gridLayout.addWidget(self.UploadButton, 7, 9, 1, 1)
        self.SearchEdit = QtGui.QLineEdit(self.centralwidget)
        self.SearchEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.SearchEdit.setStyleSheet(_fromUtf8("color:rgb(0, 0, 255)"))
        self.SearchEdit.setObjectName(_fromUtf8("SearchEdit"))
        self.gridLayout.addWidget(self.SearchEdit, 1, 7, 1, 4)
        self.ImageLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMaximumSize(QtCore.QSize(171, 151))
        self.ImageLabel.setToolTip(_fromUtf8(""))
        self.ImageLabel.setAutoFillBackground(False)
        self.ImageLabel.setFrameShape(QtGui.QFrame.Panel)
        self.ImageLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.ImageLabel.setText(_fromUtf8(""))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName(_fromUtf8("ImageLabel"))
        self.gridLayout.addWidget(self.ImageLabel, 3, 9, 4, 3)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setMaximumSize(QtCore.QSize(64, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.NextButton = QtGui.QPushButton(self.centralwidget)
        self.NextButton.setMaximumSize(QtCore.QSize(91, 23))
        self.NextButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon6)
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.gridLayout.addWidget(self.NextButton, 17, 10, 1, 2)
        self.BorrowButton = QtGui.QPushButton(self.centralwidget)
        self.BorrowButton.setMaximumSize(QtCore.QSize(81, 23))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/book_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BorrowButton.setIcon(icon7)
        self.BorrowButton.setObjectName(_fromUtf8("BorrowButton"))
        self.gridLayout.addWidget(self.BorrowButton, 11, 7, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 10, 7, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 14, 0, 1, 12)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 18, 0, 1, 12)
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setMaximumSize(QtCore.QSize(101, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/book_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon8)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 11, 0, 1, 1)
        self.BackButton = QtGui.QPushButton(self.centralwidget)
        self.BackButton.setMaximumSize(QtCore.QSize(91, 23))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon9)
        self.BackButton.setObjectName(_fromUtf8("BackButton"))
        self.gridLayout.addWidget(self.BackButton, 17, 0, 1, 1)
        self.IssuedLabel = QtGui.QLabel(self.centralwidget)
        self.IssuedLabel.setMaximumSize(QtCore.QSize(155, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IssuedLabel.setFont(font)
        self.IssuedLabel.setStyleSheet(_fromUtf8("color:rgb(0, 170, 0);"))
        self.IssuedLabel.setFrameShape(QtGui.QFrame.Box)
        self.IssuedLabel.setObjectName(_fromUtf8("IssuedLabel"))
        self.gridLayout.addWidget(self.IssuedLabel, 12, 2, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 12, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 12, 8, 1, 1)
        self.DueLabel = QtGui.QLabel(self.centralwidget)
        self.DueLabel.setMaximumSize(QtCore.QSize(156, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DueLabel.setFont(font)
        self.DueLabel.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0);"))
        self.DueLabel.setFrameShape(QtGui.QFrame.Box)
        self.DueLabel.setObjectName(_fromUtf8("DueLabel"))
        self.gridLayout.addWidget(self.DueLabel, 12, 9, 1, 3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStudents = QtGui.QMenu(self.menubar)
        self.menuStudents.setObjectName(_fromUtf8("menuStudents"))
        self.menuBooks = QtGui.QMenu(self.menubar)
        self.menuBooks.setObjectName(_fromUtf8("menuBooks"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(mainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/Add-Male-User.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon10)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionView_All = QtGui.QAction(mainWindow)
        self.actionView_All.setObjectName(_fromUtf8("actionView_All"))
        self.actionBlacklisted = QtGui.QAction(mainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/Male-User-Warning.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBlacklisted.setIcon(icon11)
        self.actionBlacklisted.setObjectName(_fromUtf8("actionBlacklisted"))
        self.actionDelete = QtGui.QAction(mainWindow)
        self.actionDelete.setIcon(icon1)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionBorrowed = QtGui.QAction(mainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/book.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBorrowed.setIcon(icon12)
        self.actionBorrowed.setObjectName(_fromUtf8("actionBorrowed"))
        self.actionOverDue = QtGui.QAction(mainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/book_error.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOverDue.setIcon(icon13)
        self.actionOverDue.setObjectName(_fromUtf8("actionOverDue"))
        self.actionConfigurations = QtGui.QAction(mainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/Office/OfficePack/wheel.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigurations.setIcon(icon14)
        self.actionConfigurations.setObjectName(_fromUtf8("actionConfigurations"))
        self.actionDocumentation = QtGui.QAction(mainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuStudents.addAction(self.actionNew)
        self.menuStudents.addAction(self.actionView_All)
        self.menuStudents.addSeparator()
        self.menuStudents.addAction(self.actionBlacklisted)
        self.menuStudents.addAction(self.actionDelete)
        self.menuStudents.addSeparator()
        self.menuStudents.addAction(self.actionQuit)
        self.menuBooks.addAction(self.actionBorrowed)
        self.menuBooks.addAction(self.actionOverDue)
        self.menuHelp.addAction(self.actionConfigurations)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuStudents.menuAction())
        self.menubar.addAction(self.menuBooks.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.AgeEdit.setReadOnly(True)
        #THE FOLLOWING ARE BUTTONS FOR THE ABOVE FUNCTIONS:
        self.read_from_db()
        self.NextButton.clicked.connect(self.next_clicked)
        self.BackButton.clicked.connect(self.back_clicked)
        self.RefreshButton.clicked.connect(self.refresh)
        self.DeleteButton.clicked.connect(self.DelConfirm)
        self.UploadButton.clicked.connect(self.UploadImager)
        self.UpdateButton.clicked.connect(self.Updator)
        self.BorrowButton.clicked.connect(self.BorrowBooks)
        self.clearButton.clicked.connect(self.ClearBooks)
        self.clearButton.clicked.connect(self.refresh)
        self.SearchButton.clicked.connect(self.SearchThem)
        #CONFIGURING ACTION FUNCTIONS
        self.actionNew.connect(self.actionNew, QtCore.SIGNAL("triggered()"), self.NewStudent)
        self.actionQuit.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), self.QuitClicked)
        self.actionDelete.connect(self.actionDelete, QtCore.SIGNAL("triggered()"), self.DelConfirm)
        self.actionView_All.connect(self.actionView_All, QtCore.SIGNAL("triggered()"), self.StudList)
        self.actionBorrowed.connect(self.actionBorrowed, QtCore.SIGNAL("triggered()"), self.BukList)
        self.actionOverDue.connect(self.actionOverDue, QtCore.SIGNAL("triggered()"), self.Overdew)
        self.actionBlacklisted.connect(self.actionBlacklisted, QtCore.SIGNAL("triggered()"), self.BlacListed)
        self.actionConfigurations.connect(self.actionConfigurations, QtCore.SIGNAL("triggered()"), self.Configurator)
        self.actionAbout.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), self.AboutPage)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Library Management System", None))
        self.label_8.setText(_translate("mainWindow", "Borrowed :", None))
        self.DeleteButton.setStatusTip(_translate("mainWindow", "delete this student`s profile", None))
        self.DeleteButton.setText(_translate("mainWindow", "Delete", None))
        self.BorrowEdit.setStatusTip(_translate("mainWindow", "type title of the book you want to borrow", None))
        self.UpdateButton.setStatusTip(_translate("mainWindow", "Update the profile details", None))
        self.UpdateButton.setText(_translate("mainWindow", "Update", None))
        self.label_11.setText(_translate("mainWindow", "BOOKS :", None))
        self.RefreshButton.setStatusTip(_translate("mainWindow", "Update the profile details", None))
        self.RefreshButton.setText(_translate("mainWindow", "Refresh", None))
        self.label_2.setText(_translate("mainWindow", "Name   :", None))
        self.SearchButton.setStatusTip(_translate("mainWindow", "search button", None))
        self.LogoLabel.setStatusTip(_translate("mainWindow", "that is the library logo", None))
        self.LibName.setStatusTip(_translate("mainWindow", "thats the library name", None))
        self.LibName.setText(_translate("mainWindow", "Library Name", None))
        self.label_3.setText(_translate("mainWindow", "Age      :", None))
        self.label_4.setText(_translate("mainWindow", "Class    :", None))
        self.label_6.setText(_translate("mainWindow", "Status   :", None))
        self.label_5.setText(_translate("mainWindow", "Gender :", None))
        self.UploadButton.setStatusTip(_translate("mainWindow", "click to place your photo", None))
        self.UploadButton.setText(_translate("mainWindow", "Upload", None))
        self.SearchEdit.setStatusTip(_translate("mainWindow", "enter name and press the search button", None))
        self.SearchEdit.setPlaceholderText(_translate("mainWindow", "search student here", None))
        self.ImageLabel.setStatusTip(_translate("mainWindow", "place image", None))
        self.ImageLabel.setWhatsThis(_translate("mainWindow", "PLACE IMAGE", None))
        self.label_10.setText(_translate("mainWindow", "Roll Number :", None))
        self.NextButton.setStatusTip(_translate("mainWindow", "go to the next student", None))
        self.NextButton.setText(_translate("mainWindow", "Next", None))
        self.NextButton.setShortcut(_translate("mainWindow", "Right", None))
        self.BorrowButton.setText(_translate("mainWindow", "Borrow", None))
        self.label_9.setText(_translate("mainWindow", "Borrow :", None))
        self.clearButton.setStatusTip(_translate("mainWindow", "click to clear the selected books", None))
        self.clearButton.setText(_translate("mainWindow", "Clear_Selected", None))
        self.BackButton.setStatusTip(_translate("mainWindow", "go to the previous student", None))
        self.BackButton.setText(_translate("mainWindow", "Back", None))
        self.BackButton.setShortcut(_translate("mainWindow", "Left", None))
        self.IssuedLabel.setText(_translate("mainWindow", "00-00-00", None))
        self.label.setText(_translate("mainWindow", "Issued On:", None))
        self.label_12.setText(_translate("mainWindow", "Due Date :", None))
        self.DueLabel.setText(_translate("mainWindow", "00-00-00", None))
        self.menuStudents.setTitle(_translate("mainWindow", "Students", None))
        self.menuBooks.setTitle(_translate("mainWindow", "Books", None))
        self.menuHelp.setTitle(_translate("mainWindow", "Help", None))
        self.actionNew.setText(_translate("mainWindow", "New ", None))
        self.actionNew.setShortcut(_translate("mainWindow", "Ctrl+N", None))
        self.actionView_All.setText(_translate("mainWindow", "View All", None))
        self.actionView_All.setStatusTip(_translate("mainWindow", "view all the students grouped by classes", None))
        self.actionBlacklisted.setText(_translate("mainWindow", "Blacklisted", None))
        self.actionDelete.setText(_translate("mainWindow", "Delete  ", None))
        self.actionDelete.setShortcut(_translate("mainWindow", "Ctrl+D", None))
        self.actionQuit.setText(_translate("mainWindow", "Quit ", None))
        self.actionQuit.setShortcut(_translate("mainWindow", "Ctrl+Q", None))
        self.actionBorrowed.setText(_translate("mainWindow", "Borrowed", None))
        self.actionOverDue.setText(_translate("mainWindow", "OverDue", None))
        self.actionConfigurations.setText(_translate("mainWindow", "Configurations", None))
        self.actionDocumentation.setText(_translate("mainWindow", "Documentation", None))
        self.actionAbout.setText(_translate("mainWindow", "About", None))

import officeIcoz

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

