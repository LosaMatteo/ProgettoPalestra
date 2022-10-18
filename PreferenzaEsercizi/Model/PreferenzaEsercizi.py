from Metodi.Metodi import Metodi


class PreferenzaEsercizi(object):
    lista_esercizi = []
    objMetodi = Metodi()

    def __init__(self, username="", esercizi=""):
        if username != "":
            self.username = username
            self.esercizi = esercizi

    def recupera_preferenze(self, percorso):
        self.lista_esercizi.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_esercizi)

    def aggiungi_preferenza(self, preferenza, percorso):
        self.aggiorna_preferenze(preferenza.username)
        self.objMetodi.aggiungi_alla_lista(preferenza, self.lista_esercizi)
        self.scrivi_lista_preferenze(percorso)

    def aggiorna_preferenze(self, username):
        for elem in self.lista_esercizi:
            if elem.username == username:
                self.lista_esercizi.remove(elem)

    def scrivi_lista_preferenze(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_esercizi)

    def get_preferenza(self, username):
        for elem in self.lista_esercizi:
            if elem.username == username:
                return elem
        return 0