from PyQt5 import QtCore, QtWidgets
from Messaggio.View.ViewRispostaMessaggio import ViewRispostaMessaggio


class ViewLeggiMessaggio(object):

    def __init__(self, username, messaggio, aggiorna_messaggi):
        self.username = username
        self.messaggio = messaggio
        self.aggiorna_messaggi = aggiorna_messaggi

    def apriCasellaMessaggi(self):
        self.risposta_messaggio = QtWidgets.QMainWindow()
        self.ui = ViewRispostaMessaggio(self.messaggio, self.aggiorna_messaggi)
        self.ui.setupUi(self.risposta_messaggio)
        self.risposta_messaggio.show()

    def setupUi(self, MainWindow):
        self.leggi_messaggio = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ptxContenuto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxContenuto.setGeometry(QtCore.QRect(90, 110, 481, 241))
        self.ptxContenuto.setObjectName("ptxContenuto")
        self.ptxContenuto.setReadOnly(True)
        self.btnRispondi = QtWidgets.QPushButton(self.centralwidget)
        self.btnRispondi.setGeometry(QtCore.QRect(310, 370, 121, 28))
        self.btnRispondi.setObjectName("btnRispondi")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(450, 370, 121, 28))
        self.btnIndietro.setObjectName("btnIndietro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        if self.messaggio.mittente == self.username:
            self.btnRispondi.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnIndietro.clicked.connect(self.leggi_messaggio.close)
        self.btnRispondi.clicked.connect(self.apriCasellaMessaggi)
        self.ptxContenuto.setPlainText(self.messaggio.contenuto)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Messaggio"))
        self.btnRispondi.setText(_translate("MainWindow", "Rispondi"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))


