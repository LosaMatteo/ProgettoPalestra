from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi.Metodi import Metodi
from Prenotazione.Model.Prenotazione import Prenotazione
from Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione


class ViewPrenotazioneFunzionale(object):
    giorni_attivi = {"mar", "mer", "ven"}
    numero_massimo = 15
    sala = "Allenamento Functional"
    objMetodi = Metodi()

    def __init__(self, username, aggiorna_prenotazioni):
        self.username = username
        self.aggiorna_prenotazioni = aggiorna_prenotazioni
        self.controller = ControllerPrenotazione()

    def prenota_orario(self):
        if self.controller.controlla_apertura(self.popupcalendar.selectedDate(), self.giorni_attivi):
            nuova_prenotazione = Prenotazione(self.username, self.sala, self.popupcalendar.selectedDate(),
                                              self.cmbOrario.currentText())
            if self.controller.effettua_prenotazione(self.numero_massimo, nuova_prenotazione):
                self.aggiorna_prenotazioni()
                self.objMetodi.show_popup_ok("Prenotazione effetuata.")
            else:
                self.objMetodi.show_popup_exception("Prenotazione già effettuata o limite massimo raggiunto.")
            self.prenotazione_funzionale.close()
        else:
            self.objMetodi.show_popup_exception("Selezionare un giorno corretto.")

    def combobox_attive(self):
        if self.controller.controlla_apertura(self.popupcalendar.selectedDate(), self.giorni_attivi):
            self.progressBar.setValue(
                self.controller.get_posti_disponibili(self.sala, self.popupcalendar.selectedDate(),
                                                      self.cmbOrario.currentText()))

    def elimina_vecchie_prenotazioni(self):
        self.controller.pulisci_prenotazioni()

    def setupUi(self, Form):
        self.prenotazione_funzionale = Form
        Form.setObjectName("Form")
        Form.resize(756, 411)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(560, 230, 121, 23))
        self.progressBar.setMaximum(15)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(560, 340, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(0, 100, 111, 16))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(550, 80, 111, 20))
        self.lblTesto_1.setObjectName("lblTesto_2")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(560, 200, 81, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(19, 15, 311, 61))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblImmagineFunctional = QtWidgets.QLabel(Form)
        self.lblImmagineFunctional.setGeometry(QtCore.QRect(370, 10, 91, 71))
        self.lblImmagineFunctional.setText("")
        self.lblImmagineFunctional.setPixmap(QtGui.QPixmap(".\\IconaAllFunzionale.png"))
        self.lblImmagineFunctional.setScaledContents(True)
        self.lblImmagineFunctional.setObjectName("lblImmagineFunctional")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 120, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("popupcalendar")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.cmbOrario.setObjectName("cmbOrari")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnPrenota.clicked.connect(self.prenota_orario)
        self.popupcalendar.setMinimumDate(QDate.currentDate())
        self.cmbOrario.activated[str].connect(self.combobox_attive)
        self.popupcalendar.clicked.connect(self.combobox_attive)
        self.popupcalendar.setMaximumDate(QDate.currentDate().addMonths(1))
        self.elimina_vecchie_prenotazioni()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prenotazioni functional"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.lblInfo.setText(_translate("Form", "Seleziona data:"))
        self.lblTesto_1.setText(_translate("Form", "Seleziona orario:"))
        self.lblTesto_2.setText(_translate("Form", "Posti liberi:"))
        self.lblTesto_3.setText(_translate("Form",
                                        "<html><head/><body><p>Le lezioni di Allenamento Funzionale si svolgono<br/>martedì, mercoledì e venerdì.<br/>Dalle ore 15:30 e dalle 17:00. <br/></p></body></html>"))
        self.cmbOrario.setItemText(0, _translate("Form", "15:30-17:00"))
        self.cmbOrario.setItemText(1, _translate("Form", "17:00-18:30"))

