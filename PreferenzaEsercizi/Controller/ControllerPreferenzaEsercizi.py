from PreferenzaEsercizi.Model.PreferenzaEsercizi import PreferenzaEsercizi


class ControllerPreferenzaEsercizi(object):
    percorso = "./PreferenzaEsercizi/Data/ListaPreferenze.txt"

    def __init__(self):
        self.model = PreferenzaEsercizi()

    def aggiungi_preferenza(self, preferenza):
        self.model.aggiungi_preferenza(preferenza, self.percorso)

    def recupera_preferenze(self):
        self.model.recupera_preferenze(self.percorso)

    def get_preferenza_cliente(self, username):
        return self.model.get_preferenza(username)