from PyQt5 import QtCore, QtGui, QtWidgets
from Metodi.Metodi import Metodi
from Staff.Controller.ControllerStaff import ControllerStaff
from Orario.View.ViewGestioneOrario import ViewGestioneOrario


class ViewVisualizzaStaff(object):
    objMetodi = Metodi()

    def __init__(self, username, aggiorna_staff):
        self.username = username
        self.aggiorna_staff = aggiorna_staff
        self.controller = ControllerStaff()

    def visualizza_info(self):
        oggetto_personale = self.controller.get_dipendente(self.username)
        self.txtNome.setText(oggetto_personale.nome)
        self.txtCognome.setText(oggetto_personale.cognome)
        self.txtCodiceFiscale.setText(oggetto_personale.codice_fiscale)
        self.txtMansione.setText(oggetto_personale.mansione)

    def salva_modifiche(self):
        if self.txtNome.text() != "" and self.txtCognome.text() != "" and self.txtCodiceFiscale.text() != "" \
                and self.txtMansione.text() != "":
            try:
                oggetto_personale = self.controller.get_dipendente(self.username)
                if oggetto_personale.nome == self.txtNome.text() and oggetto_personale.cognome == self.txtCognome.text() and \
                        oggetto_personale.codice_fiscale == self.txtCodiceFiscale.text() and oggetto_personale.mansione == self.txtMansione.text():
                    self.objMetodi.show_popup_exception("Nessun campo modificato.")
                else:
                    self.controller.rimuovi_dipendente(self.username)
                    oggetto_personale.nome = self.txtNome.text()
                    oggetto_personale.cognome = self.txtCognome.text()
                    oggetto_personale.codice_fiscale = self.txtCodiceFiscale.text()
                    oggetto_personale.mansione = self.txtMansione.text()
                    self.controller.aggiungi_dipendente(oggetto_personale)
                    self.aggiorna_staff()
                    self.objMetodi.show_popup_ok("Modifiche salvate con successo!")
                self.view_visualizza_staff.close()
            except(Exception):
                self.objMetodi.show_popup_exception("Non hai selezionato nulla nella lista!")
        else:
            self.objMetodi.show_popup_exception("Uno o più campi risultano vuoti.")

    def pulisci_caselle(self):
        self.txtNome.clear()
        self.txtCognome.clear()
        self.txtCodiceFiscale.clear()
        self.txtMansione.clear()

    def rimuovi_staff(self):
        try:
            if self.objMetodi.show_popup_question("Sei sicuro di voler eliminare il membro dello staff? "
                                                  "Verranno rimossi anche i suoi turni di lavoro."):
                self.controller.rimuovi_dipendente(self.username)
                self.pulisci_caselle()
                self.aggiorna_staff()
                self.view_visualizza_staff.close()
            else:
                self.view_visualizza_staff.close()
        except(Exception):
            self.objMetodi.show_popup_exception("Errore!")
        self.view_visualizza_staff.close()

    def reset_password(self):
        self.controller.reset_psw_dipendente(self.username)
        self.objMetodi.show_popup_ok("Password resettata con successo!")
        self.view_visualizza_staff.close()

    def open_gestione_orario(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ViewGestioneOrario(self.username.replace(" ", ""))
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        self.view_visualizza_staff = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(80, 40, 121, 41))
        self.lblTitolo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblTitolo.setObjectName("lblTitolo")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(340, 40, 113, 21))
        self.txtNome.setObjectName("txtNome")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(340, 70, 113, 21))
        self.txtCognome.setObjectName("txtCognome")
        self.txtMansione = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMansione.setGeometry(QtCore.QRect(340, 130, 113, 21))
        self.txtMansione.setObjectName("txtMansione")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(340, 100, 113, 21))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(100, 190, 101, 24))
        self.btnReset.setObjectName("btnReset")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(250, 40, 41, 21))
        self.lblNome.setObjectName("lblNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(250, 70, 51, 21))
        self.lblCognome.setObjectName("lblCognome")
        self.lblMansione = QtWidgets.QLabel(self.centralwidget)
        self.lblMansione.setGeometry(QtCore.QRect(250, 130, 51, 21))
        self.lblMansione.setObjectName("lblMansione")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(250, 100, 81, 21))
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(20, 190, 61, 24))
        self.btnSalva.setObjectName("btnSalva")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(390, 190, 71, 24))
        self.btnIndietro.setObjectName("btnIndietro")
        self.lblNomeStaff = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeStaff.setGeometry(QtCore.QRect(60, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblNomeStaff.setFont(font)
        self.lblNomeStaff.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNomeStaff.setObjectName("lblNomeStaff")
        self.btnOrario = QtWidgets.QPushButton(self.centralwidget)
        self.btnOrario.setGeometry(QtCore.QRect(300, 190, 75, 24))
        self.btnOrario.setObjectName("btnOrario")
        self.btnRimuovi = QtWidgets.QPushButton(self.centralwidget)
        self.btnRimuovi.setGeometry(QtCore.QRect(210, 190, 75, 24))
        self.btnRimuovi.setObjectName("btnRimuovi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.txtNome.setReadOnly(True)
        self.txtCognome.setReadOnly(True)
        self.txtCodiceFiscale.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSalva.clicked.connect(self.salva_modifiche)
        self.btnRimuovi.clicked.connect(self.rimuovi_staff)
        self.visualizza_info()
        self.btnOrario.clicked.connect(self.open_gestione_orario)
        self.btnIndietro.clicked.connect(self.view_visualizza_staff.close)
        self.btnReset.clicked.connect(self.reset_password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Informazioni - " + self.username))
        self.lblTitolo.setText(_translate("MainWindow", "Informazioni di "))
        self.btnReset.setText(_translate("MainWindow", "Reset password"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblMansione.setText(_translate("MainWindow", "Mansione"))
        self.lblCodiceFiscale.setText(_translate("MainWindow", "Codice fiscale"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))
        self.lblNomeStaff.setText(_translate("MainWindow", self.username))
        self.btnOrario.setText(_translate("MainWindow", "Orario"))
        self.btnRimuovi.setText(_translate("MainWindow", "Rimuovi"))