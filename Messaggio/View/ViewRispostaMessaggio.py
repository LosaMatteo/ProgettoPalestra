from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from Metodi.Metodi import Metodi
from Messaggio.Model.Messaggio import Messaggio
from Messaggio.Controller.ControllerMessaggio import ControllerMessaggio


class ViewRispostaMessaggio(object):
    objMetodi = Metodi()

    def __init__(self, messaggio, aggiorna_messaggi):
        self.messaggio = messaggio
        self.aggiorna_messaggi = aggiorna_messaggi
        self.controller = ControllerMessaggio()

    def scrivi_messaggio(self):
        messaggio_risposta = Messaggio(self.messaggio.destinatario, self.messaggio.mittente, self.ptxTesto.toPlainText(),
                                       datetime.today().strftime('%Y-%m-%d-%H:%M'))
        if self.controller.spedisci_messaggio(messaggio_risposta):
            self.aggiorna_messaggi()
            self.objMetodi.show_popup_ok("Il tuo messaggio è stato inviato correttamente")
        else:
            self.objMetodi.show_popup_exception("Impossibile mandare un messaggio vuoto.")
        self.view_risposta_messaggio.close()

    def setupUi(self, MainWindow):
        self.view_risposta_messaggio = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(70, 80, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.ptxTesto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxTesto.setGeometry(QtCore.QRect(140, 90, 421, 211))
        self.ptxTesto.setPlainText("")
        self.ptxTesto.setObjectName("ptxTesto")
        self.btnInviaMessaggio = QtWidgets.QPushButton(self.centralwidget)
        self.btnInviaMessaggio.setGeometry(QtCore.QRect(410, 320, 141, 28))
        self.btnInviaMessaggio.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnInviaMessaggio.clicked.connect(self.scrivi_messaggio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rispondi"))
        self.lblTesto_1.setText(_translate("MainWindow", "Oggetto:"))
        self.btnInviaMessaggio.setText(_translate("MainWindow", "Invia Messaggio"))