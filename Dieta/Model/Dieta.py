from Metodi.Metodi import Metodi
from Cliente.Model.Cliente import Cliente


class Dieta(object):
    objMetodi = Metodi()
    lista_info_dieta = []
    objCliente = Cliente()

    def __init__(self, username="", bmi="", peso_ideale="", fabbisogno="", segnalazioni=""):
        if username != "":
            self.username = username
            self.bmi = bmi
            self.peso_ideale = peso_ideale
            self.fabbisogno = fabbisogno
            self.segnalazioni = segnalazioni

    def salva_info_cliente(self, username, altezza, peso, eta):
        self.objCliente = self.objCliente.get_cliente_autenticazione(username)
        self.objCliente.altezza = altezza
        self.objCliente.peso = peso
        self.objCliente.eta = eta

    def recupera_info_diete_salvate(self, percorso):
        self.lista_info_dieta.clear()
        self.objMetodi.recupera_salvataggio(percorso, self.lista_info_dieta)

    def controlla_ridondanza(self, username):
        for elem in self.lista_info_dieta:
            if elem.username == username:
                return True
        return False

    def rimuovi_info_dieta(self, username, percorso):
        for elem in self.lista_info_dieta:
            if elem.username == username:
                self.lista_info_dieta.remove(elem)
        self.scrivi_lista_info(percorso)

    def aggiungi_info_dieta(self, dieta, percorso):
        self.objMetodi.aggiungi_alla_lista(dieta, self.lista_info_dieta)
        self.scrivi_lista_info(percorso)

    def scrivi_lista_info(self, percorso):
        self.objMetodi.scrivi_su_file(percorso, self.lista_info_dieta)

    def popola_lista_diete(self):
        try:
            with open("./Dieta/Data/dieta.txt", "r") as openfile:
                lettura = openfile.read()
            lettura = lettura.split("\n")
            return lettura
        except Exception:
            return 0

    def get_info_dieta(self, username):
        for elem in self.lista_info_dieta:
            if elem.username == username:
                return elem
        return 0

    def rimuovi_dieta_assegnata(self, username, percorso):
        lista_files_dieta = self.objMetodi.get_lista_files(percorso)
        for elem in lista_files_dieta:
            if elem.startswith(username):
                self.objMetodi.rimuovi_file(percorso + elem)

    def get_gender(self, username):
        self.objCliente = self.objCliente.get_cliente_autenticazione(username)
        return self.objCliente.get_sesso_cliente(self.objCliente)

    def get_eta(self, username):
        self.objCliente = self.objCliente.get_cliente_autenticazione(username)
        return self.objCliente.get_eta(self.objCliente)

    def get_peso(self, username):
        self.objCliente = self.objCliente.get_cliente_autenticazione(username)
        return self.objCliente.get_peso(self.objCliente)

    def get_altezza(self, username):
        self.objCliente = self.objCliente.get_cliente_autenticazione(username)
        return self.objCliente.get_altezza(self.objCliente)

    def calcola_BMI(self, altezza, peso):
        bmi = peso / (altezza * altezza)
        return bmi