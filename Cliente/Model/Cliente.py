from Metodi.Metodi import Metodi
from Abbonamento.Model.Abbonamento import Abbonamento


class Cliente(object):
    lista_clienti = []
    objAbbonamento = Abbonamento()
    objMetodi = Metodi()

    def __init__(self, nome="", cognome="", sesso="", data_nascita="", luogo_nascita="", codice_fiscale="",
                 password="", abbonamento="", altezza="", peso="", eta="", ):
        if nome != "" or cognome != "":
            self.nome = nome
            self.cognome = cognome
            self.sesso = sesso
            self.data_nascita = data_nascita
            self.luogo_nascita = luogo_nascita
            self.codice_fiscale = codice_fiscale
            self.password = password
            self.objAbbonamento = abbonamento
            self.altezza = altezza
            self.peso = peso
            self.eta = eta

    def popola_lista_clienti(self):
        return self.objMetodi.popola_lista_id(self.lista_clienti)

    def recupera_clienti_salvati(self, percorso):
        self.lista_clienti.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_clienti)

    def aggiungi_cliente(self, cliente, percorso):
        nuovo_abbonamento = Abbonamento()
        self.set_abbonamento_cliente(cliente, nuovo_abbonamento.get_abbonamento())
        self.objMetodi.aggiungi_alla_lista(cliente, self.lista_clienti)
        self.scrivi_lista_clienti(percorso)

    def salva_modifiche_cliente(self, cliente, percorso):
        self.objMetodi.aggiungi_alla_lista(cliente, self.lista_clienti)
        self.scrivi_lista_clienti(percorso)

    def rimuovi_cliente(self, stringa_da_eliminare, percorso):
        self.objMetodi.rimuovi_dalla_lista(stringa_da_eliminare, self.lista_clienti)
        self.scrivi_lista_clienti(percorso)

    def scrivi_lista_clienti(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_clienti)

    def elimina_cliente(self, stringa_da_eliminare, percorso):
        self.objMetodi.rimuovi_dalla_lista(stringa_da_eliminare, self.lista_clienti)
        self.scrivi_lista_clienti(percorso)

    def set_abbonamento_cliente(self, cliente, abbonamento):
        cliente.abbonamento = abbonamento

    def get_cliente_from_id(self, id):
        return self.objMetodi.get_oggetto_from_id_spazio(id, self.lista_clienti)

    def get_cliente_autenticazione(self, id):
        return self.objMetodi.get_oggetto_from_id(id, self.lista_clienti)

    def get_psw_cliente(self):
        return self.objMetodi.get_password(self.lista_clienti)

    def set_psw_cliente(self, cliente, nuova_password, percorso):
        cliente.password = nuova_password
        self.scrivi_lista_clienti(percorso)

    def reset_psw_cliente(self, name, percorso):
        self.objMetodi.reset_password(name, self.lista_clienti)
        self.scrivi_lista_clienti(percorso)

    def get_lista_id_clienti(self):
        return self.objMetodi.get_lista(self.lista_clienti)

    def get_sesso_cliente(self, cliente):
        return cliente.sesso

    def get_eta(self, cliente):
        return cliente.eta

    def get_peso(self, cliente):
        return cliente.peso

    def get_altezza(self, cliente):
        return cliente.altezza

    def controlla_unicita(self, codice_fiscale):
        for elem in self.lista_clienti:
            if elem.codice_fiscale.lower() == codice_fiscale.lower():
                return False
        return True