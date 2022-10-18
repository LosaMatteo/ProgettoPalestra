from Metodi.Metodi import Metodi


class Attrezzo(object):
    lista_attrezzi = []
    objMetodi = Metodi()

    def __init__(self, descrizione="", data_acquisto="", quantita="", prezzo_unitario="", data_manutenzione=""):
        if descrizione != "":
            self.descr = descrizione
            self.data_ac = data_acquisto
            self.quantita = quantita
            self.pr_uni = prezzo_unitario
            self.data_man = data_manutenzione

    def popola_lista_attrezzi(self):
        return self.objMetodi.popola_lista(self.lista_attrezzi)

    def recupera_attrezzi_salvati(self, percorso):
        self.lista_attrezzi.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_attrezzi)

    def aggiungi_attrezzo(self, attrezzo, percorso):
        self.lista_attrezzi.append([attrezzo.descr, attrezzo.data_ac, attrezzo.quantita, attrezzo.pr_uni, attrezzo.data_man])
        self.objMetodi.scrivi_su_file(percorso, self.lista_attrezzi)

    def scrivi_lista_attrezzi(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_attrezzi)

    def rimuovi_attrezzo(self, riga, percorso):
        self.lista_attrezzi.remove(self.lista_attrezzi[riga])
        self.scrivi_lista_attrezzi(percorso)

