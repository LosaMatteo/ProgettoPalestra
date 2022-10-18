from Attrezzo.Model.Attrezzo import Attrezzo


class ControllerAttrezzo(object):
    percorso = "./Attrezzo/Data/ListaAttrezzi.txt"

    def __init__(self):
        self.model = Attrezzo()

    def aggiungi_attrezzo(self, attrezzo):
        self.model.aggiungi_attrezzo(attrezzo, self.percorso)
        self.model.scrivi_lista_attrezzi(self.percorso)

    def popola_lista_attrezzi(self):
        return self.model.popola_lista_attrezzi()

    def recupera_attrezzi_salvati(self):
        self.model.recupera_attrezzi_salvati(self.percorso)

    def rimuovi_attrezzo(self, riga):
        self.model.rimuovi_attrezzo(riga, self.percorso)