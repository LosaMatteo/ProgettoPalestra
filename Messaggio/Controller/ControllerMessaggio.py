from Messaggio.Model.Messaggio import Messaggio


class ControllerMessaggio(object):
    percorso = "./Messaggio/Data/ListaMessaggi.txt"

    def __init__(self):
        self.model = Messaggio()

    def spedisci_messaggio(self, messaggio):
        return self.model.spedisci_messaggio(messaggio, self.percorso)

    def recupera_messaggi(self):
        self.model.recupera_messaggi(self.percorso)

    def get_lista_messaggi_from_id(self, id):
        return self.model.get_lista_from_id(id)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def get_lista_staff(self):
        return self.model.get_lista_staff()

    def selezione_destinatario(self, chkClienti, chkStaff):
        if chkClienti or chkStaff:
            return True
        else:
            return False

    def elimina_messaggio(self, messaggio):
        self.model.elimina_messaggio(messaggio, self.percorso)

