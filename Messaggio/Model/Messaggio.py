from Metodi.Metodi import Metodi
from Cliente.Model.Cliente import Cliente
from Staff.Model.Staff import Staff


class Messaggio(object):
    lista_messaggi = []
    objMetodi = Metodi()
    objCliente = Cliente()
    objStaff = Staff()

    def __init__(self, mittente="", destinatario="", contenuto="", data=""):
        self.mittente = mittente
        self.destinatario = destinatario
        self.contenuto = contenuto
        self.data = data

    def popola_lista_messaggi(self):
        return self.objMetodi.popola_lista_id(self.lista_messaggi)

    def spedisci_messaggio(self, messaggio, percorso):
        if messaggio.contenuto.replace(" ", "") != "":
            self.aggiungi_messaggio(messaggio, percorso)
            return True
        else:
            self.elimina_messaggio(messaggio, percorso)
            return False

    def recupera_messaggi(self, percorso):
        self.lista_messaggi.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_messaggi)

    def aggiungi_messaggio(self, messaggio, percorso):
        self.objMetodi.aggiungi_alla_lista(messaggio, self.lista_messaggi)
        self.scrivi_lista_messaggi(percorso)

    def scrivi_lista_messaggi(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_messaggi)

    def elimina_messaggio(self, messaggio, percorso):
        for x in self.lista_messaggi:
            if x.mittente == messaggio.mittente and x.destinatario == messaggio.destinatario and \
                    x.contenuto == messaggio.contenuto and x.data == messaggio.data:
                self.lista_messaggi.remove(x)
                break
        self.scrivi_lista_messaggi(percorso)

    def get_lista_from_id(self, id):
        lista_nuova = []
        for x in self.lista_messaggi:
            if x.destinatario == id or x.mittente == id:
                lista_nuova.append(x)
        lista_nuova.sort(key=lambda x: x.data, reverse=True) # ordina la lista messaggi in ordine temporale
        return lista_nuova

    def get_lista_clienti(self):
        return self.objCliente.get_lista_id_clienti()

    def get_lista_staff(self):
        return self.objStaff.get_lista_id_staff()

    def notifica_turno(self, mittente, destinatario, messaggio, data, percorso):
        notifica = Messaggio(mittente, destinatario, messaggio, data)
        notifica.aggiungi_messaggio(notifica, percorso)
