from PyQt5.QtWidgets import QFileDialog

from Metodi.Metodi import Metodi
from Dieta.Model.Dieta import Dieta


class ControllerDieta(object):
    objMetodi = Metodi()
    percorso_info = "./Dieta/Data/DatiClienti.txt"

    def __init__(self):
        self.model = Dieta()

    def salva_info_dieta_cliente(self, username, altezza, peso, eta):
        self.model.salva_info_cliente(username, altezza, peso, eta)

    def aggiungi_info_dieta(self, dieta):
        self.model.aggiungi_info_dieta(dieta, self.percorso_info)

    def recupera_info_dieta(self):
        self.model.recupera_info_diete_salvate(self.percorso_info)

    def rimuovi_dieta_assegnata(self, username, percorso):
        self.model.rimuovi_dieta_assegnata(username, percorso)

    def get_info_dieta(self, username):
        return self.model.get_info_dieta(username)

    def get_gender(self, username):
        return self.model.get_gender(username)

    def get_eta(self, username):
        return self.model.get_eta(username)

    def get_peso(self, username):
        return self.model.get_peso(username)

    def get_altezza(self, username):
        return self.model.get_altezza(username)

    def calcola_peso_ideale(self, altezza, eta, sesso):
        coefficiente_peso_maschio = 100
        coefficiente_peso_femmina = 112
        weight = 0
        if sesso == "maschio":
            weight = 0.8 * (altezza * 100 - coefficiente_peso_maschio) + eta / 2
        elif sesso == "femmina":
            weight = 0.8 * (altezza * 100 - coefficiente_peso_femmina) + eta / 2
        return weight

    def calcola_bmi(self, altezza, peso):
        bmi = peso / (altezza * altezza)
        return bmi

    def calcolo_ads(self, lavoro, attivita_fisica):
        if lavoro == "Lavori edile" or lavoro == "Lavori agricoli" or lavoro == "Operaio/a(pesante)":
            coefficiente_lavoro = 15
        else:
            coefficiente_lavoro = 10
        if attivita_fisica == "oltre 5 ore settimanali":
            coefficiente_attivita = 20
        elif attivita_fisica == "da 3 a 5 ore settimanali":
            coefficiente_attivita = 15
        else:
            coefficiente_attivita = 10
        coefficiente = coefficiente_attivita + coefficiente_lavoro
        return coefficiente

    def calcolo_calorie(self, sesso, peso, altezza, eta, lavoro, attivita_fisica):
        vettore_risposte = []
        if sesso == "maschio":
            MB = 66 + 13.7 * peso + 5 * altezza - 6.8 * eta
            fabbisogno_calorico = 1 * peso * 24
            fabbisogno_calorico += (fabbisogno_calorico * self.calcolo_ads(lavoro, attivita_fisica)) / 100
            vettore_risposte.append(MB)
            vettore_risposte.append(fabbisogno_calorico)
            return vettore_risposte
        else:
            MB = 655 + 9.6 * peso + 1.8 * altezza - 4.7 * eta
            fabbisogno_calorico = 0.9 * peso * 24
            fabbisogno_calorico += (fabbisogno_calorico * self.calcolo_ads(lavoro, attivita_fisica)) / 100
            vettore_risposte.append(MB)
            vettore_risposte.append(fabbisogno_calorico)
            return vettore_risposte

    def crea_oggetto_dieta(self, username, bmi, peso_ideale, fabbisogno, segnalazioni):
        info_dieta = Dieta(username, bmi, peso_ideale, fabbisogno, segnalazioni)
        if self.model.controlla_ridondanza(username):
            self.model.rimuovi_info_dieta(username, self.percorso_info)
        self.model.aggiungi_info_dieta(info_dieta, self.percorso_info)

    def popola_lista_diete(self):
        return self.model.popola_lista_diete()

    def allega_file_dieta(self):
        try:
            filename = QFileDialog.getOpenFileName()
            return filename[0]
        except Exception:
            return





