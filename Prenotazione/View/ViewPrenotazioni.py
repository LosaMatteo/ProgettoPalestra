from PyQt5 import QtCore, QtGui, QtWidgets
from Prenotazione.View.ViewPrenotazioneZumba import ViewPrenotazioneZumba
from Prenotazione.View.ViewPrenotazioneFunzionale import ViewPrenotazioneFunzionale
from Prenotazione.View.ViewPrenotazioneSalaPesi import ViewPrenotazioneSalaPesi


class ViewPrenotazioni(object):

    def __init__(self, username, aggiorna_prenotazioni):
        self.username = username
        self.aggiorna_prenotazioni = aggiorna_prenotazioni

    def open_prenotazione_sala_pesi(self):
        self.prenotazione_sala_pesi = QtWidgets.QMainWindow()
        self.ui = ViewPrenotazioneSalaPesi(self.username, self.aggiorna_prenotazioni)
        self.ui.setupUi(self.prenotazione_sala_pesi)
        self.prenotazione_sala_pesi.show()

    def open_prenotazione_funzionale(self):
        self.prenotazione_funzionale = QtWidgets.QMainWindow()
        self.ui = ViewPrenotazioneFunzionale(self.username, self.aggiorna_prenotazioni)
        self.ui.setupUi(self.prenotazione_funzionale)
        self.prenotazione_funzionale.show()

    def open_prenotazione_zumba(self):
        self.prenotazione_zumba = QtWidgets.QMainWindow()
        self.ui = ViewPrenotazioneZumba(self.username, self.aggiorna_prenotazioni)
        self.ui.setupUi(self.prenotazione_zumba)
        self.prenotazione_zumba.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(689, 576)
        self.lblTitolo = QtWidgets.QLabel(Form)
        self.lblTitolo.setGeometry(QtCore.QRect(200, 70, 261, 81))
        self.lblTitolo.setScaledContents(True)
        self.lblTitolo.setObjectName("lblTitolo")
        self.lblImmagineIntestazione = QtWidgets.QLabel(Form)
        self.lblImmagineIntestazione.setGeometry(QtCore.QRect(470, 80, 71, 71))
        self.lblImmagineIntestazione.setText("")
        self.lblImmagineIntestazione.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/Prenot1.png"))
        self.lblImmagineIntestazione.setScaledContents(True)
        self.lblImmagineIntestazione.setObjectName("lblImmagineIntestazione")
        self.btnApriSalaPesi = QtWidgets.QPushButton(Form)
        self.btnApriSalaPesi.setGeometry(QtCore.QRect(50, 420, 113, 32))
        self.btnApriSalaPesi.setObjectName("btnApriSalaPesi")
        self.btnApriFunzionale = QtWidgets.QPushButton(Form)
        self.btnApriFunzionale.setGeometry(QtCore.QRect(300, 420, 113, 32))
        self.btnApriFunzionale.setObjectName("btnApriFunzionale")
        self.btnApriZumba = QtWidgets.QPushButton(Form)
        self.btnApriZumba.setGeometry(QtCore.QRect(530, 420, 113, 32))
        self.btnApriZumba.setObjectName("btnApriZumba")
        self.lblImmagineSalaPesi = QtWidgets.QLabel(Form)
        self.lblImmagineSalaPesi.setGeometry(QtCore.QRect(20, 240, 181, 151))
        self.lblImmagineSalaPesi.setText("")
        self.lblImmagineSalaPesi.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/SalaPesi.png"))
        self.lblImmagineSalaPesi.setScaledContents(True)
        self.lblImmagineSalaPesi.setObjectName("lblImmagineSalaPesi")
        self.lblImmagineZumba = QtWidgets.QLabel(Form)
        self.lblImmagineZumba.setGeometry(QtCore.QRect(500, 240, 181, 151))
        self.lblImmagineZumba.setText("")
        self.lblImmagineZumba.setTextFormat(QtCore.Qt.RichText)
        self.lblImmagineZumba.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/zumba.png"))
        self.lblImmagineZumba.setScaledContents(True)
        self.lblImmagineZumba.setObjectName("lblImmagineZumba")
        self.lblImmagineFunctional = QtWidgets.QLabel(Form)
        self.lblImmagineFunctional.setGeometry(QtCore.QRect(270, 240, 171, 151))
        self.lblImmagineFunctional.setText("")
        self.lblImmagineFunctional.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/funzionale.png"))
        self.lblImmagineFunctional.setScaledContents(True)
        self.lblImmagineFunctional.setObjectName("lblImmagineFunctional")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnApriSalaPesi.clicked.connect(self.open_prenotazione_sala_pesi)
        self.btnApriFunzionale.clicked.connect(self.open_prenotazione_funzionale)
        self.btnApriZumba.clicked.connect(self.open_prenotazione_zumba)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prenotazioni"))
        self.lblTitolo.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">PRENOTAZIONI</span></p></body></html>"))
        self.btnApriSalaPesi.setText(_translate("Form", "Sala Pesi"))
        self.btnApriFunzionale.setText(_translate("Form", "Funzionale"))
        self.btnApriZumba.setText(_translate("Form", "Zumba"))
