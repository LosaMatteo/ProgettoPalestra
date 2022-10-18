from Metodi.Metodi import Metodi
from Orario.Model.Orario import Orario


class Staff(object):
    objMetodi = Metodi()
    objOrario = Orario()
    lista_staff = []

    def __init__(self, nome="", cognome="", codice_fiscale="", orario="", mansione="", password=""):
        if nome != "" or cognome != "":
            self.nome = nome
            self.cognome = cognome
            self.codice_fiscale = codice_fiscale
            self.objOrario = orario
            self.mansione = mansione
            self.password = password

    def popola_lista_staff(self):
        return Metodi.popola_lista_id(self.lista_staff)

    def recupera_dipendenti_salvati(self, percorso):
        self.lista_staff.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_staff)

    def aggiungi_dipendente(self, dipendente, percorso):
        self.objMetodi.aggiungi_alla_lista(dipendente, self.lista_staff)
        self.scrivi_lista_staff(percorso)

    def scrivi_lista_staff(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_staff)

    def get_dipendente_from_id(self, id):
        return self.objMetodi.get_oggetto_from_id_spazio(id, self.lista_staff)

    def rimuovi_dipendente(self, username, percorso):
        orario = Orario()
        self.objMetodi.rimuovi_dalla_lista(username, self.lista_staff)
        orario.rimuovi_orario(username, percorso)
        self.scrivi_lista_staff(percorso)

    def reset_psw_staff(self, username, percorso):
        self.objMetodi.reset_password(username, self.lista_staff)
        self.scrivi_lista_staff(percorso)

    def get_psw_staff(self):
        return self.objMetodi.get_password(self.lista_staff)

    def set_psw_dipendente(self, dipendente, nuova_password, percorso):
        dipendente.password = nuova_password
        self.scrivi_lista_staff(percorso)

    def get_dipendente_autenticazione(self, id):
        return self.objMetodi.get_oggetto_from_id(id, self.lista_staff)

    def get_lista_id_staff(self):
        return self.objMetodi.get_lista(self.lista_staff)

    def controlla_unicita(self, codice_fiscale):
        for elem in self.lista_staff:
            if elem.codice_fiscale.lower() == codice_fiscale.lower():
                return False
        return True