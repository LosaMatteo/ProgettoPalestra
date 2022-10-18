from Prenotazione.Model.Prenotazione import Prenotazione


class ControllerPrenotazione(object):
    percorso = "./Prenotazione/Data/Prenotazioni.txt"

    def __init__(self):
        self.model = Prenotazione()

    def effettua_prenotazione(self, numero_massimo, prenotazione):
        return self.model.effettua_prenotazione(numero_massimo, prenotazione, self.percorso)

    def recupera_prenotazioni(self):
        self.model.recupera_prenotazioni(self.percorso)

    def rimuovi_prenotazione(self, prenotazione):
        self.model.rimuovi_prenotazione(prenotazione, self.percorso)

    def get_posti_disponibili(self, sala, data, ora):
        return self.model.get_posti_disponibili(sala, data, ora)

    def controlla_apertura(self, data_selezionata, giorni_attivi):
        return self.model.controlla_apertura(data_selezionata, giorni_attivi)

    def pulisci_prenotazioni(self):
        self.model.elimina_vecchie_prenotazioni(self.percorso)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()



