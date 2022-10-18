from Metodi.Metodi import Metodi


class Abbonamento(object):
    lista_abbonamenti = []
    objMetodi = Metodi()

    def __init__(self, data_iscrizione="", data_certificato_medico="", tipo_di_abbonamento=""):
        if data_iscrizione != "":
            self.data_iscrizione = data_iscrizione
            self.data_certificato_medico = data_certificato_medico
            self.tipo_di_abbonamento = tipo_di_abbonamento

    def aggiungi_abbonamento(self, obj):
        self.objMetodi.aggiungi_alla_lista(obj, self.lista_abbonamenti)

    def get_abbonamento(self):
        abbonamento = self.lista_abbonamenti[0]
        self.lista_abbonamenti.pop()
        return abbonamento
