from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from Cliente.View.ViewAggiungiCliente import ViewAggiungiCliente
from Cliente.View.ViewVisualizzaCliente import ViewVisualizzaCliente
from Attrezzo.View.ViewAggiungiAttrezzo import ViewAggiungiAttrezzo
from Staff.View.ViewAggiungiStaff import ViewAggiungiStaff
from Staff.View.ViewVisualizzaStaff import ViewVisualizzaStaff
from Metodi.Metodi import Metodi
from Messaggio.View.ViewInviaMessaggio import ViewInviaMessaggio
from Messaggio.View.ViewLeggiMessaggio import ViewLeggiMessaggio
from Messaggio.Controller.ControllerMessaggio import ControllerMessaggio
from Attrezzo.Controller.ControllerAttrezzo import ControllerAttrezzo


class ViewHomeAdmin(object):
    objMetodi = Metodi()
    controller_messaggio = ControllerMessaggio()
    controller_attrezzo = ControllerAttrezzo()
    riga = 0

    def __init__(self, username, lista_clienti, lista_staff, aggiorna_lista_clienti,
                 aggiorna_lista_staff):
        self.username = username
        self.lista_clienti = lista_clienti
        self.lista_staff = lista_staff
        self.aggiorna_lista_clienti = aggiorna_lista_clienti
        self.aggiorna_lista_staff = aggiorna_lista_staff

    def open_visualizza_cliente(self):
        try:
            if self.lstClienti.currentItem().isSelected():
                username = self.lstClienti.currentItem().text()
                self.visualizza_staff = QtWidgets.QMainWindow()
                self.ui = ViewVisualizzaCliente(username)
                self.ui.setupUi(self.visualizza_staff)
                self.visualizza_staff.show()
        except(Exception):
            self.objMetodi.show_popup_exception("Seleziona un cliente!")

    def open_aggiungi_cliente(self):
        self.aggiungi_cliente = QtWidgets.QMainWindow()
        self.ui = ViewAggiungiCliente(self.aggiorna_clienti)
        self.ui.setupUi(self.aggiungi_cliente)
        self.aggiungi_cliente.show()

    def open_visualizza_staff(self):
        try:
            if self.lstPersonale.currentItem().isSelected():
                nome = self.lstPersonale.currentItem().text()
                self.visualizza_staff = QtWidgets.QMainWindow()
                self.ui = ViewVisualizzaStaff(nome, self.aggiorna_staff)
                self.ui.setupUi(self.visualizza_staff)
                self.visualizza_staff.show()
        except(Exception):
            self.objMetodi.show_popup_exception("Seleziona un membro del personale!")

    def open_aggiungi_staff(self):
        self.aggiungi_staff = QtWidgets.QMainWindow()
        self.ui = ViewAggiungiStaff(self.aggiorna_staff)
        self.ui.setupUi(self.aggiungi_staff)
        self.aggiungi_staff.show()

    def open_aggiungi_attrezzo(self):
        self.visualizza_staff = QtWidgets.QMainWindow()
        self.ui = ViewAggiungiAttrezzo(self.aggiorna_attrezzi)
        self.ui.setupUi(self.visualizza_staff)
        self.visualizza_staff.show()

    def open_invia_messaggio(self):
        self.invia_messaggio = QtWidgets.QMainWindow()
        self.ui = ViewInviaMessaggio(self.username, self.visualizza_messaggi)
        self.ui.setupUi(self.invia_messaggio)
        self.invia_messaggio.show()

    def open_leggi_messaggio(self, messaggio):
        self.leggi_messaggio = QtWidgets.QMainWindow()
        self.ui = ViewLeggiMessaggio(self.username, messaggio, self.visualizza_messaggi)
        self.ui.setupUi(self.leggi_messaggio)
        self.leggi_messaggio.show()

    def visualizza_messaggi(self):
        self.lstMessaggi.clear()
        lista_messaggi = self.controller_messaggio.get_lista_messaggi_from_id(self.username)
        if lista_messaggi is not None:
            for elem in lista_messaggi:
                if elem.mittente == self.username:
                    self.lstMessaggi.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
                elif elem.destinatario == self.username:
                    self.lstMessaggi.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def restituisci_messaggio(self):
        riga = self.lstMessaggi.currentRow()
        messaggio = self.controller_messaggio.get_lista_messaggi_from_id(self.username)[riga]
        self.open_leggi_messaggio(messaggio)

    def elimina_messaggio(self):
        try:
            messaggio = self.controller_messaggio.get_lista_messaggi_from_id(self.username)[self.lstMessaggi.currentRow()]
            self.controller_messaggio.elimina_messaggio(messaggio)
            self.lstMessaggi.takeItem(self.lstMessaggi.currentRow())
            self.visualizza_messaggi()
        except(Exception):
            self.objMetodi.show_popup_exception("Non hai selezionato nessun messaggio")

    def rimuovi_attrezzo(self):
        try:
            if self.tblAttrezzi.currentItem().isSelected():
                self.controller_attrezzo.rimuovi_attrezzo(self.tblAttrezzi.currentRow())
                self.aggiorna_attrezzi()
        except(Exception):
            self.objMetodi.show_popup_exception("Non hai selezionato nulla nella tabella")

    def carica_clienti(self):
        self.lstClienti.clear()
        self.lista_clienti = self.aggiorna_lista_clienti()
        if self.lista_clienti is not None:
            for x in self.lista_clienti:
                self.lstClienti.addItem(x)

    def aggiorna_clienti(self):
        self.carica_clienti()

    def carica_staff(self):
        self.lstPersonale.clear()
        self.lista_staff = self.aggiorna_lista_staff()
        if self.lista_staff is not None:
            for x in self.lista_staff:
                self.lstPersonale.addItem(x)

    def aggiorna_staff(self):
        self.carica_staff()

    def carica_attrezzi(self):
        vettore = []
        lista = self.controller_attrezzo.popola_lista_attrezzi()
        if lista is not None:
            for x in lista:
                for j in x:
                    vettore.append(j)
        colonna = 0
        i = 0
        if self.riga != 0:
            temp = self.riga
            while temp != -1:
                self.tblAttrezzi.removeRow(temp)
                temp -= 1
                self.riga = 0
        while len(vettore) > i + 1:
            self.tblAttrezzi.insertRow(self.riga)
            self.tblAttrezzi.setItem(self.riga, colonna, QTableWidgetItem(vettore[i]))
            self.tblAttrezzi.setItem(self.riga, colonna + 1, QTableWidgetItem(vettore[i + 1]))
            self.tblAttrezzi.setItem(self.riga, colonna + 2, QTableWidgetItem(vettore[i + 2]))
            self.tblAttrezzi.setItem(self.riga, colonna + 3, QTableWidgetItem(vettore[i + 3]))
            self.tblAttrezzi.setItem(self.riga, colonna + 4, QTableWidgetItem(vettore[i + 4]))
            self.riga += 1
            i += 5

    def aggiorna_attrezzi(self):
        self.carica_attrezzi()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 731, 521))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.TabellaClienti = QtWidgets.QWidget()
        self.TabellaClienti.setObjectName("TabellaClienti")
        self.lstClienti = QtWidgets.QListWidget(self.TabellaClienti)
        self.lstClienti.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.lstClienti.setObjectName("lstClienti")
        self.btnAggiungiCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnAggiungiCliente.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnAggiungiCliente.setObjectName("btnAggiungiCliente")
        self.btnVisualizzaCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnVisualizzaCliente.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnVisualizzaCliente.setObjectName("btnVisualizzaCliente")
        self.btnAggiornaCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnAggiornaCliente.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btnAggiornaCliente.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiornaCliente.setIcon(icon)
        self.btnAggiornaCliente.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaCliente.setObjectName("btnAggiornaCliente")
        self.lblTitoloTabellaCliente = QtWidgets.QLabel(self.TabellaClienti)
        self.lblTitoloTabellaCliente.setGeometry(QtCore.QRect(30, 40, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloTabellaCliente.setFont(font)
        self.lblTitoloTabellaCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitoloTabellaCliente.setObjectName("lblTitoloTabellaCliente")
        self.lblSfondoClienti = QtWidgets.QLabel(self.TabellaClienti)
        self.lblSfondoClienti.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoClienti.setText("")
        self.lblSfondoClienti.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoClienti.setScaledContents(True)
        self.lblSfondoClienti.setObjectName("lblSfondoClienti")
        self.lblImmagineCliente = QtWidgets.QLabel(self.TabellaClienti)
        self.lblImmagineCliente.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.lblImmagineCliente.setText("")
        self.lblImmagineCliente.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.lblImmagineCliente.setScaledContents(True)
        self.lblImmagineCliente.setObjectName("lblImmagineCliente")
        self.lblSfondoClienti.raise_()
        self.lstClienti.raise_()
        self.btnAggiungiCliente.raise_()
        self.btnVisualizzaCliente.raise_()
        self.btnAggiornaCliente.raise_()
        self.lblTitoloTabellaCliente.raise_()
        self.lblImmagineCliente.raise_()
        self.tabWidget.addTab(self.TabellaClienti, "")
        self.TabellaPersonale = QtWidgets.QWidget()
        self.TabellaPersonale.setObjectName("tabPer")
        self.lstPersonale = QtWidgets.QListWidget(self.TabellaPersonale)
        self.lstPersonale.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.lstPersonale.setObjectName("lstPersonale")
        self.btnAggiungiPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnAggiungiPersonale.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnAggiungiPersonale.setObjectName("btnAggiornaPersonale")
        self.btnVisualizzaPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnVisualizzaPersonale.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnVisualizzaPersonale.setObjectName("btnVisualizzaPersonale")
        self.lblTitoloTabellaPersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblTitoloTabellaPersonale.setGeometry(QtCore.QRect(40, 40, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloTabellaPersonale.setFont(font)
        self.lblTitoloTabellaPersonale.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitoloTabellaPersonale.setObjectName("lblTitoloTabellaPersonale")
        self.btnAggiornaPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnAggiornaPersonale.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btnAggiornaPersonale.setText("")
        self.btnAggiornaPersonale.setIcon(icon)
        self.btnAggiornaPersonale.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaPersonale.setObjectName("btnAggiornaPersonale")
        self.lblSfondoPersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblSfondoPersonale.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoPersonale.setText("")
        self.lblSfondoPersonale.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoPersonale.setScaledContents(True)
        self.lblSfondoPersonale.setObjectName("lblSfondoPersonale")
        self.lblImmaginePersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblImmaginePersonale.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.lblImmaginePersonale.setText("")
        self.lblImmaginePersonale.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.lblImmaginePersonale.setScaledContents(True)
        self.lblImmaginePersonale.setObjectName("lblImmaginePersonale")
        self.lblSfondoPersonale.raise_()
        self.lstPersonale.raise_()
        self.btnAggiungiPersonale.raise_()
        self.btnVisualizzaPersonale.raise_()
        self.lblTitoloTabellaPersonale.raise_()
        self.btnAggiornaPersonale.raise_()
        self.lblImmaginePersonale.raise_()
        self.tabWidget.addTab(self.TabellaPersonale, "")
        self.TabellaAttrezzi = QtWidgets.QWidget()
        self.TabellaAttrezzi.setObjectName("TabellaAttrezzi")
        self.btnAggiungiAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnAggiungiAttrezzi.setGeometry(QtCore.QRect(390, 360, 91, 31))
        self.btnAggiungiAttrezzi.setObjectName("btnAggiungiAttrezzi")
        self.btnRimuoviAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnRimuoviAttrezzi.setGeometry(QtCore.QRect(240, 360, 91, 31))
        self.btnRimuoviAttrezzi.setObjectName("btnRimuoviAttrezzi")
        self.lblSfondoAttrezzi = QtWidgets.QLabel(self.TabellaAttrezzi)
        self.lblSfondoAttrezzi.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoAttrezzi.setText("")
        self.lblSfondoAttrezzi.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoAttrezzi.setScaledContents(True)
        self.lblSfondoAttrezzi.setObjectName("lblSfondoAttrezzi")
        self.tblAttrezzi = QtWidgets.QTableWidget(self.TabellaAttrezzi)
        self.tblAttrezzi.setGeometry(QtCore.QRect(10, 80, 691, 261))
        self.tblAttrezzi.setObjectName("tblAttrezzi")
        self.tblAttrezzi.setColumnCount(5)
        self.tblAttrezzi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(4, item)
        self.btnAggiornaAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnAggiornaAttrezzi.setGeometry(QtCore.QRect(660, 90, 31, 31))
        self.btnAggiornaAttrezzi.setText("")
        self.btnAggiornaAttrezzi.setIcon(icon)
        self.btnAggiornaAttrezzi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaAttrezzi.setObjectName("btnAggiornaAttrezzi")
        self.lblSfondoAttrezzi.raise_()
        self.btnAggiungiAttrezzi.raise_()
        self.btnRimuoviAttrezzi.raise_()
        self.tblAttrezzi.raise_()
        self.btnAggiungiAttrezzi.raise_()
        self.btnAggiornaAttrezzi.raise_()
        self.tabWidget.addTab(self.TabellaAttrezzi, "")
        self.TabellaMessaggi = QtWidgets.QWidget()
        self.TabellaMessaggi.setObjectName("TabellaMessaggi")
        self.btnEliminaMessaggio = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnEliminaMessaggio.setGeometry(QtCore.QRect(510, 220, 141, 28))
        self.btnEliminaMessaggio.setObjectName("btnEliminaMessaggio")
        self.btnScriviMessaggio = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnScriviMessaggio.setGeometry(QtCore.QRect(510, 170, 141, 28))
        self.btnScriviMessaggio.setObjectName("btnScriviMessaggio")
        self.lstMessaggi = QtWidgets.QListWidget(self.TabellaMessaggi)
        self.lstMessaggi.setGeometry(QtCore.QRect(50, 110, 441, 251))
        self.lstMessaggi.setObjectName("lstMessaggi")
        self.lblTitoloMessaggi = QtWidgets.QLabel(self.TabellaMessaggi)
        self.lblTitoloMessaggi.setGeometry(QtCore.QRect(60, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloMessaggi.setFont(font)
        self.lblTitoloMessaggi.setObjectName("label")
        self.lblSfondoMessaggi = QtWidgets.QLabel(self.TabellaMessaggi)
        self.lblSfondoMessaggi.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoMessaggi.setText("")
        self.lblSfondoMessaggi.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoMessaggi.setScaledContents(True)
        self.lblSfondoMessaggi.setObjectName("label_5")
        self.btnAggiornaMessaggi = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnAggiornaMessaggi.setGeometry(QtCore.QRect(450, 120, 31, 31))
        self.btnAggiornaMessaggi.setText("")
        self.btnAggiornaMessaggi.setIcon(icon)
        self.btnAggiornaMessaggi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMessaggi.setObjectName("btnAggiornaMessaggi")
        self.lblSfondoMessaggi.raise_()
        self.btnEliminaMessaggio.raise_()
        self.btnScriviMessaggio.raise_()
        self.lstMessaggi.raise_()
        self.lblTitoloMessaggi.raise_()
        self.btnAggiornaMessaggi.raise_()
        self.tabWidget.addTab(self.TabellaMessaggi, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.controller_messaggio.recupera_messaggi()
        self.visualizza_messaggi()
        self.carica_attrezzi()
        self.carica_clienti()
        self.carica_staff()
        self.btnRimuoviAttrezzi.clicked.connect(self.rimuovi_attrezzo)
        self.btnAggiungiCliente.clicked.connect(self.open_aggiungi_cliente)
        self.btnAggiungiPersonale.clicked.connect(self.open_aggiungi_staff)
        self.btnAggiungiAttrezzi.clicked.connect(self.open_aggiungi_attrezzo)
        self.btnAggiungiPersonale.clicked.connect(self.carica_staff)
        self.btnVisualizzaCliente.clicked.connect(self.open_visualizza_cliente)
        self.btnVisualizzaPersonale.clicked.connect(self.open_visualizza_staff)
        self.lstMessaggi.doubleClicked.connect(self.restituisci_messaggio)
        self.btnScriviMessaggio.clicked.connect(self.open_invia_messaggio)
        self.btnEliminaMessaggio.clicked.connect(self.elimina_messaggio)
        self.btnAggiornaCliente.clicked.connect(self.aggiorna_clienti)
        self.btnAggiornaPersonale.clicked.connect(self.aggiorna_staff)
        self.btnAggiornaAttrezzi.clicked.connect(self.aggiorna_attrezzi)
        self.btnAggiornaMessaggi.clicked.connect(self.visualizza_messaggi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interfaccia Admin"))
        self.btnAggiungiCliente.setText(_translate("MainWindow", "Aggiungi"))
        self.btnVisualizzaCliente.setText(_translate("MainWindow", "Visualizza"))
        self.lblTitoloTabellaCliente.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista clienti</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaClienti), _translate("MainWindow", "Clienti"))
        self.btnAggiungiPersonale.setText(_translate("MainWindow", "Aggiungi"))
        self.btnVisualizzaPersonale.setText(_translate("MainWindow", "Visualizza"))
        self.lblTitoloTabellaPersonale.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista personale</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaPersonale), _translate("MainWindow", "Personale"))
        self.btnAggiungiAttrezzi.setText(_translate("MainWindow", "Aggiungi"))
        self.btnRimuoviAttrezzi.setText(_translate("MainWindow", "Rimuovi"))
        item = self.tblAttrezzi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descrizione"))
        item = self.tblAttrezzi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data acquisto"))
        item = self.tblAttrezzi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantità"))
        item = self.tblAttrezzi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Costo unitario"))
        item = self.tblAttrezzi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data manutenzione"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaAttrezzi), _translate("MainWindow", "Attrezzi"))
        self.btnEliminaMessaggio.setText(_translate("MainWindow", "Elimina Messaggio"))
        self.btnScriviMessaggio.setText(_translate("MainWindow", "Scrivi Messaggio"))
        self.lblTitoloMessaggi.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Casella dei messaggi</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaMessaggi), _translate("MainWindow", "Bacheca"))
