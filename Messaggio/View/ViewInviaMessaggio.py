from PyQt5 import QtCore, QtGui, QtWidgets
from Metodi.Metodi import Metodi
from Messaggio.Model.Messaggio import Messaggio
from Messaggio.Controller.ControllerMessaggio import ControllerMessaggio
from datetime import datetime


class ViewInviaMessaggio(object):
    objMetodi = Metodi()

    def __init__(self, username, aggiorna_messaggi):
        self.username = username
        self.aggiorna_messaggi = aggiorna_messaggi
        self.controller = ControllerMessaggio()

    def popola_combobox(self):
        self.lblMittente.setText(self.username)
        if self.username != "Admin":
            self.cmbDestinatari.addItem("A-Admin")
        for elem in self.controller.get_lista_clienti():
            if elem != self.username:
                self.cmbDestinatari.addItem("C-" + elem)
        for elem in self.controller.get_lista_staff():
            if elem != self.username:
                self.cmbDestinatari.addItem("P-" + elem)

    def scrittura_file_messaggi(self):
        esito_invio = False
        if self.chkClienti.isChecked() == False and self.chkStaff.isChecked() == False:
            destinatario = self.cmbDestinatari.currentText().split("-")
            nuovo_messaggio = Messaggio(self.username, destinatario[1], self.ptxTesto.toPlainText(),
                                        datetime.today().strftime('%Y-%m-%d-%H:%M'))
            esito_invio = self.controller.spedisci_messaggio(nuovo_messaggio)
        if self.chkClienti.isChecked():
            for elem in self.controller.get_lista_clienti():
                messaggio_clienti = Messaggio(self.username, elem, self.ptxTesto.toPlainText(),
                                              datetime.today().strftime('%Y-%m-%d-%H:%M'))
                esito_invio = self.controller.spedisci_messaggio(messaggio_clienti)
        if self.chkStaff.isChecked():
            for elem in self.controller.get_lista_staff():
                messaggio_dipendenti = Messaggio(self.username, elem, self.ptxTesto.toPlainText(),
                                                 datetime.today().strftime('%Y-%m-%d-%H:%M'))
                esito_invio = self.controller.spedisci_messaggio(messaggio_dipendenti)
        if esito_invio:
            self.aggiorna_messaggi()
            self.objMetodi.show_popup_ok("il tuo contenuto è stato inviato correttamente")
        else:
            self.objMetodi.show_popup_exception("Impossibile mandare un messaggio vuoto.")
        self.view_invia_messaggio.close()

    def selezione_destinatario(self):
        self.cmbDestinatari.setDisabled(self.controller.selezione_destinatario(self.chkClienti.isChecked(),
                                                                               self.chkStaff.isChecked()))

    def setupUi(self, MainWindow):
        self.view_invia_messaggio = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTesto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_2.setGeometry(QtCore.QRect(40, 60, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_2.setFont(font)
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.btnInviaMessaggio = QtWidgets.QPushButton(self.centralwidget)
        self.btnInviaMessaggio.setGeometry(QtCore.QRect(360, 330, 141, 28))
        self.btnInviaMessaggio.setObjectName("btnInviaMessaggio")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(30, 30, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_3.setGeometry(QtCore.QRect(20, 90, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_3.setFont(font)
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.cmbDestinatari = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDestinatari.setGeometry(QtCore.QRect(90, 60, 151, 22))
        self.cmbDestinatari.setObjectName("cmbDestinatari")
        self.ptxTesto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxTesto.setGeometry(QtCore.QRect(90, 100, 421, 211))
        self.ptxTesto.setPlainText("")
        self.ptxTesto.setObjectName("ptxTesto")
        self.lblMittente = QtWidgets.QLabel(self.centralwidget)
        self.lblMittente.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblMittente.setFont(font)
        self.lblMittente.setText("")
        self.lblMittente.setObjectName("lblMittente")
        self.chkClienti = QtWidgets.QCheckBox(self.centralwidget)
        self.chkClienti.setGeometry(QtCore.QRect(280, 60, 91, 20))
        self.chkClienti.setObjectName("chkClienti")
        self.chkStaff = QtWidgets.QCheckBox(self.centralwidget)
        self.chkStaff.setGeometry(QtCore.QRect(400, 60, 91, 20))
        self.chkStaff.setObjectName("chkStaff")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if self.username != "Admin":
            self.chkStaff.hide()
            self.chkClienti.hide()
        self.popola_combobox()
        self.controller.recupera_messaggi()
        self.btnInviaMessaggio.clicked.connect(self.scrittura_file_messaggi)
        self.chkStaff.clicked.connect(self.selezione_destinatario)
        self.chkClienti.clicked.connect(self.selezione_destinatario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrivi messaggio"))
        self.lblTesto_2.setText(_translate("MainWindow", "A:"))
        self.btnInviaMessaggio.setText(_translate("MainWindow", "Invia Messaggio"))
        self.lblTesto_1.setText(_translate("MainWindow", "DA:"))
        self.lblTesto_3.setText(_translate("MainWindow", "Oggetto:"))
        self.chkClienti.setText(_translate("MainWindow", "Tutti i clienti"))
        self.chkStaff.setText(_translate("MainWindow", "Tutto lo staff"))
