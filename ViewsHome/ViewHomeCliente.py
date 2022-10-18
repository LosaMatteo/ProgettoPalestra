import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi.Metodi import Metodi
from Messaggio.Controller.ControllerMessaggio import ControllerMessaggio
from Messaggio.View.ViewLeggiMessaggio import ViewLeggiMessaggio
from Messaggio.View.ViewInviaMessaggio import ViewInviaMessaggio
from Dieta.View.ViewInfoDieta import ViewInfoDieta
from PreferenzaEsercizi.View.ViewPreferenzaEsercizi import ViewPreferenzaEsercizi
from Prenotazione.View.ViewPrenotazioni import ViewPrenotazioni
from ModificaPassword.ViewModificaPassword import ViewModificaPassword
from Allenamento.View.ViewVisualizzaAllenamento import ViewVisualizzaAllenamento


class ViewHomeCliente(object):
    percorso = "./Dieta/Data/FilesDieteCliente/"
    objMetodi = Metodi()
    controller_messaggio = ControllerMessaggio()
    lista_files = []

    def __init__(self, username, cliente, lista_prenotazioni, annulla_prenotazione, scheda_esercizi):
        self.username = username
        self.cliente = cliente
        self.lista_prenotazioni = lista_prenotazioni
        self.annulla_prenotazione = annulla_prenotazione
        self.esercizi = scheda_esercizi

    def aggiungi_prenotazione(self):
        self.lstPrenotazioni.clear()
        for elem in self.lista_prenotazioni():
            self.lstPrenotazioni.addItem("data: " + elem.data.toString("dd/MM/yyyy") + " orario: " +
                                         elem.orario + " " + elem.sala)

    def open_info_dieta(self):
        self.info_dieta = QtWidgets.QMainWindow()
        self.ui = ViewInfoDieta(self.username)
        self.ui.setupUi(self.info_dieta)
        self.info_dieta.show()

    def open_preferenza_esercizi(self):
        self.preferenza_esercizi = QtWidgets.QMainWindow()
        self.ui = ViewPreferenzaEsercizi(self.username)
        self.ui.setupUi(self.preferenza_esercizi)
        self.preferenza_esercizi.show()

    def open_effettua_prenotazione(self):
        self.effettua_prenotazione = QtWidgets.QMainWindow()
        self.ui = ViewPrenotazioni(self.username, self.aggiungi_prenotazione)
        self.ui.setupUi(self.effettua_prenotazione)
        self.effettua_prenotazione.show()

    def open_modifica_password(self):
        self.modifica_password = QtWidgets.QMainWindow()
        self.ui = ViewModificaPassword(self.username)
        self.ui.setupUi(self.modifica_password)
        self.modifica_password.show()

    def carica_diete(self):
        for elem in self.objMetodi.get_lista_files(self.percorso):
            if elem.startswith(self.username):
                self.lstDieta.addItem("Dieta " + self.username)

    def apri_file_dieta(self):
        lista_files = self.objMetodi.get_lista_files(self.percorso)
        for elem in lista_files:
            if elem.startswith(self.username):
                nome_file = elem.split(".")
                os.chdir(self.percorso)
                os.system(self.username + "." + nome_file[1])
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
                return

    def visualizza_info_cliente(self):
        self.mostra()
        data_odierna = QDate.currentDate()
        self.txtNome.setText(self.cliente.nome)
        self.txtCognome.setText(self.cliente.cognome)
        self.txtUsername.setText(self.username)
        self.txtPassword.setText(self.cliente.password)
        self.txtCodiceFiscale.setText(self.cliente.codice_fiscale)
        self.txtLuogoNascita.setText(self.cliente.luogo_nascita)
        self.txtDataNascita.setText(self.cliente.data_nascita.toString())
        self.dtdDataIscrizione.setDate(self.cliente.abbonamento.data_iscrizione)
        if self.cliente.abbonamento.tipo_di_abbonamento.__contains__("mensile"):
            self.dtdScadenzaAbbonamento.setDate(self.dtdDataIscrizione.date().addMonths(1))
            if data_odierna > self.dtdScadenzaAbbonamento.date():
                self.objMetodi.show_popup_exception("Abbonamento scaduto.")
        elif self.cliente.abbonamento.tipo_di_abbonamento.__contains__("annuale"):
            self.dtdScadenzaAbbonamento.setDate(self.dtdDataIscrizione.date().addYears(1))
            if data_odierna > self.dtdScadenzaAbbonamento.date():
                self.objMetodi.show_popup_exception("Abbonamento scaduto-")
        self.dtdScadenzaCertificatoMedico.setDate(self.cliente.abbonamento.data_certificato_medico)

    def open_visualizza_allenamento(self):
        self.visualizza_allenamento = QtWidgets.QMainWindow()
        self.ui = ViewVisualizzaAllenamento(self.username)
        self.ui.setupUi(self.visualizza_allenamento)
        self.visualizza_allenamento.show()

    def nascondi(self):
        self.lstInformazioniPersonali.hide()
        self.txtNome.hide()
        self.txtCognome.hide()
        self.txtUsername.hide()
        self.txtPassword.hide()
        self.txtCodiceFiscale.hide()
        self.txtLuogoNascita.hide()
        self.txtDataNascita.hide()
        self.dtdDataIscrizione.hide()
        self.dtdScadenzaAbbonamento.hide()
        self.dtdScadenzaCertificatoMedico.hide()
        self.lblNome.hide()
        self.lblCognome.hide()
        self.lblUsername.hide()
        self.lblPassword.hide()
        self.lblCodiceFiscale.hide()
        self.lblLuogoNascita.hide()
        self.lblDataNascita.hide()
        self.lblDataIscrizione.hide()
        self.lblDataFineAbbonamento.hide()
        self.lblDataCertificatoMedico.hide()
        self.btnMostraPassword.hide()

    def mostra(self):
        self.lstInformazioniPersonali.show()
        self.txtNome.show()
        self.txtCognome.show()
        self.txtUsername.show()
        self.txtPassword.show()
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtCodiceFiscale.show()
        self.txtLuogoNascita.show()
        self.txtDataNascita.show()
        self.dtdDataIscrizione.show()
        self.dtdScadenzaAbbonamento.show()
        self.dtdScadenzaCertificatoMedico.show()
        self.lblNome.show()
        self.lblCognome.show()
        self.lblUsername.show()
        self.lblPassword.show()
        self.lblCodiceFiscale.show()
        self.lblLuogoNascita.show()
        self.lblDataNascita.show()
        self.lblDataIscrizione.show()
        self.lblDataFineAbbonamento.show()
        self.lblDataCertificatoMedico.show()
        self.btnMostraPassword.show()

    def mostra_password(self):
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Normal)

    def nascondi_password(self):
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def visualizza_scheda_allenamento(self):
        allenamento = self.esercizi(self.username)
        if allenamento != 0:
            self.lstSchedaAllenamento.addItem("Scheda dal " + allenamento.data_inizio)

    def elimina_prenotazione(self):
        try:
            if self.lstPrenotazioni.currentItem().isSelected():
                self.annulla_prenotazione(self.lista_prenotazioni()[self.lstPrenotazioni.currentIndex().row()])
                self.lstPrenotazioni.clear()
                self.aggiungi_prenotazione()
        except AttributeError:
            self.objMetodi.show_popup_exception("Selezionare una voce dalla lista.")
        except Exception:
            self.objMetodi.show_popup_exception("Errore.")

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
        self.controller_messaggio.get_lista_messaggi_from_id(self.username)
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

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 647)
        self.lblMsgDiBenvenuto = QtWidgets.QLabel(Form)
        self.lblMsgDiBenvenuto.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        self.lblMsgDiBenvenuto.setFont(font)
        self.lblMsgDiBenvenuto.setObjectName("lblMsgDiBenvenuto")
        self.lblNomeUtente = QtWidgets.QLabel(Form)
        self.lblNomeUtente.setGeometry(QtCore.QRect(170, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        self.lblNomeUtente.setFont(font)
        self.lblNomeUtente.setObjectName("lblNomeUtente")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 50, 471, 551))
        self.toolBox.setObjectName("toolBox")
        self.Pagina_1 = QtWidgets.QWidget()
        self.Pagina_1.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_1.setObjectName("Pagina_1")
        self.lblSfondo = QtWidgets.QLabel(self.Pagina_1)
        self.lblSfondo.setGeometry(QtCore.QRect(-1, 0, 461, 391))
        self.lblSfondo.setText("")
        self.lblSfondo.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondo.setScaledContents(True)
        self.lblSfondo.setObjectName("lblSfondo")
        self.btnCambioPassword = QtWidgets.QPushButton(self.Pagina_1)
        self.btnCambioPassword.setGeometry(QtCore.QRect(330, 290, 121, 24))
        self.btnCambioPassword.setObjectName("btnCambioPassword")
        self.btnLeTueInfo = QtWidgets.QPushButton(self.Pagina_1)
        self.btnLeTueInfo.setGeometry(QtCore.QRect(330, 270, 121, 21))
        self.btnLeTueInfo.setObjectName("btnLeTueInfo")
        self.lstInformazioniPersonali = QtWidgets.QListWidget(self.Pagina_1)
        self.lstInformazioniPersonali.setGeometry(QtCore.QRect(20, 20, 281, 361))
        self.lstInformazioniPersonali.setObjectName("lstInformazioniPersonali")
        self.txtPassword = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtPassword.setGeometry(QtCore.QRect(170, 140, 113, 22))
        self.txtPassword.setText("")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setReadOnly(True)
        self.txtPassword.setObjectName("txtPassword")
        self.dtdDataIscrizione = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdDataIscrizione.setGeometry(QtCore.QRect(170, 260, 111, 22))
        self.dtdDataIscrizione.setReadOnly(True)
        self.dtdDataIscrizione.setCalendarPopup(True)
        self.dtdDataIscrizione.setObjectName("dtdDataIscrizione")
        self.txtLuogoNascita = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtLuogoNascita.setGeometry(QtCore.QRect(170, 200, 113, 22))
        self.txtLuogoNascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtLuogoNascita.setReadOnly(True)
        self.txtLuogoNascita.setObjectName("txtLuogoNascita")
        self.lblDataIscrizione = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataIscrizione.setGeometry(QtCore.QRect(40, 260, 111, 21))
        self.lblDataIscrizione.setObjectName("lblDataIscrizione")
        self.dtdScadenzaCertificatoMedico = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdScadenzaCertificatoMedico.setGeometry(QtCore.QRect(170, 320, 111, 22))
        self.dtdScadenzaCertificatoMedico.setReadOnly(True)
        self.dtdScadenzaCertificatoMedico.setCalendarPopup(True)
        self.dtdScadenzaCertificatoMedico.setObjectName("dtdScadenzaCertificatoMedico")
        self.lblLuogoNascita = QtWidgets.QLabel(self.Pagina_1)
        self.lblLuogoNascita.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.lblLuogoNascita.setObjectName("lblLuogoNascita")
        self.lblNome = QtWidgets.QLabel(self.Pagina_1)
        self.lblNome.setGeometry(QtCore.QRect(40, 50, 111, 21))
        self.lblNome.setObjectName("lblNome")
        self.txtNome = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtNome.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.txtNome.setReadOnly(True)
        self.txtNome.setObjectName("txtNome")
        self.lblDataFineAbbonamento = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataFineAbbonamento.setGeometry(QtCore.QRect(30, 290, 141, 21))
        self.lblDataFineAbbonamento.setObjectName("lblDataFineAbbonamento")
        self.lblDataCertificatoMedico = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataCertificatoMedico.setGeometry(QtCore.QRect(30, 320, 131, 21))
        self.lblDataCertificatoMedico.setObjectName("lblDataCertificatoMedico")
        self.txtDataNascita = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtDataNascita.setGeometry(QtCore.QRect(170, 230, 113, 22))
        self.txtDataNascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtDataNascita.setReadOnly(True)
        self.txtDataNascita.setObjectName("txtDataNascita")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.Pagina_1)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.lblDataNascita = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataNascita.setGeometry(QtCore.QRect(40, 230, 111, 21))
        self.lblDataNascita.setObjectName("lblDataNascita")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.txtCodiceFiscale.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtCodiceFiscale.setReadOnly(True)
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.lblUsername = QtWidgets.QLabel(self.Pagina_1)
        self.lblUsername.setGeometry(QtCore.QRect(40, 110, 111, 21))
        self.lblUsername.setObjectName("lblUsername")
        self.txtUsername = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtUsername.setGeometry(QtCore.QRect(170, 110, 113, 22))
        self.txtUsername.setReadOnly(True)
        self.txtUsername.setObjectName("txtUsername")
        self.txtCognome = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtCognome.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.txtCognome.setReadOnly(True)
        self.txtCognome.setObjectName("txtCognome")
        self.lblPassword = QtWidgets.QLabel(self.Pagina_1)
        self.lblPassword.setGeometry(QtCore.QRect(40, 140, 111, 21))
        self.lblPassword.setObjectName("lblPassword")
        self.lblCognome = QtWidgets.QLabel(self.Pagina_1)
        self.lblCognome.setGeometry(QtCore.QRect(40, 80, 111, 21))
        self.lblCognome.setObjectName("lblCognome")
        self.dtdScadenzaAbbonamento = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdScadenzaAbbonamento.setGeometry(QtCore.QRect(170, 290, 111, 22))
        self.dtdScadenzaAbbonamento.setReadOnly(True)
        self.dtdScadenzaAbbonamento.setCalendarPopup(True)
        self.dtdScadenzaAbbonamento.setObjectName("dtdScadenzaAbbonamento")
        self.btnMostraPassword = QtWidgets.QPushButton(self.Pagina_1)
        self.btnMostraPassword.setGeometry(QtCore.QRect(260, 141, 21, 20))
        self.btnMostraPassword.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMostraPassword.setIcon(icon)
        self.btnMostraPassword.setObjectName("btnMostraPassword")
        self.toolBox.addItem(self.Pagina_1, "")
        self.Pagina_2 = QtWidgets.QWidget()
        self.Pagina_2.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_2.setObjectName("Pagina_2")
        self.lblTitolo = QtWidgets.QLabel(self.Pagina_2)
        self.lblTitolo.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.lblTitolo.setObjectName("lblTitolo")
        self.lblTesto_2 = QtWidgets.QLabel(self.Pagina_2)
        self.lblTesto_2.setGeometry(QtCore.QRect(10, 290, 240, 31))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.btnEserciziCorsi = QtWidgets.QPushButton(self.Pagina_2)
        self.btnEserciziCorsi.setGeometry(QtCore.QRect(260, 290, 113, 31))
        self.btnEserciziCorsi.setObjectName("btnEserciziCorsi")
        self.lblSfondo_2 = QtWidgets.QLabel(self.Pagina_2)
        self.lblSfondo_2.setGeometry(QtCore.QRect(-1, 0, 451, 351))
        self.lblSfondo_2.setText("")
        self.lblSfondo_2.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondo_2.setScaledContents(True)
        self.lblSfondo_2.setObjectName("lblSfondo_2")
        self.lstSchedaAllenamento = QtWidgets.QListWidget(self.Pagina_2)
        self.lstSchedaAllenamento.setGeometry(QtCore.QRect(30, 50, 411, 192))
        self.lstSchedaAllenamento.setObjectName("lstSchedaAllenamento")
        self.lblSfondo_2.raise_()
        self.lblTitolo.raise_()
        self.lblTesto_2.raise_()
        self.btnEserciziCorsi.raise_()
        self.lstSchedaAllenamento.raise_()
        self.toolBox.addItem(self.Pagina_2, "")
        self.Pagina_3 = QtWidgets.QWidget()
        self.Pagina_3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Pagina_3.setObjectName("Pagina_3")
        self.lblTitolo_2 = QtWidgets.QLabel(self.Pagina_3)
        self.lblTitolo_2.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.lblTitolo_2.setObjectName("lblTitolo_2")
        self.btnFabbisogno = QtWidgets.QPushButton(self.Pagina_3)
        self.btnFabbisogno.setGeometry(QtCore.QRect(300, 290, 113, 32))
        self.btnFabbisogno.setObjectName("btnFabbisogno")
        self.lblTesto_3 = QtWidgets.QLabel(self.Pagina_3)
        self.lblTesto_3.setGeometry(QtCore.QRect(50, 290, 250, 31))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblSfondo_3 = QtWidgets.QLabel(self.Pagina_3)
        self.lblSfondo_3.setGeometry(QtCore.QRect(-1, 0, 471, 401))
        self.lblSfondo_3.setText("")
        self.lblSfondo_3.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondoverde.png"))
        self.lblSfondo_3.setScaledContents(True)
        self.lblSfondo_3.setObjectName("lblSfondo_3")
        self.lstDieta = QtWidgets.QListWidget(self.Pagina_3)
        self.lstDieta.setGeometry(QtCore.QRect(20, 30, 271, 211))
        self.lstDieta.setObjectName("lstDieta")
        self.lblSfondo_3.raise_()
        self.lblTitolo_2.raise_()
        self.btnFabbisogno.raise_()
        self.lblTesto_3.raise_()
        self.lstDieta.raise_()
        self.toolBox.addItem(self.Pagina_3, "")
        self.Pagina_4 = QtWidgets.QWidget()
        self.Pagina_4.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_4.setObjectName("Pagina_4")
        self.lblTitolo_3 = QtWidgets.QLabel(self.Pagina_4)
        self.lblTitolo_3.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.lblTitolo_3.setObjectName("lblTitolo_3")
        self.lblTesto_4 = QtWidgets.QLabel(self.Pagina_4)
        self.lblTesto_4.setGeometry(QtCore.QRect(20, 270, 91, 31))
        self.lblTesto_4.setObjectName("lblTesto_4")
        self.btnPrenotazioni = QtWidgets.QPushButton(self.Pagina_4)
        self.btnPrenotazioni.setGeometry(QtCore.QRect(160, 270, 113, 32))
        self.btnPrenotazioni.setObjectName("btnPrenotazioni")
        self.lblSfondo_4 = QtWidgets.QLabel(self.Pagina_4)
        self.lblSfondo_4.setGeometry(QtCore.QRect(0, 0, 471, 391))
        self.lblSfondo_4.setText("")
        self.lblSfondo_4.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfoidnigiallo.png"))
        self.lblSfondo_4.setScaledContents(True)
        self.lblSfondo_4.setObjectName("lblSfondo_4")
        self.lstPrenotazioni = QtWidgets.QListWidget(self.Pagina_4)
        self.lstPrenotazioni.setGeometry(QtCore.QRect(20, 30, 381, 211))
        self.lstPrenotazioni.setAutoScroll(True)
        self.lstPrenotazioni.setObjectName("lstPrenotazioni")
        self.btnCancella = QtWidgets.QPushButton(self.Pagina_4)
        self.btnCancella.setGeometry(QtCore.QRect(350, 40, 31, 21))
        self.btnCancella.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Resources/images/cancella.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancella.setIcon(icon1)
        self.btnCancella.setIconSize(QtCore.QSize(30, 200))
        self.btnCancella.setObjectName("btnCancella")
        self.btnAggiorna = QtWidgets.QPushButton(self.Pagina_4)
        self.btnAggiorna.setGeometry(QtCore.QRect(410, 30, 31, 31))
        self.btnAggiorna.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiorna.setIcon(icon2)
        self.btnAggiorna.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiorna.setObjectName("btnAggiorna")
        self.lblSfondo_4.raise_()
        self.lblTitolo_3.raise_()
        self.lblTesto_4.raise_()
        self.btnPrenotazioni.raise_()
        self.lstPrenotazioni.raise_()
        self.btnAggiorna.raise_()
        self.btnCancella.raise_()
        self.toolBox.addItem(self.Pagina_4, "")
        self.Pagina_5 = QtWidgets.QWidget()
        self.Pagina_5.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_5.setObjectName("page_5")
        self.lblTitolo_4 = QtWidgets.QLabel(self.Pagina_5)
        self.lblTitolo_4.setGeometry(QtCore.QRect(50, 10, 191, 61))
        self.lblTitolo_4.setObjectName("lblTitolo_4")
        self.lblSfondo_5 = QtWidgets.QLabel(self.Pagina_5)
        self.lblSfondo_5.setGeometry(QtCore.QRect(-1, 10, 471, 401))
        self.lblSfondo_5.setText("")
        self.lblSfondo_5.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.lblSfondo_5.setObjectName("lblSfondo_5")
        self.lstMessaggi = QtWidgets.QListWidget(self.Pagina_5)
        self.lstMessaggi.setGeometry(QtCore.QRect(20, 70, 300, 321))
        self.lstMessaggi.setObjectName("lstMessaggi")
        self.btnNuovoMessaggio = QtWidgets.QPushButton(self.Pagina_5)
        self.btnNuovoMessaggio.setGeometry(QtCore.QRect(325, 160, 141, 28))
        self.btnNuovoMessaggio.setObjectName("btnNuovoMessaggio")
        self.btnEliminaMessaggio = QtWidgets.QPushButton(self.Pagina_5)
        self.btnEliminaMessaggio.setGeometry(QtCore.QRect(325, 200, 141, 28))
        self.btnEliminaMessaggio.setObjectName("btnEliminaMessaggio")
        self.btnAggiornaMessaggi = QtWidgets.QPushButton(self.Pagina_5)
        self.btnAggiornaMessaggi.setGeometry(QtCore.QRect(330, 70, 31, 31))
        self.btnAggiornaMessaggi.setText("")
        self.btnAggiornaMessaggi.setIcon(icon2)
        self.btnAggiornaMessaggi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMessaggi.setObjectName("btnAggiornaMessaggi")
        self.lblSfondo_5.raise_()
        self.lblTitolo_4.raise_()
        self.lstMessaggi.raise_()
        self.btnNuovoMessaggio.raise_()
        self.btnEliminaMessaggio.raise_()
        self.btnAggiornaMessaggi.raise_()
        self.toolBox.addItem(self.Pagina_5, "")
        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.controller_messaggio.recupera_messaggi()
        self.nascondi()
        self.visualizza_messaggi()
        self.lblNomeUtente.setText(self.username)
        self.btnLeTueInfo.clicked.connect(self.visualizza_info_cliente)
        self.btnCambioPassword.clicked.connect(self.open_modifica_password)
        self.btnEserciziCorsi.clicked.connect(self.open_preferenza_esercizi)
        self.btnFabbisogno.clicked.connect(self.open_info_dieta)
        self.btnPrenotazioni.clicked.connect(self.open_effettua_prenotazione)
        self.lstSchedaAllenamento.clicked.connect(self.open_visualizza_allenamento)
        self.lstMessaggi.doubleClicked.connect(self.restituisci_messaggio)
        self.btnNuovoMessaggio.clicked.connect(self.open_invia_messaggio)
        self.aggiungi_prenotazione()
        self.carica_diete()
        self.lstDieta.doubleClicked.connect(self.apri_file_dieta)
        self.btnMostraPassword.pressed.connect(self.mostra_password)
        self.btnMostraPassword.clicked.connect(self.nascondi_password)
        self.btnEliminaMessaggio.clicked.connect(self.elimina_messaggio)
        self.visualizza_scheda_allenamento()
        self.btnCancella.clicked.connect(self.elimina_prenotazione)
        self.btnAggiorna.clicked.connect(self.aggiungi_prenotazione)
        self.btnAggiornaMessaggi.clicked.connect(self.visualizza_messaggi)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bentornato, " + self.username))
        self.lblMsgDiBenvenuto.setText(_translate("Form",
                                                  "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Bentornato </span></p></body></html>"))
        self.lblNomeUtente.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.btnCambioPassword.setText(_translate("Form", "Cambia password"))
        self.btnLeTueInfo.setText(_translate("Form", "Le tue info"))
        self.lblDataIscrizione.setText(_translate("Form", "Data iscrizione"))
        self.lblLuogoNascita.setText(_translate("Form", "Luogo di nascita:"))
        self.lblNome.setText(_translate("Form", "Nome:"))
        self.lblDataFineAbbonamento.setText(_translate("Form", "Data fine abbonamento"))
        self.lblDataCertificatoMedico.setText(_translate("Form", "Data certificato medico"))
        self.lblCodiceFiscale.setText(_translate("Form", "Codice Fiscale:"))
        self.lblDataNascita.setText(_translate("Form", "Data di nascita:"))
        self.lblUsername.setText(_translate("Form", "Username:"))
        self.lblPassword.setText(_translate("Form", "Password:"))
        self.lblCognome.setText(_translate("Form", "Cognome:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_1), _translate("Form", "Informazioni personali"))
        self.lblTitolo.setText(_translate("Form", "<html><head/><body><p>La tua scheda allenamento:</p></body></html>"))
        self.lblTesto_2.setText(_translate("Form",
                                           "<html><head/><body><p><span style=\" color:#000000;\">Scopri gli esercizi e seleziona preferenze</span></p></body></html>"))
        self.btnEserciziCorsi.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_2), _translate("Form", "Allenamento"))
        self.lblTitolo_2.setText(_translate("Form", "<html><head/><body><p>La tua dieta: </p></body></html>"))
        self.btnFabbisogno.setText(_translate("Form", "Clicca qui!"))
        self.lblTesto_3.setText(
            _translate("Form", "<html><head/><body><p>Dacci informazioni sulla tua alimentazione<br> e scopri di"
                               " più sulla tua forma fisica</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_3), _translate("Form", "Dieta"))
        self.lblTitolo_3.setText(_translate("Form", "<html><head/><body><p>Le tue Prenotazioni:</p></body></html>"))
        self.lblTesto_4.setText(_translate("Form", "<html><head/><body><p>Per prenotare</p></body></html>"))
        self.btnPrenotazioni.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_4), _translate("Form", "Prenotazioni"))
        self.lblTitolo_4.setText(_translate("Form",
                                            "<html><head/><body><p align=\"center\">Qui riceverai le notifiche </p><p align=\"center\">riguardanti il tuo abbonamento!</p></body></html>"))
        self.btnNuovoMessaggio.setText(_translate("Form", "Scrivi Messaggio"))
        self.btnEliminaMessaggio.setText(_translate("Form", "Elimina Messaggio"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_5), _translate("Form", "Messaggi"))