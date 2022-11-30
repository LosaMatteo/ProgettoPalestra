from PyQt5.QtCore import QDate
from Metodi.Metodi import Metodi
from Cliente.Model.Cliente import Cliente



class Prenotazione(object):
    lista_prenotazioni = []
    objMetodi = Metodi()

    def __init__(self, username="", sala="", data="", orario=""):
        if username != "":
            self.username = username
            self.sala = sala
            self.data = data
            self.orario = orario

    def recupera_prenotazioni(self, percorso):
        self.lista_prenotazioni.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_prenotazioni)

    def aggiungi_prenotazione(self, obj, percorso):
        self.objMetodi.aggiungi_alla_lista(obj, self.lista_prenotazioni)
        self.scrivi_lista_prenotazioni(percorso)

    def scrivi_lista_prenotazioni(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_prenotazioni)

    def get_lista_prenotazioni(self, percorso):
        if self.lista_prenotazioni is not None:
            self.elimina_vecchie_prenotazioni(percorso)
        return self.lista_prenotazioni

    def get_posti_disponibili(self, sala, data, ora):
        indice = 0
        for elem in self.lista_prenotazioni:
            if elem.sala == sala and elem.data == data and elem.orario == ora:
                indice += 1
        return indice

    def controlla_ridondanza(self, prenotazione):
        for elem in self.lista_prenotazioni:
            if self.confronta_data_prenotazioni(elem, prenotazione):
                return False
        return True

    def effettua_prenotazione(self, limite_massimo, prenotazione, percorso):
        if self.get_posti_disponibili(prenotazione.sala, prenotazione.data, prenotazione.orario) < limite_massimo and \
                self.controlla_ridondanza(prenotazione):
            self.aggiungi_prenotazione(prenotazione, percorso)
            return True
        return False

    def elimina_vecchie_prenotazioni(self, percorso):
        for elem in self.lista_prenotazioni:
            if QDate.currentDate() > elem.data:
                self.lista_prenotazioni.remove(elem)
        self.scrivi_lista_prenotazioni(percorso)

    def rimuovi_prenotazione(self, prenotazione, percorso):
        if prenotazione != 0:
            for elem in self.lista_prenotazioni:
                if self.confronta_data_prenotazioni(elem, prenotazione):
                    self.lista_prenotazioni.remove(elem)
            self.scrivi_lista_prenotazioni(percorso)

    def confronta_data_prenotazioni(self, prenotazione1, prenotazione2):
        if prenotazione1.username == prenotazione2.username and \
                prenotazione1.data.toString("dd/MM/yyyy") == prenotazione2.data.toString("dd/MM/yyyy") and \
                prenotazione1.sala == prenotazione2.sala and prenotazione1.orario == prenotazione2.orario:
            return True
        return False

    def get_prenotazione_by_username(self, username):
        for elem in self.lista_prenotazioni:
            if elem.username == username:
                return elem
        return 0

    def controlla_apertura(self, data_selezionata, giorni_attivi):
        for elem in giorni_attivi:
            if data_selezionata.toString()[:3] == elem:
                return True
        return False
