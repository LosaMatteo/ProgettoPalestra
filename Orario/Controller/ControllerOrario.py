from Orario.Model.Orario import Orario
from datetime import datetime
from Messaggio.Model.Messaggio import Messaggio


class ControllerOrario(object):
    percorso = "./Orario/Data/ListaTurni.txt"
    objMessaggio = Messaggio()

    def __init__(self):
        self.model = Orario()

    def invia_orario(self, orario):
        if self.model.aggiungi_orario(orario, self.percorso):
            self.objMessaggio.notifica_turno("Admin", orario.username.replace(" ", ""),
                                             "Ti è stato assegnato il turno in data "
                                             + orario.data + " di " + orario.tipo + " delle " + orario.fascia_oraria,
                                             datetime.today().strftime('%Y-%m-%d-%H:%M'), "./Messaggio/Data/ListaMessaggi.txt")
            return True
        else:
            return False

    def recupera_turni_salvati(self):
        self.model.recupera_orario_turni(self.percorso)

    def fascia_oraria(self, tipo):
        vett = []
        vett.clear()
        if tipo == "Sala Pesi":
            vett.append("09:30-11:00")
            vett.append("11:00-12:30")
            vett.append("12:30-14:00")
            vett.append("14:00-15:30")
            vett.append("15:30-17:30")
            vett.append("17:00-18:30")
            vett.append("18:30-20:00")
            vett.append("20:00-21:30")
            vett.append("21:30-23:00")
            return vett
        elif tipo == "Zumba":
            vett.append("18:00-19:30")
            vett.append("19:30-21:00")
            return vett
        else:
            vett.append("15:30-17:00")
            vett.append("17:00-18:30")
            return vett

    def controlla_validita_giorno(self, tipo, data):
        if tipo == "Sala Pesi":
            if data == "dom":
                return False
        if tipo == "Zumba":
            if data != "gio" and data != "ven":
                return False
        elif tipo == "Functional":
            if data != "mar" and data != "mer" and data != "ven":
                return False
        return True

    def get_lista_turni_data(self, data, username):
        return self.model.get_lista_turni_data(data, username)

    def presenza_turno(self, username, data):
        for elem in self.get_lista_turni_data(data, username):
            if elem.username == username:
                return True
        return False

    def rimuovi_orario(self, username, data, orario, tipo):
        self.model.rimuovi_turno_da_lista(username, data, tipo, orario, self.percorso)
        self.objMessaggio.notifica_turno("Admin", username.replace(" ", ""), "Il turno in data " +
                                         data + " di " + tipo + " dalle " + orario + " è stato cancellato.",
                                         datetime.today().strftime('%Y-%m-%d-%H:%M'), "./Messaggio/Data/ListaMessaggi.txt")