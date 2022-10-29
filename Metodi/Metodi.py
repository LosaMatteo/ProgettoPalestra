import pickle
from PyQt5.QtWidgets import QMessageBox
import os
from os import listdir
from os.path import isfile, join


class Metodi(object):

    @staticmethod
    def popola_lista(lista):
        if len(lista) > 0:
            f = []
            for x in lista:
                f.append(x)
            return f

    @staticmethod
    def popola_lista_id(lista):
        if len(lista) > 0:
            f = []
            for x in lista:
                f.append(x.nome + " " + x.cognome)
            return f


    @staticmethod
    def get_lista_id(lista):
        vett = []
        for elem in lista:
            vett.append(elem.nome + elem.cognome)
        return vett

    @staticmethod
    def recupera_salvataggio(path, lista):
        if os.path.exists(path) and os.path.getsize(path) != 0:
            with(open(path, "rb")) as openfile:
                while True:
                    try:
                        lista.append(pickle.load(openfile))
                    except EOFError:
                        break

    @staticmethod
    def aggiungi_alla_lista(obj, lista):
        lista.append(obj)

    @staticmethod
    def rimuovi_dalla_lista(strdaeliminare, lista):
        for x in lista:
            if x.nome + " " + x.cognome == strdaeliminare:
                lista.remove(x)
                return

    @staticmethod
    def scrivi_su_file(path, lista):
        filehandler = open(path, 'wb')
        for x in lista:
            pickle.dump(x, filehandler)

    @staticmethod
    def get_oggetto_from_id_spazio(id, lista):
        for x in lista:
            if x.nome + " " + x.cognome == id:
                return x

    @staticmethod
    def get_oggetto_from_id(id, lista):
        for x in lista:
            if x.nome + x.cognome == id:
                return x

    @staticmethod
    def get_password(list):
        credenziali = dict()
        for dati in list:
            credenziali[dati.nome + dati.cognome] = dati.password
        return credenziali

    @staticmethod
    def reset_password(username, lista):
        for x in lista:
            if x.nome + " " + x.cognome == username:
                x.password = "1"
                return

    @staticmethod
    def rimuovi_file(percorso):
        os.remove(percorso)

    @staticmethod
    def get_id(username):
        indirizzo = ""
        str = username.split(" ")
        for elem in str:
            indirizzo += elem
        return indirizzo

    def show_popup_ok(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    def show_popup_exception(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Retry)
        self.msg.show()

    @staticmethod
    def get_lista_files(percorso):
        listafiles = [f for f in listdir(percorso) if isfile(join(percorso, f))]
        return listafiles

    def show_popup_question(self, str):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Atheneo Fitness")
        self.msg.setText(str)
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.setDefaultButton(QMessageBox.No)
        risposta = self.msg.exec_()
        if risposta == QMessageBox.Yes:
            return True
        elif risposta == QMessageBox.No:
            return False
