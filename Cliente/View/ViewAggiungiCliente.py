from PyQt5 import QtCore, QtGui, QtWidgets
from Cliente.Model.Cliente import Cliente
from Cliente.Controller.ControllerCliente import ControllerCliente
from Abbonamento.View.ViewAbbonamento import ViewAbbonamento
from Metodi.Metodi import Metodi


class ViewAggiungiCliente(object):
    objMetodi = Metodi()

    def __init__(self, aggiorna_clienti):
        self.aggiorna_clienti = aggiorna_clienti
        self.controller = ControllerCliente()

    def conferma_credenziali(self):
        try:
            if self.txtNome.text() != "" and self.txtCognome.text() != "" and self.txtLuogoNascita.text() != "" \
                    and self.txtCodiceFiscale.text() != "":
                if self.controller.controlla_unicita(self.txtCodiceFiscale.text()):
                    self.view_abbonamento = QtWidgets.QMainWindow()
                    self.ui = ViewAbbonamento()
                    self.ui.setupUi(self.view_abbonamento)
                    self.view_abbonamento.show()
                    self.btnSalva.show()
                else: self.objMetodi.show_popup_exception("Utente già registrato.")
            else: self.objMetodi.show_popup_exception("Riempire tutti i campi prima di continuare.")
        except Exception: self.objMetodi.show_popup_exception("Errore.")

    def salva_cliente(self):
        try:
            nuovo_cliente = Cliente(self.txtNome.text().replace(" ", ""), self.txtCognome.text().replace(" ", ""),
                                    self.cmbSesso.currentText(), self.dtdDataDiNascita.date(),
                                    self.txtLuogoNascita.text(), self.txtCodiceFiscale.text(), "1")
            self.controller.aggiungi_cliente(nuovo_cliente)
            self.controller.recupera_clienti_salvati()
            self.aggiorna_clienti()
            self.view_aggiungi_cliente.close()
        except(Exception):
            self.objMetodi.show_popup_exception("Errore")

    def setupUi(self, MainWindow):
        self.view_aggiungi_cliente = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(100, 20, 501, 91))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(180, 130, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(270, 130, 181, 21))
        self.txtNome.setObjectName("txtNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(170, 170, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblCognome.setFont(font)
        self.lblCognome.setObjectName("lblCognome")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(270, 170, 181, 21))
        self.txtCognome.setObjectName("txtCognome")
        self.lblSesso = QtWidgets.QLabel(self.centralwidget)
        self.lblSesso.setGeometry(QtCore.QRect(178, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblSesso.setFont(font)
        self.lblSesso.setObjectName("lblSesso")
        self.lblLuogoNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblLuogoNascita.setGeometry(QtCore.QRect(70, 290, 191, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblLuogoNascita.setFont(font)
        self.lblLuogoNascita.setObjectName("lblLuogoNascita")
        self.txtLuogoNascita = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLuogoNascita.setGeometry(QtCore.QRect(270, 290, 181, 21))
        self.txtLuogoNascita.setObjectName("txtLuogoNascita")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(460, 380, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.btnSalva.setFont(font)
        self.btnSalva.setObjectName("btnSalva")
        self.cmbSesso = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSesso.setGeometry(QtCore.QRect(270, 210, 91, 22))
        self.cmbSesso.setObjectName("cmbSesso")
        self.cmbSesso.addItem("")
        self.cmbSesso.addItem("")
        self.lblDataNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblDataNascita.setGeometry(QtCore.QRect(80, 250, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblDataNascita.setFont(font)
        self.lblDataNascita.setObjectName("lblDataNascita")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(90, 330, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblCodiceFiscale.setFont(font)
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(270, 330, 181, 21))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.btnAvanti = QtWidgets.QPushButton(self.centralwidget)
        self.btnAvanti.setGeometry(QtCore.QRect(460, 410, 101, 31))
        self.btnAvanti.setIconSize(QtCore.QSize(200, 200))
        self.btnAvanti.setObjectName("btnAvanti")
        self.dtdDataDiNascita = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdDataDiNascita.setGeometry(QtCore.QRect(270, 250, 110, 22))
        self.dtdDataDiNascita.setCalendarPopup(True)
        self.dtdDataDiNascita.setObjectName("dtdDataDiNascita")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSalva.hide()
        self.btnAvanti.clicked.connect(self.conferma_credenziali)
        self.btnSalva.clicked.connect(self.salva_cliente)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuova iscrizione"))
        self.btnAvanti.setText((_translate("MainWindow", "Abbonamenti")))
        self.lblTitle.setText(_translate("MainWindow", "Aggiungi i dati del cliente"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblSesso.setText(_translate("MainWindow", "Sesso"))
        self.lblLuogoNascita.setText(_translate("MainWindow", "Luogo di nascita"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.cmbSesso.setItemText(0, _translate("MainWindow", "maschio"))
        self.cmbSesso.setItemText(1, _translate("MainWindow", "femmina"))
        self.lblDataNascita.setText(_translate("MainWindow", "Data di nascita"))
        self.lblCodiceFiscale.setText(_translate("MainWindow", "Codice Fiscale"))
