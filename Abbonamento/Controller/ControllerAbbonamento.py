from Abbonamento.Model.Abbonamento import Abbonamento


class ControllerAbbonamento(object):
    def __init__(self):
        self.model = Abbonamento()

    def aggiungi_abbonamento_cliente(self, abbonamento):
        self.model.aggiungi_abbonamento(abbonamento)

