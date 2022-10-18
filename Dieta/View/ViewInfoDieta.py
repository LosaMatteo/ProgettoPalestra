from PyQt5 import QtCore, QtGui, QtWidgets
from Dieta.View.ViewDietaChetogenica import ViewDietaChetogenica
from Dieta.View.ViewDietaIpocalorica import ViewDietaIpocalorica
from Dieta.View.ViewDietaIpercalorica import ViewDietaIpercalorica
from Metodi.Metodi import Metodi
from Dieta.Model.Dieta import Dieta
from Dieta.Controller.ControllerDieta import ControllerDieta


class ViewInfoDieta(object):
    objMetodi = Metodi()

    def __init__(self, username):
        self.username = username
        self.controller = ControllerDieta()

    def salva_dati_fisiologoci(self):
        self.controller.salva_info_dieta_cliente(self.username, str(self.txtAltezza.text()), str(self.txtPeso.text()),
                                         str(self.txtEta.text()))

    def calcola_bmi(self):
        try:
            altezza = float(self.txtAltezza.text()) / 100
            peso = float(self.txtPeso.text())
            self.salva_dati_fisiologoci()
            self.lblIndiceBMI.setText(str(self.controller.calcola_bmi(altezza, peso).__round__(2)))
        except Exception:
            self.objMetodi.show_popup_exception("Non hai inserito altezza e/o peso!")

    def salva_info_dieta(self):
        try:
            info_dieta = Dieta(self.username, self.lblIndiceBMI.text(),
                                        self.lblPesoIdeale.text(), self.lblFabbisogno.text(),
                                        self.ptxSegnalazioni.toPlainText())
            self.controller.aggiungi_info_dieta(info_dieta)
            self.objMetodi.show_popup_ok("Dati fisiologici e preferenze salvate")
            self.view_info_dieta.close()
        except Exception:
            self.objMetodi.show_popup_exception("Errore nel salvataggio")

    def calcola_peso_ideale(self):
        try:
            altezza = float(self.txtAltezza.text()) / 100
            eta = int(self.txtEta.text())
            self.salva_dati_fisiologoci()
            sesso = self.comboBox.currentText()
            self.lblPesoIdeale.setText(str(self.controller.calcola_peso_ideale(altezza, eta, sesso).__round__(2)))
        except Exception:
            self.objMetodi.show_popup_exception("Non hai inserito altezza, peso ed età!")

    def calcolo_calorie(self):
        try:
            self.salva_dati_fisiologoci()
            vettore_dati = self.controller.calcolo_calorie(self.controller.get_gender(self.username),
                                                          float(self.controller.get_peso(self.username)),
                                                          float(self.controller.get_altezza(self.username)),
                                                          float(self.controller.get_eta(self.username)),
                                                          self.cmbLavoro.currentText(), self.cmbAttFisica.currentText())
            self.lblMB.setText(str(vettore_dati[0].__round__(2)))
            self.lblFabbisogno.setText(str(vettore_dati[1].__round__(2)))
        except Exception:
            self.objMetodi.show_popup_exception("Non hai inserito altezza, peso ed età!")

    def popola_lista_dieta(self):
        if self.controller.popola_lista_diete() == 0:
            self.objMetodi.show_popup_exception("Dati generici delle diete non trovati.")
        else:
            for elem in self.controller.popola_lista_diete():
                self.listWidget.addItem(elem)
                self.listWidget.show()

    def open_dieta_chetogenica(self):
        self.dieta_chetogenica = QtWidgets.QMainWindow()
        self.ui = ViewDietaChetogenica()
        self.ui.setupUi(self.dieta_chetogenica)
        self.dieta_chetogenica.show()

    def open_dieta_ipocalorica(self):
        self.dieta_ipocalorica = QtWidgets.QMainWindow()
        self.ui = ViewDietaIpocalorica()
        self.ui.setupUi(self.dieta_ipocalorica)
        self.dieta_ipocalorica.show()

    def open_dieta_ipercalorica(self):
        self.dieta_ipercalorica = QtWidgets.QMainWindow()
        self.ui = ViewDietaIpercalorica()
        self.ui.setupUi(self.dieta_ipercalorica)
        self.dieta_ipercalorica.show()

    def apri_interfacce(self):
        if self.listWidget.currentItem().text() == "dieta chetogenica":
                self.open_dieta_chetogenica()
        elif self.listWidget.currentItem().text() == "dieta ipocalorica":
                self.open_dieta_ipocalorica()
        elif self.listWidget.currentItem().text() == "dieta ipercalorica":
                self.open_dieta_ipercalorica()

    def setupUi(self, Form):
            self.view_info_dieta = Form
            Form.setObjectName("Form")
            Form.resize(763, 528)
            self.toolBox = QtWidgets.QToolBox(Form)
            self.toolBox.setGeometry(QtCore.QRect(40, 20, 571, 481))
            self.toolBox.setObjectName("toolBox")
            self.page = QtWidgets.QWidget()
            self.page.setGeometry(QtCore.QRect(0, 0, 571, 357))
            self.page.setObjectName("page")
            self.label = QtWidgets.QLabel(self.page)
            self.label.setGeometry(QtCore.QRect(0, 0, 121, 251))
            self.label.setObjectName("label")
            self.comboBox = QtWidgets.QComboBox(self.page)
            self.comboBox.setGeometry(QtCore.QRect(50, 200, 104, 31))
            self.comboBox.setMaxVisibleItems(2)
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.txtPeso = QtWidgets.QLineEdit(self.page)
            self.txtPeso.setGeometry(QtCore.QRect(80, 120, 71, 21))
            self.txtPeso.setObjectName("lineEdit")
            self.txtAltezza = QtWidgets.QLineEdit(self.page)
            self.txtAltezza.setGeometry(QtCore.QRect(80, 70, 71, 21))
            self.txtAltezza.setObjectName("lineEdit_2")
            self.btnBMI = QtWidgets.QPushButton(self.page)
            self.btnBMI.setGeometry(QtCore.QRect(20, 270, 151, 32))
            self.btnBMI.setObjectName("pushButton")
            self.btnPesoForma = QtWidgets.QPushButton(self.page)
            self.btnPesoForma.setGeometry(QtCore.QRect(330, 270, 151, 32))
            self.btnPesoForma.setObjectName("pushButton_2")
            self.label_2 = QtWidgets.QLabel(self.page)
            self.label_2.setGeometry(QtCore.QRect(10, 310, 71, 21))
            self.label_2.setObjectName("label_2")
            self.lblIndiceBMI = QtWidgets.QLabel(self.page)
            self.lblIndiceBMI.setGeometry(QtCore.QRect(90, 310, 51, 21))
            self.lblIndiceBMI.setText("")
            self.lblIndiceBMI.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.page)
            self.label_4.setGeometry(QtCore.QRect(150, 310, 51, 21))
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self.page)
            self.label_5.setGeometry(QtCore.QRect(330, 310, 121, 21))
            self.label_5.setObjectName("label_5")
            self.lblPesoIdeale = QtWidgets.QLabel(self.page)
            self.lblPesoIdeale.setGeometry(QtCore.QRect(460, 310, 51, 21))
            self.lblPesoIdeale.setText("")
            self.lblPesoIdeale.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.page)
            self.label_7.setGeometry(QtCore.QRect(520, 310, 41, 21))
            self.label_7.setObjectName("label_7")
            self.label_19 = QtWidgets.QLabel(self.page)
            self.label_19.setGeometry(QtCore.QRect(250, 60, 311, 131))
            self.label_19.setText("")
            self.label_19.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/logoMPT.png"))
            self.label_19.setScaledContents(True)
            self.label_19.setObjectName("label_19")
            self.txtEta = QtWidgets.QLineEdit(self.page)
            self.txtEta.setGeometry(QtCore.QRect(80, 160, 71, 21))
            self.txtEta.setObjectName("lineEdit_4")
            self.toolBox.addItem(self.page, "")
            self.page_2 = QtWidgets.QWidget()
            self.page_2.setGeometry(QtCore.QRect(0, 0, 571, 357))
            self.page_2.setObjectName("page_2")
            self.label_8 = QtWidgets.QLabel(self.page_2)
            self.label_8.setGeometry(QtCore.QRect(0, 0, 191, 201))
            self.label_8.setObjectName("label_8")
            self.cmbLavoro = QtWidgets.QComboBox(self.page_2)
            self.cmbLavoro.setGeometry(QtCore.QRect(100, 100, 201, 26))
            self.cmbLavoro.setObjectName("comboBox_2")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbLavoro.addItem("")
            self.cmbAttFisica = QtWidgets.QComboBox(self.page_2)
            self.cmbAttFisica.setGeometry(QtCore.QRect(100, 150, 201, 26))
            self.cmbAttFisica.setObjectName("comboBox_3")
            self.cmbAttFisica.addItem("")
            self.cmbAttFisica.addItem("")
            self.cmbAttFisica.addItem("")
            self.cmbAttFisica.addItem("")
            self.btnCalorie = QtWidgets.QPushButton(self.page_2)
            self.btnCalorie.setGeometry(QtCore.QRect(50, 200, 113, 31))
            self.btnCalorie.setObjectName("pushButton_3")
            self.label_9 = QtWidgets.QLabel(self.page_2)
            self.label_9.setGeometry(QtCore.QRect(0, 250, 131, 21))
            self.label_9.setObjectName("label_9")
            self.label_11 = QtWidgets.QLabel(self.page_2)
            self.label_11.setGeometry(QtCore.QRect(210, 250, 31, 21))
            self.label_11.setObjectName("label_11")
            self.label_12 = QtWidgets.QLabel(self.page_2)
            self.label_12.setGeometry(QtCore.QRect(210, 280, 31, 21))
            self.label_12.setObjectName("label_12")
            self.lblMB = QtWidgets.QLabel(self.page_2)
            self.lblMB.setGeometry(QtCore.QRect(140, 250, 51, 21))
            self.lblMB.setText("")
            self.lblMB.setObjectName("label_10")
            self.lblFabbisogno = QtWidgets.QLabel(self.page_2)
            self.lblFabbisogno.setGeometry(QtCore.QRect(140, 280, 51, 21))
            self.lblFabbisogno.setText("")
            self.lblFabbisogno.setObjectName("label_13")
            self.label_14 = QtWidgets.QLabel(self.page_2)
            self.label_14.setGeometry(QtCore.QRect(0, 280, 131, 21))
            self.label_14.setObjectName("label_14")
            self.label_20 = QtWidgets.QLabel(self.page_2)
            self.label_20.setGeometry(QtCore.QRect(330, 220, 221, 151))
            self.label_20.setText("")
            self.label_20.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/calcolo-fabbisogno-calorico.png"))
            self.label_20.setScaledContents(True)
            self.label_20.setObjectName("label_20")
            self.toolBox.addItem(self.page_2, "")
            self.page_3 = QtWidgets.QWidget()
            self.page_3.setGeometry(QtCore.QRect(0, 0, 571, 357))
            self.page_3.setObjectName("page_3")
            self.listWidget = QtWidgets.QListWidget(self.page_3)
            self.listWidget.setGeometry(QtCore.QRect(240, 60, 261, 192))
            self.listWidget.setObjectName("listWidget")
            self.label_17 = QtWidgets.QLabel(self.page_3)
            self.label_17.setGeometry(QtCore.QRect(10, 30, 211, 101))
            self.label_17.setObjectName("label_17")
            self.label_18 = QtWidgets.QLabel(self.page_3)
            self.label_18.setGeometry(QtCore.QRect(30, 130, 171, 121))
            self.label_18.setText("")
            self.label_18.setPixmap(QtGui.QPixmap("./Resources/images/pngDieta/immagine_dieta.jpeg"))
            self.label_18.setScaledContents(True)
            self.label_18.setObjectName("label_18")
            self.toolBox.addItem(self.page_3, "")
            self.page_4 = QtWidgets.QWidget()
            self.page_4.setObjectName("page_4")
            self.ptxSegnalazioni = QtWidgets.QPlainTextEdit(self.page_4)
            self.ptxSegnalazioni.setGeometry(QtCore.QRect(80, 50, 441, 261))
            self.ptxSegnalazioni.setObjectName("ptxSegnalazioni")
            self.label_15 = QtWidgets.QLabel(self.page_4)
            self.label_15.setGeometry(QtCore.QRect(30, 10, 511, 31))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.label_15.setFont(font)
            self.label_15.setObjectName("label_15")
            self.btnSalva = QtWidgets.QPushButton(self.page_4)
            self.btnSalva.setGeometry(QtCore.QRect(412, 327, 111, 21))
            self.btnSalva.setObjectName("btnSalva")
            self.toolBox.addItem(self.page_4, "")
            self.retranslateUi(Form)
            self.toolBox.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Form)
            self.popola_lista_dieta()
            self.btnBMI.clicked.connect(self.calcola_bmi)
            self.btnPesoForma.clicked.connect(self.calcola_peso_ideale)
            self.btnCalorie.clicked.connect(self.calcolo_calorie)
            self.listWidget.clicked.connect(self.apri_interfacce)
            self.btnSalva.clicked.connect(self.salva_info_dieta)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Dieta cliente"))
            self.label.setText(_translate("Form",
                                          "<html><head/><body><p><span style=\" font-weight:600;\">Inserisci i tuoi dati:</span><br/></p><p>Altezza(cm): <br/></p><p>Peso(kg):<br/></p><p>Età:<br/></p><p>Sesso:</p></body></html>"))
            self.comboBox.setItemText(0, _translate("Form", "maschio"))
            self.comboBox.setItemText(1, _translate("Form", "femmina"))
            self.btnBMI.setText(_translate("Form", "Calcola BMI"))
            self.btnPesoForma.setText(_translate("Form", "Calcola Peso Forma"))
            self.label_2.setText(_translate("Form", "<html><head/><body><p>Il tuo BMI è: </p></body></html>"))
            self.label_4.setText(_translate("Form", "kg/m2"))
            self.label_5.setText(_translate("Form", "<html><head/><body><p>Il tuo Peso Forma è:</p></body></html>"))
            self.label_7.setText(_translate("Form", "kg"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Calcola BMI e Peso Forma"))
            self.label_8.setText(_translate("Form",
                                            "<html><head/><body><p><span style=\" font-weight:600;\">Imposta i seguenti parametri:</span></p><p><br/></p><p>Lavoro:</p><p><br/>Attività Fisica:</p></body></html>"))
            self.cmbLavoro.setItemText(0, _translate("Form", "Casalingo/a o collaboratore domestico"))
            self.cmbLavoro.setItemText(1, _translate("Form", "Commesso/a"))
            self.cmbLavoro.setItemText(2, _translate("Form", "Dirigente"))
            self.cmbLavoro.setItemText(3, _translate("Form", "Impiegato"))
            self.cmbLavoro.setItemText(4, _translate("Form", "Lavori agricoli"))
            self.cmbLavoro.setItemText(5, _translate("Form", "Lavori edili"))
            self.cmbLavoro.setItemText(6, _translate("Form", "Libero professionista"))
            self.cmbLavoro.setItemText(7, _translate("Form", "Operaio/a (leggero)"))
            self.cmbLavoro.setItemText(8, _translate("Form", "Operaio/a (pesante)"))
            self.cmbLavoro.setItemText(9, _translate("Form", "Studente"))
            self.cmbAttFisica.setItemText(0, _translate("Form", "Nessuna"))
            self.cmbAttFisica.setItemText(1, _translate("Form", "fino a 2 ore settimanali"))
            self.cmbAttFisica.setItemText(2, _translate("Form", "da 3 a 5 ore settimanali"))
            self.cmbAttFisica.setItemText(3, _translate("Form", "oltre 5 ore settimanali"))
            self.btnCalorie.setText(_translate("Form", "Calcola ora!"))
            self.label_9.setText(_translate("Form", "<html><head/><body><p>Metabolismo basale:</p></body></html>"))
            self.label_11.setText(_translate("Form", "Kcal"))
            self.label_12.setText(_translate("Form", "Kcal"))
            self.label_14.setText(_translate("Form", "<html><head/><body><p>Fabbisogno Calorico:</p></body></html>"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.page_2),
                                     _translate("Form", "Calcola Fabbisogno e Metabolismo Basale"))
            self.label_17.setText(_translate("Form",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Diete che </span></p><p align=\"center\"><span style=\" font-size:12pt;\">potrebbero interessarti</span></p></body></html>"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Dieta"))
            self.label_15.setText(_translate("Form",
                                             "<html><head/><body><p>Segnala al nutrizionista eventuali allergie o preferenze alimentari:</p><p><br/></p><p><br/></p></body></html>"))
            self.btnSalva.setText(_translate("Form", "Salva"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Note per il nutrizionista"))