from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Metodi.Metodi import Metodi
from Allenamento.Controller.ControllerAllenamento import ControllerAllenamento


class ViewVisualizzaAllenamento(object):
    objMetodi = Metodi()

    def __init__(self, username):
        self.username = username
        self.controller = ControllerAllenamento()

    def visualizza_scheda_allenamento(self):
        oggetto_scheda = self.controller.get_allenamento_cliente(self.username)
        if oggetto_scheda != 0:
            self.lblNome.setText(self.username)
            self.lblDataInizio.setText(oggetto_scheda.data_inizio)
            self.lblDataFine.setText(oggetto_scheda.data_fine)
            row = 0
            colonna = 0
            i = 0
            while len(oggetto_scheda.nome_esercizi) >= i + 1:
                dati_esercizi = oggetto_scheda.numeri_esercizi[i].split("-")
                self.Tabella.insertRow(row)
                self.Tabella.setItem(row, colonna, QTableWidgetItem(oggetto_scheda.nome_esercizi[i]))
                self.Tabella.setItem(row, colonna + 1, QTableWidgetItem(dati_esercizi[0]))
                self.Tabella.setItem(row, colonna + 2, QTableWidgetItem(dati_esercizi[1]))
                self.Tabella.setItem(row, colonna + 3, QTableWidgetItem(dati_esercizi[2]))
                row += 1
                i += 1
        else:
            self.objMetodi.show_popup_exception("Nessuna scheda trovata.")

    def setupUi(self, MainWindow):
        self.view_visualizza_allenamento = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(250, 29, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitolo.setFont(font)
        self.lblTitolo.setObjectName("lblTitolo")
        self.Tabella = QtWidgets.QTableWidget(self.centralwidget)
        self.Tabella.setGeometry(QtCore.QRect(160, 170, 501, 301))
        self.Tabella.setObjectName("Tabella")
        self.Tabella.setColumnCount(4)
        self.Tabella.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabella.setHorizontalHeaderItem(3, item)
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(330, 70, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setText("")
        self.lblNome.setObjectName("lblNome")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(622, 500, 121, 28))
        self.btnIndietro.setObjectName("btnIndietro")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(80, 130, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_2.setGeometry(QtCore.QRect(460, 130, 151, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_2.setFont(font)
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblDataInizio = QtWidgets.QLabel(self.centralwidget)
        self.lblDataInizio.setGeometry(QtCore.QRect(220, 121, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDataInizio.setFont(font)
        self.lblDataInizio.setText("")
        self.lblDataInizio.setObjectName("lblDataInizio")
        self.lblDataFine = QtWidgets.QLabel(self.centralwidget)
        self.lblDataFine.setGeometry(QtCore.QRect(590, 120, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDataFine.setFont(font)
        self.lblDataFine.setText("")
        self.lblDataFine.setObjectName("lblDataFine")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.visualizza_scheda_allenamento()
        self.btnIndietro.clicked.connect(self.view_visualizza_allenamento.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheda di allenamento"))
        self.lblTitolo.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Scheda di allenamento</p></body></html>"))
        item = self.Tabella.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Esercizio"))
        item = self.Tabella.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Serie"))
        item = self.Tabella.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ripetizioni"))
        item = self.Tabella.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Recupero"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))
        self.lblTesto_1.setText(_translate("MainWindow", "Data inizio scheda:"))
        self.lblTesto_2.setText(_translate("MainWindow", "Data fine scheda:"))