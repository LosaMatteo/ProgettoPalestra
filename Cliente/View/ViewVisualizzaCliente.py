from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Cliente.Controller.ControllerCliente import ControllerCliente
from Metodi.Metodi import Metodi


class ViewVisualizzaCliente(object):
    objMetodi = Metodi()

    def __init__(self, username):
        self.username = username
        self.controller = ControllerCliente()

    def visualizza_info(self):
        data_odierna = QDate.currentDate()
        oggetto_cliente = self.controller.get_cliente_from_id(self.username)
        self.txtNome.setText(oggetto_cliente.nome)
        self.txtCognome.setText(oggetto_cliente.cognome)
        self.cmbSesso.setCurrentText(oggetto_cliente.sesso)
        self.txtDataDiNascita.setDate(oggetto_cliente.data_nascita)
        self.txtLuogoDiNascita.setText(oggetto_cliente.luogo_nascita)
        self.txtCodiceFiscale.setText(oggetto_cliente.codice_fiscale)
        self.dtdDataIscrizione.setDate(oggetto_cliente.abbonamento.data_iscrizione)
        if oggetto_cliente.abbonamento.tipo_di_abbonamento.__contains__("mensile"):
            if data_odierna > self.dtdDataIscrizione.date().addMonths(1):
                self.objMetodi.show_popup_ok("Abbonamento scaduto")
        elif oggetto_cliente.abbonamento.tipo_di_abbonamento.__contains__("annuale"):
            if data_odierna > self.dtdDataIscrizione.date().addYears(1):
                self.objMetodi.show_popup_ok("Abbonamento scaduto")
        self.dtdScadenzaCertMedico.setDate(oggetto_cliente.abbonamento.data_certificato_medico)
        self.cmbTipoAbbonamento.setCurrentText(oggetto_cliente.abbonamento.tipo_di_abbonamento)

    def salva_modifiche(self):
        if self.txtNome.text() != "" and self.txtCognome.text() != "" \
                and self.txtLuogoDiNascita.text() != "" and self.txtCodiceFiscale.text() != "":
            try:
                oggetto_cliente = self.controller.get_cliente_from_id(self.username)
                if oggetto_cliente.nome == self.txtNome.text() and oggetto_cliente.cognome == self.txtCognome.text() and \
                        oggetto_cliente.sesso == self.cmbSesso.currentText() and \
                        oggetto_cliente.data_di_nascita == self.txtDataDiNascita.date() and \
                        oggetto_cliente.luogo_di_nascita == self.txtLuogoDiNascita.text() and \
                        oggetto_cliente.codice_fiscale == self.txtCodiceFiscale.text() and \
                        oggetto_cliente.abbonamento.data_iscrizione == self.dtdDataIscrizione.date() and \
                        oggetto_cliente.abbonamento.data_certificato_medico == self.dtdScadenzaCertMedico.date() and \
                        oggetto_cliente.abbonamento.tipo_di_abbonamento == self.cmbTipoAbbonamento.currentText():
                    self.objMetodi.show_popup_exception("Nessun campo modificato.")
                else:
                    self.controller.rimuovi_cliente(self.username)
                    oggetto_cliente.nome = self.txtNome.text()
                    oggetto_cliente.cognome = self.txtCognome.text()
                    oggetto_cliente.sesso = self.cmbSesso.currentText()
                    oggetto_cliente.data_di_nascita = self.txtDataDiNascita.date()
                    oggetto_cliente.luogo_di_nascita = self.txtLuogoDiNascita.text()
                    oggetto_cliente.codice_fiscale = self.txtCodiceFiscale.text()

                    oggetto_cliente.abbonamento.data_iscrizione = self.dtdDataIscrizione.date()
                    oggetto_cliente.abbonamento.data_certificato_medico = self.dtdScadenzaCertMedico.date()
                    oggetto_cliente.abbonamento.tipo_di_abbonamento = self.cmbTipoAbbonamento.currentText()
                    self.controller.salva_modifiche_cliente(oggetto_cliente)
                    self.objMetodi.show_popup_ok("Modifiche salvate con successo!")
                self.view_visualizza_cliente.close()
            except(Exception):
                self.objMetodi.show_popup_exception("Errore.")
        else:
            self.objMetodi.show_popup_exception("Uno o più campi risultano vuoti.")

    def pulisci_caselle(self):
        self.txtNome.clear()
        self.txtCognome.clear()
        self.txtCodiceFiscale.clear()
        self.txtLuogoDiNascita.clear()
        self.txtDataDiNascita.clear()
        self.cmbSesso.clear()
        self.cmbTipoAbbonamento.clear()
        self.dtdDataIscrizione.clear()
        self.dtdScadenzaCertMedico.clear()

    def rimuovi_cliente(self):
        try:
            self.controller.elimina_cliente(self.username)
            self.pulisci_caselle()
            self.view_visualizza_cliente.close()
        except(Exception):
            self.objMetodi.show_popup_exception("Errore!")

    def reset_password(self):
        self.controller.reset_psw_cliente(self.username)
        self.objMetodi.show_popup_ok("La password è stata ripristinata")

    def setupUi(self, MainWindow):
        self.view_visualizza_cliente = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(80, 40, 121, 41))
        self.lblTitolo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblTitolo.setObjectName("lblTitolo")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(360, 40, 113, 21))
        self.txtNome.setObjectName("txtNome")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(360, 70, 113, 21))
        self.txtCognome.setObjectName("txtCognome")
        self.cmbSesso = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSesso.setEnabled(True)
        self.cmbSesso.setGeometry(QtCore.QRect(360, 100, 111, 22))
        self.cmbSesso.setEditable(True)
        self.cmbSesso.setObjectName("cmbSesso")
        self.cmbSesso.addItem("")
        self.cmbSesso.addItem("")
        self.txtDataDiNascita = QtWidgets.QDateEdit(self.centralwidget)
        self.txtDataDiNascita.setGeometry(QtCore.QRect(360, 130, 111, 22))
        self.txtDataDiNascita.setCalendarPopup(True)
        self.txtDataDiNascita.setObjectName("txtDataDiNascita")
        self.txtLuogoDiNascita = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLuogoDiNascita.setGeometry(QtCore.QRect(360, 160, 113, 21))
        self.txtLuogoDiNascita.setObjectName("txtLuogoDiNascita")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(360, 190, 113, 21))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.dtdDataIscrizione = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdDataIscrizione.setGeometry(QtCore.QRect(610, 40, 111, 22))
        self.dtdDataIscrizione.setCalendarPopup(True)
        self.dtdDataIscrizione.setObjectName("dtdDataIscrizione")
        self.dtdScadenzaCertMedico = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdScadenzaCertMedico.setGeometry(QtCore.QRect(610, 70, 111, 22))
        self.dtdScadenzaCertMedico.setCalendarPopup(True)
        self.dtdScadenzaCertMedico.setObjectName("dtdScadenzaCertMedico")
        self.cmbTipoAbbonamento = QtWidgets.QComboBox(self.centralwidget)
        self.cmbTipoAbbonamento.setGeometry(QtCore.QRect(610, 100, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        self.cmbTipoAbbonamento.setFont(font)
        self.cmbTipoAbbonamento.setEditable(True)
        self.cmbTipoAbbonamento.setObjectName("cmbTipoAbbonamento")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.cmbTipoAbbonamento.addItem("")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(30, 270, 101, 24))
        self.btnReset.setObjectName("btnReset")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(308, 40, 41, 21))
        self.lblNome.setObjectName("lblNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(298, 70, 51, 21))
        self.lblCognome.setObjectName("lblCognome")
        self.lblSesso = QtWidgets.QLabel(self.centralwidget)
        self.lblSesso.setGeometry(QtCore.QRect(300, 100, 49, 21))
        self.lblSesso.setObjectName("lblSesso")
        self.lblDataDiNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblDataDiNascita.setGeometry(QtCore.QRect(268, 130, 81, 21))
        self.lblDataDiNascita.setObjectName("lblDataDiNascita")
        self.lblLuogoDiNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblLuogoDiNascita.setGeometry(QtCore.QRect(258, 160, 91, 21))
        self.lblLuogoDiNascita.setObjectName("lblLuogoDiNascita")
        self.lblCodFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodFiscale.setGeometry(QtCore.QRect(268, 190, 81, 21))
        self.lblCodFiscale.setObjectName("lblCodFiscale")
        self.lblIscrizione = QtWidgets.QLabel(self.centralwidget)
        self.lblIscrizione.setGeometry(QtCore.QRect(508, 40, 91, 21))
        self.lblIscrizione.setObjectName("lblIscrizione")
        self.lblScadenzaCertificato = QtWidgets.QLabel(self.centralwidget)
        self.lblScadenzaCertificato.setGeometry(QtCore.QRect(498, 70, 101, 21))
        self.lblScadenzaCertificato.setObjectName("lblScadenzaCertificato")
        self.lblAbbonamento = QtWidgets.QLabel(self.centralwidget)
        self.lblAbbonamento.setGeometry(QtCore.QRect(518, 100, 81, 21))
        self.lblAbbonamento.setObjectName("lblAbbonamento")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(170, 270, 75, 24))
        self.btnSalva.setObjectName("btnSalva")
        self.btnRimuovi = QtWidgets.QPushButton(self.centralwidget)
        self.btnRimuovi.setGeometry(QtCore.QRect(280, 270, 90, 24))
        self.btnRimuovi.setObjectName("btnRimuovi")
        self.btn_Indietro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Indietro.setGeometry(QtCore.QRect(400, 270, 80, 24))
        self.btn_Indietro.setObjectName("btn_Indietro")
        self.lblNomeCliente = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCliente.setGeometry(QtCore.QRect(-35, 80, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblNomeCliente.setFont(font)
        self.lblNomeCliente.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNomeCliente.setObjectName("lblNomeCliente")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.txtNome.setReadOnly(True)
        self.txtCognome.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.visualizza_info()
        self.btnSalva.clicked.connect(self.salva_modifiche)
        self.btnReset.clicked.connect(self.reset_password)
        self.btnRimuovi.clicked.connect(self.rimuovi_cliente)
        self.btn_Indietro.clicked.connect(self.view_visualizza_cliente.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Informazioni - " + self.username))
        self.lblTitolo.setText(_translate("MainWindow", "Informazioni di"))
        self.cmbSesso.setItemText(0, _translate("MainWindow", "Maschio"))
        self.cmbSesso.setItemText(1, _translate("MainWindow", "Femmina"))
        self.cmbTipoAbbonamento.setItemText(0, _translate("MainWindow", "Abbonamento mensile sala pesi €30"))
        self.cmbTipoAbbonamento.setItemText(1, _translate("MainWindow", "Abbonamento annuale sala pesi €300"))
        self.cmbTipoAbbonamento.setItemText(2, _translate("MainWindow", "Abbonamento mensile functional €40"))
        self.cmbTipoAbbonamento.setItemText(3, _translate("MainWindow", "Abbonamento annuale functional €360"))
        self.cmbTipoAbbonamento.setItemText(4, _translate("MainWindow", "Abbonamento mensile zumba €35"))
        self.cmbTipoAbbonamento.setItemText(5, _translate("MainWindow", "Abbonamento annuale zumba €340"))
        self.cmbTipoAbbonamento.setItemText(6, _translate("MainWindow", "abbonamento mensile all inclusive €42"))
        self.cmbTipoAbbonamento.setItemText(7, _translate("MainWindow", "abbonamento annuale all inclusive €420"))
        self.btnReset.setText(_translate("MainWindow", "Reset password"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblSesso.setText(_translate("MainWindow", "Sesso"))
        self.lblDataDiNascita.setText(_translate("MainWindow", "Data di nascita"))
        self.lblLuogoDiNascita.setText(_translate("MainWindow", "Luogo di nascita"))
        self.lblCodFiscale.setText(_translate("MainWindow", "Codice fiscale"))
        self.lblIscrizione.setText(_translate("MainWindow", "Data di iscrizione"))
        self.lblScadenzaCertificato.setText(_translate("MainWindow", "Scadenza cerificato"))
        self.lblAbbonamento.setText(_translate("MainWindow", "Abbonamento"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.btnRimuovi.setText(_translate("MainWindow", "Rimuovi"))
        self.btn_Indietro.setText(_translate("MainWindow", "Indietro"))
        self.lblNomeCliente.setText(_translate("MainWindow", self.username))



