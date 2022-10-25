from Cliente.Model.Cliente import Cliente
from Metodi.Metodi import Metodi


class ControllerCliente(object):
    percorso = "./Cliente/Data/ListaClienti.txt"
    objMetodi = Metodi()

    def __init__(self):
        self.model = Cliente()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente, self.percorso)

    def salva_modifiche_cliente(self, cliente):
        self.model.salva_modifiche_cliente(cliente, self.percorso)

    def recupera_clienti_salvati(self):
        self.model.recupera_clienti_salvati(self.percorso)

    def popola_lista_clienti(self):
        return self.model.popola_lista_clienti()

    def controlla_unicita(self, codice_fiscale):
        return self.model.controlla_unicita(codice_fiscale)

    def get_cliente_from_id(self, username):
        return self.model.get_cliente_from_id(username)

    def get_cliente_autenticazione(self, id):
        return self.model.get_cliente_autenticazione(id)

    def rimuovi_vecchio_cliente(self, username):
        self.model.rimuovi_cliente(username, self.percorso)

    def elimina_cliente_conferma(self, username):
        if self.objMetodi.show_popup_question("Sei sicuro di voler eliminare il cliente?"):
            self.model.rimuovi_cliente(username, self.percorso)

    def get_psw_cliente(self):
        return self.model.get_psw_cliente()

    def set_psw_cliente(self, cliente, nuova_password):
        self.model.set_psw_cliente(cliente, nuova_password, self.percorso)

    def reset_psw_cliente(self, nome):
        self.model.reset_psw_cliente(nome, self.percorso)

    def get_lista_id_clienti(self):
        return self.model.get_lista_id_clienti()


