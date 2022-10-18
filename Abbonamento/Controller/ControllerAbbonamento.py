from Abbonamento.Model.Abbonamento import Abbonamento


class ControllerAbbonamento(object):
    def __init__(self):
        self.model = Abbonamento()

    def aggiungi_abbonamento_cliente(self, abbonamento):
        self.model.aggiungi_abbonamento(abbonamento)

    def get_abbonamento_cliente(self):
        self.model.get_abbonamento()

