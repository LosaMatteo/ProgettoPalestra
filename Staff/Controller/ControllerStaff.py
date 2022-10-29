from Staff.Model.Staff import Staff
from Metodi.Metodi import Metodi


class ControllerStaff(object):
    percorso = "./Staff/Data/ListaStaff.txt"
    objMetodi = Metodi()

    def __init__(self):
        self.model = Staff()

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente, self.percorso)

    def popola_lista_staff(self):
        return self.model.popola_lista_staff()

    def recupera_dipendenti_salvati(self):
        self.model.recupera_dipendenti_salvati(self.percorso)

    def get_dipendente(self, username):
        return self.model.get_dipendente_from_id(username)

    def get_dipendente_autenticazione(self, id):
        return self.model.get_dipendente_autenticazione(id)

    def rimuovi_dipendente(self, username):
        self.model.rimuovi_dipendente(username, self.percorso)

    def reset_psw_dipendente(self, username):
        self.model.reset_psw_staff(username, self.percorso)

    def set_psw_dipendente(self, dipendente, nuova_password):
        self.model.set_psw_dipendente(dipendente, nuova_password, self.percorso)

    def controlla_unicita(self, codice_fiscale):
        return self.model.controlla_unicita(codice_fiscale)

    def get_lista_id_staff(self):
        return self.model.get_lista_id_staff()

    def get_psw_staff(self):
        return self.model.get_psw_staff()


