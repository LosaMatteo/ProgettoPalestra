from Metodi.Metodi import Metodi


class Orario(object):
    lista_turni = []
    objMetodi = Metodi()

    def __init__(self, data="", fascia_oraria="", username="", paga="", tipo=""):
        if data != "":
            self.data = data
            self.fascia_oraria = fascia_oraria
            self.username = username
            self.paga = paga
            self.tipo = tipo

    def recupera_orario_turni(self, percorso):
        self.lista_turni.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_turni)

    def aggiungi_orario(self, orario, percorso):
        if self.confronta_turno(orario):
            return False
        else:
            self.objMetodi.aggiungi_alla_lista(orario, self.lista_turni)
            self.scrivi_lista_orari(percorso)
            return True

    def scrivi_lista_orari(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_turni)

    def get_lista_turni_data(self, data, username):
        lista_turni = []
        for elem in self.lista_turni:
            if data == elem.data and username == self.objMetodi.get_id(elem.username):
                lista_turni.append(elem)
        return lista_turni

    def rimuovi_turno_da_lista(self, username, data, tipo, orario, percorso):
        for elem in self.lista_turni:
            if elem.data == data and elem.username == username and elem.tipo == tipo and elem.fascia_oraria == orario:
                self.lista_turni.remove(elem)
        self.scrivi_lista_orari(percorso)

    def rimuovi_orario(self, username, percorso):
        for elem in self.lista_turni:
            if elem.username == username:
                self.lista_turni.remove(elem)
        self.scrivi_lista_orari(percorso)

    def confronta_turno(self, oggetto):
        for elem in self.lista_turni:
            if oggetto.username == elem.username and oggetto.data == elem.data and \
                    oggetto.tipo == elem.tipo and elem.fascia_oraria == oggetto.fascia_oraria:
                return True
        return False
