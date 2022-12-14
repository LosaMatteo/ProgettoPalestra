from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi.Metodi import Metodi
from Attrezzo.Model.Attrezzo import Attrezzo
from Attrezzo.Controller.ControllerAttrezzo import ControllerAttrezzo


class ViewAggiungiAttrezzo(object):
    objMetodi = Metodi()

    def __init__(self, aggiorna_attrezzi):
        self.aggiorna_attrezzi = aggiorna_attrezzi
        self.controller = ControllerAttrezzo()

    def salva_attrezzatura(self):
        try:
            if self.txtDescr.text() != "" and self.dtAcquisto.text() != "" and self.txtQuantita.text() != "" and\
                                   self.txtPrezzo.text() != "" and self.dtMan.text() != "":
                nuovo_attrezzo = Attrezzo(self.txtDescr.text(), self.dtAcquisto.text(), self.txtQuantita.text(),
                                          self.txtPrezzo.text(), self.dtMan.text())
                self.controller.aggiungi_attrezzo(nuovo_attrezzo)
                self.aggiorna_attrezzi()
                self.view_aggiungi_attrezzo.close()
            else:
                self.objMetodi.show_popup_exception("È necessario riempire ogni campo.")
        except Exception:
            self.objMetodi.show_popup_exception("Errore.")

    def setupUi(self, MainWindow):
        self.view_aggiungi_attrezzo = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(90, 30, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.txtDescr = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDescr.setGeometry(QtCore.QRect(410, 150, 201, 21))
        self.txtDescr.setObjectName("txtDescr")
        self.lblDescr = QtWidgets.QLabel(self.centralwidget)
        self.lblDescr.setGeometry(QtCore.QRect(160, 150, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblDescr.setFont(font)
        self.lblDescr.setObjectName("lblDescr")
        self.dtAcquisto = QtWidgets.QDateEdit(self.centralwidget)
        self.dtAcquisto.setGeometry(QtCore.QRect(410, 210, 141, 22))
        self.dtAcquisto.setObjectName("dtAcquisto")
        self.dtAcquisto.setDate(QDate.currentDate())
        self.lblAcquisto = QtWidgets.QLabel(self.centralwidget)
        self.lblAcquisto.setGeometry(QtCore.QRect(160, 210, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblAcquisto.setFont(font)
        self.lblAcquisto.setObjectName("lblAcquisto")
        self.lblQuantita = QtWidgets.QLabel(self.centralwidget)
        self.lblQuantita.setGeometry(QtCore.QRect(160, 270, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblQuantita.setFont(font)
        self.lblQuantita.setObjectName("lblQuantita")
        self.txtQuantita = QtWidgets.QLineEdit(self.centralwidget)
        self.txtQuantita.setGeometry(QtCore.QRect(410, 270, 201, 21))
        self.txtQuantita.setObjectName("txtQuantita")
        self.lblPrezzo = QtWidgets.QLabel(self.centralwidget)
        self.lblPrezzo.setGeometry(QtCore.QRect(160, 330, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblPrezzo.setFont(font)
        self.lblPrezzo.setObjectName("lblPrezzo")
        self.txtPrezzo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrezzo.setGeometry(QtCore.QRect(410, 330, 201, 21))
        self.txtPrezzo.setObjectName("txtPrezzo")
        self.lblMan = QtWidgets.QLabel(self.centralwidget)
        self.lblMan.setGeometry(QtCore.QRect(160, 390, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblMan.setFont(font)
        self.lblMan.setObjectName("lblMan")
        self.dtMan = QtWidgets.QDateEdit(self.centralwidget)
        self.dtMan.setGeometry(QtCore.QRect(410, 390, 141, 22))
        self.dtMan.setObjectName("dtMan")
        self.dtMan.setDate(QDate.currentDate())
        self.btnAnnulla = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnnulla.setGeometry(QtCore.QRect(200, 460, 101, 31))
        self.btnAnnulla.setObjectName("btnAnnulla")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(450, 460, 101, 31))
        self.btnSalva.setObjectName("btnSalva")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSalva.clicked.connect(self.salva_attrezzatura)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aggiunta attrezzo"))
        self.lblTitle.setText(_translate("MainWindow", "Aggiungi un nuovo attrezzo o macchinario"))
        self.lblDescr.setText(_translate("MainWindow", "Aggiungi una breve descrizione"))
        self.lblAcquisto.setText(_translate("MainWindow", "Seleziona la data di acquisto"))
        self.lblQuantita.setText(_translate("MainWindow", "Inserisci la quantità acquistata"))
        self.lblPrezzo.setText(_translate("MainWindow", "Inserisci il prezzo unitario"))
        self.lblMan.setText(_translate("MainWindow", "Seleziona la data di manutenzione "))
        self.btnAnnulla.setText(_translate("MainWindow", "Annulla"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))