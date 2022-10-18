from Metodi.Metodi import Metodi
from PyQt5.QtCore import QDate


class Allenamento(object):
    lista_allenamenti = []
    objMetodi = Metodi

    def __init__(self, username="", nome_esercizi="", numero_esercizi="", data_inizio="", data_fine=""):
        if username != "":
            self.username = username
            self.nome_esercizi = nome_esercizi
            self.numeri_esercizi = numero_esercizi
            self.data_inizio = data_inizio
            self.data_fine = data_fine

    def recupera_allenamenti_salvati(self, percorso):
        self.lista_allenamenti.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_allenamenti)

    def get_allenamento_by_user(self, username):
        for elem in self.lista_allenamenti:
            if elem.username == username:
                return elem
        return 0

    def controllo_data(self, allenamento):
        if self.get_allenamento_by_user(allenamento.username) == 0:
            return False
        elif QDate.fromString(self.get_allenamento_by_user(allenamento.username).data_fine, "dd/MM/yyyy") > \
                QDate.currentDate():
            return True
        else:
            return False

    def rimuovi_allenamento(self, allenamento):
        for elem in self.lista_allenamenti:
            if elem.username == allenamento.username:
                self.lista_allenamenti.remove(elem)

    def aggiungi_allenamento(self, allenamento, percorso):
        self.objMetodi.aggiungi_alla_lista(allenamento, self.lista_allenamenti)
        self.salva_lista_allenamenti(percorso)

    def salva_lista_allenamenti(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_allenamenti)

    def rimuovi_allenamento_cliente(self, username, percorso):
        for elem in self.lista_allenamenti:
            if elem.username == username:
                self.lista_allenamenti.remove(elem)
        self.salva_lista_allenamenti(percorso)
