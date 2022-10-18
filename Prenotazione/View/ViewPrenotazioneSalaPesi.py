from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Metodi.Metodi import Metodi
from Prenotazione.Model.Prenotazione import Prenotazione
from Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione


class ViewPrenotazioneSalaPesi(object):
    giorni_attivi = {"lun", "mar", "mer", "gio", "ven", "sab"}
    numero_massimo = 10
    sala = "Sala Pesi"
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
            self.view_prenotazione_sala_pesi.close()
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
        self.view_prenotazione_sala_pesi = Form
        Form.setObjectName("Form")
        Form.resize(758, 487)
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(20, 120, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("calendarWidget")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(20, 20, 351, 71))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(160, 100, 101, 16))
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(580, 110, 81, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(580, 210, 111, 16))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(580, 250, 131, 23))
        self.progressBar.setMaximum(10)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(550, 400, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.lblImmagineSalaPesi = QtWidgets.QLabel(Form)
        self.lblImmagineSalaPesi.setGeometry(QtCore.QRect(400, 10, 61, 61))
        self.lblImmagineSalaPesi.setText("")
        self.lblImmagineSalaPesi.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/IconaSalaPesi1.png"))
        self.lblImmagineSalaPesi.setScaledContents(True)
        self.lblImmagineSalaPesi.setObjectName("lblImmagineSalaPesi")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(580, 140, 111, 22))
        self.cmbOrario.setObjectName("cmbOrari")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")
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
        Form.setWindowTitle(_translate("Form", "Prenotazioni sala pesi"))
        self.lblInfo.setText(_translate("Form",
                                        "<html><head/><body><p>La Sala Pesi è aperta dal lunedì al sabato. <br/>La prenotazione è valida per 1 ora e 30 minuti dall\'ora selezionata.</p></body></html>"))
        self.lblTesto_1.setText(_translate("Form", "Scegli il giorno:"))
        self.lblTesto_2.setText(_translate("Form", "Scegli l\'ora"))
        self.lblTesto_3.setText(_translate("Form", "Posti disponibili:"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.cmbOrario.setItemText(0, _translate("Form", "09:30-11:00"))
        self.cmbOrario.setItemText(1, _translate("Form", "11:00-12:30"))
        self.cmbOrario.setItemText(2, _translate("Form", "12:30-14:00"))
        self.cmbOrario.setItemText(3, _translate("Form", "14:00-15:30"))
        self.cmbOrario.setItemText(4, _translate("Form", "15:30-17:00"))
        self.cmbOrario.setItemText(5, _translate("Form", "17:00-18:30"))
        self.cmbOrario.setItemText(6, _translate("Form", "18:30-20:00"))
        self.cmbOrario.setItemText(7, _translate("Form", "20:00-21:30"))
        self.cmbOrario.setItemText(8, _translate("Form", "21:30-23:00"))
