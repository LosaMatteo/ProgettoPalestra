from PyQt5 import QtCore, QtGui, QtWidgets
from ViewsHome.ViewHomeAdmin import ViewHomeAdmin
from ViewsHome.ViewHomeStaff import ViewHomeStaff
from ViewsHome.ViewHomeCliente import ViewHomeCliente
from Metodi.Metodi import Metodi
from Cliente.Controller.ControllerCliente import ControllerCliente
from Staff.Controller.ControllerStaff import ControllerStaff
from Dieta.Controller.ControllerDieta import ControllerDieta
from Orario.Controller.ControllerOrario import ControllerOrario
from PreferenzaEsercizi.Controller.ControllerPreferenzaEsercizi import ControllerPreferenzaEsercizi
from Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione
from Allenamento.Controller.ControllerAllenamento import ControllerAllenamento


class ViewLogin(object):
    controller_cliente = ControllerCliente()
    controller_staff = ControllerStaff()
    controller_preferenza = ControllerPreferenzaEsercizi()
    controller_orario = ControllerOrario()
    controller_dieta = ControllerDieta()
    controller_prenotazione = ControllerPrenotazione()
    controller_allenamento = ControllerAllenamento()
    objMetodi = Metodi()
    lista_accessi = []
    credenziali_admin = dict()
    credenziali_admin["Admin"] = "1"

    def __init__(self):
        self.view_login = None

    def open_view_admin(self, username):
        self.view_admin = QtWidgets.QMainWindow()
        self.ui = ViewHomeAdmin(username, self.controller_cliente.get_lista_id_clienti(),
                                self.controller_staff.get_lista_id_staff(),
                                self.controller_cliente.popola_lista_clienti,
                                self.controller_staff.popola_lista_staff)
        self.ui.setupUi(self.view_admin)
        self.view_admin.show()

    def open_view_staff(self, username):
        self.view_staff = QtWidgets.QMainWindow()
        self.ui = ViewHomeStaff(username, self.controller_cliente.get_lista_id_clienti(),
                                self.controller_preferenza.get_preferenza_cliente,
                                self.controller_orario.get_lista_turni_data,
                                self.controller_dieta.get_info_dieta)
        self.ui.setupUi(self.view_staff)
        self.view_staff.show()

    def open_view_cliente(self, username):
        self.view_cliente = QtWidgets.QMainWindow()
        self.ui = ViewHomeCliente(username, self.controller_cliente.get_cliente_autenticazione(username),
                                  self.controller_prenotazione.get_lista_prenotazioni,
                                  self.controller_prenotazione.rimuovi_prenotazione,
                                  self.controller_allenamento.get_allenamento_cliente)
        self.ui.setupUi(self.view_cliente)
        self.view_cliente.show()

    def cancella_riempimento(self):
        self.lblError.setText("")
        self.txtBox_user.setText("")
        self.txtBox_psw.setText("")

    def split_line(self):
        self.lista_accessi.clear()
        self.lista_accessi.append(self.credenziali_admin)
        self.lista_accessi.append(self.controller_staff.get_psw_staff())
        self.lista_accessi.append(self.controller_cliente.get_psw_cliente())

    def login_check(self):
        try:
            datiaccesso = []
            datiaccesso.clear()
            self.lblError.setText("")
            user = self.txtBox_user.text()
            if user[-1] == " ":
                user = user[:-1]
            psw = self.txtBox_psw.text()
            i = 0
            for elem in self.lista_accessi:
                for usernames in elem.keys():
                    if usernames == user and elem[usernames] == psw:
                        datiaccesso.append(i)
                        datiaccesso.append(user)
                        return datiaccesso
                i += 1
            datiaccesso.append(-1)
            return datiaccesso
        except(Exception):
            self.objMetodi.show_popup_exception("Inserire i dati.")
            return 0

    def login(self):
        datiaccesso = self.login_check()
        if datiaccesso != 0:
            if datiaccesso[0] == 0:
                self.open_view_admin(datiaccesso[1])
                self.view_login.close()
            elif datiaccesso[0] == 1:
                self.controller_prenotazione.recupera_prenotazioni()
                self.controller_orario.recupera_turni_salvati()
                self.controller_dieta.recupera_info_dieta()
                self.controller_preferenza.recupera_preferenze()
                self.open_view_staff(datiaccesso[1])
                self.view_login.close()
            elif datiaccesso[0] == 2:
                self.controller_prenotazione.recupera_prenotazioni()
                self.controller_orario.recupera_turni_salvati()
                self.controller_preferenza.recupera_preferenze()
                self.controller_allenamento.recupera_allenamenti_salvati()
                self.open_view_cliente(datiaccesso[1])
                self.view_login.close()
            else:
                self.objMetodi.show_popup_exception("username o password errata.")

    def hide_password(self):
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hide_password_return(self):
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, ViewLogin):
        self.view_login = ViewLogin
        ViewLogin.setObjectName("ATHENEO")
        ViewLogin.resize(867, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewLogin.sizePolicy().hasHeightForWidth())
        ViewLogin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        ViewLogin.setFont(font)
        ViewLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ViewLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(190, 20, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblUser = QtWidgets.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(230, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblUser.setFont(font)
        self.lblUser.setObjectName("lblUser")
        self.txtBox_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBox_user.setGeometry(QtCore.QRect(330, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.txtBox_user.setFont(font)
        self.txtBox_user.setText("")
        self.txtBox_user.setObjectName("txtBox_user")
        self.lblPsw = QtWidgets.QLabel(self.centralwidget)
        self.lblPsw.setGeometry(QtCore.QRect(230, 220, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblPsw.setFont(font)
        self.lblPsw.setObjectName("lblPsw")
        self.txtBox_psw = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBox_psw.setGeometry(QtCore.QRect(330, 220, 201, 31))
        self.txtBox_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtBox_psw.setObjectName("txtBox_psw")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(280, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.lblInfo = QtWidgets.QLabel(self.centralwidget)
        self.lblInfo.setGeometry(QtCore.QRect(220, 380, 521, 16))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblInfo.setFont(font)
        self.lblInfo.setObjectName("lblInfo")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(580, 80, 201, 101))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap("Resources/images/palestra.jpg"))
        self.lblLogo.setObjectName("lblLogo")
        self.lblError = QtWidgets.QLabel(self.centralwidget)
        self.lblError.setGeometry(QtCore.QRect(300, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lblError.setFont(font)
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(440, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.btnNascondiPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnNascondiPassword.setGeometry(QtCore.QRect(500, 230, 21, 16))
        self.btnNascondiPassword.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/images/pngGUI_client/download.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btnNascondiPassword.setIcon(icon)
        self.btnNascondiPassword.setIconSize(QtCore.QSize(20, 20))
        self.btnNascondiPassword.setObjectName("pushButton_7")
        ViewLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        ViewLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewLogin)
        self.statusbar.setObjectName("statusbar")
        ViewLogin.setStatusBar(self.statusbar)
        self.retranslateUi(ViewLogin)
        QtCore.QMetaObject.connectSlotsByName(ViewLogin)

        self.controller_cliente.recupera_clienti_salvati()
        self.controller_staff.recupera_dipendenti_salvati()
        self.split_line()
        self.btnLogin.clicked.connect(self.login)
        self.btnCancel.clicked.connect(self.cancella_riempimento)
        self.btnNascondiPassword.pressed.connect(self.hide_password)
        self.btnNascondiPassword.clicked.connect(self.hide_password_return)

    def retranslateUi(self, ViewLogin):
        _translate = QtCore.QCoreApplication.translate
        ViewLogin.setWindowTitle(_translate("ATHENEO", "ATHENEO - Login"))
        self.lblTitle.setText(_translate("ATHENEO", "ATHENEO  FITNESS  CLUB"))
        self.lblUser.setText(_translate("ATHENEO", "Username"))
        self.lblPsw.setText(_translate("ATHENEO", "Password"))
        self.btnLogin.setText(_translate("ATHENEO", "Login"))
        self.btnCancel.setText(_translate("ATHENEO", "Cancella"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ATHENEO = QtWidgets.QMainWindow()
    ui = ViewLogin()
    ui.setupUi(ATHENEO)
    ATHENEO.show()
    sys.exit(app.exec_())
