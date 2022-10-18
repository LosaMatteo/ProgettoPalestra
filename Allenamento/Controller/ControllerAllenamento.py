from Allenamento.Model.Allenamento import Allenamento


class ControllerAllenamento(object):
    percorso = "./Allenamento/Data/SchedeAllenamento.txt"

    def __init__(self):
        self.model = Allenamento()

    def get_allenamento_cliente(self, username):
        return self.model.get_allenamento_by_user(username)

    def controllo_scadenza(self, allenamento):
        self.model.controllo_data(allenamento)

    def sovrascrivi_allenamento(self, allenamento):
        self.model.rimuovi_allenamento(allenamento)
        self.model.aggiungi_allenamento(allenamento, self.percorso)

    def aggiungi_allenamento(self, allenamento):
        self.model.aggiungi_allenamento(allenamento, self.percorso)

    def recupera_allenamenti_salvati(self):
        self.model.recupera_allenamenti_salvati(self.percorso)

    def salva_lista_allenamenti(self):
        self.model.salva_lista_allenamenti(self.percorso)

    def rimuovi_allenamento_cliente(self, username):
        self.model.rimuovi_allenamento_cliente(username, self.percorso)




