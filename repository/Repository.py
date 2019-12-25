from Film import Film
from Card import Card
from Rezervare import Rezervare
import copy
class Repository:
    def __init__(self, filme, carduri, rezervari):
        self.filmDB = filme
        self.cardDB = carduri
        self.rezDB = rezervari
        self.filme = self.importFilme(self.filmDB)
        self.carduri = self.importCarduri(self.cardDB)
        self.rezervari = self.importRezervari(self.rezDB)
    
    def saveFilme(self):
        """
        Salveaza starea curenta a filmelor
        """
        file = open(self.filmDB, "w")
        for film in self.filme:
            line = str(film.getID()) + " " + film.getTitlu() + " " + str(film.getAn()) + " " + str(film.getPret())
            for ora in film.getProgram():
                line = line + " " + ora
            line += "\n"
            file.write(line)
    
    def saveCarduri(self):
        """
        Salveaza starea curenta a cardurilor
        """
        file = open(self.cardDB, "w")
        for card in self.carduri:
            line = str(card.getID()) + " " + card.getNume() + " " + card.getPrenume() + " " + str(card.getCNP()) + " " + card.getDataNastere() + " " + card.getDataInregistrare() + " " + str(card.getPuncte())
            line += "\n"
            file.write(line)
    
    def saveRezervari(self):
        """
        Salveaza starea curenta a rezervarilor
        """
        file = open(self.rezDB, "w")
        for rez in self.rezervari:
            line = str(rez.getID()) + " " + str(rez.getIDF()) + " " + str(rez.getIDC()) + " " + rez.getData() + " " + rez.getOra()
            line += "\n"
            file.write(line)

    def importFilme(self, filmDB):
        """
        Importeaza toate filmele
        """
        try:
            file = open(filmDB, "r")
        except:
            file = open(filmDB, "w")
            file.write("")
            return []
        lista = []
        for line in file:
            line = line.strip("\n").split(" ")
            program = []
            for cont in range(4, len(line)):
                program.append(line[cont])
            try:
                film = Film(int(line[0]), line[1], int(line[2]), float(line[3]), program)
                if film.valid():
                    lista.append(film)
            except:
                pass
        print(lista)
        return lista
    
    def importCarduri(self, cardDB):
        """
        Importeaza toate cardurile
        """
        try:
            file = open(cardDB, "r")
        except:
            file = open(cardDB, "w")
            file.write("")
            return []
        lista = []
        for line in file:
            line = line.strip("\n").split(" ")
            try:
                card = Card(int(line[0]), line[1], line[2], int(line[3]), line[4], line[5], int(line[6]))
                if card.valid() == True:
                    lista.append(card)
            except:
                pass
        return lista
    
    def importRezervari(self, rezDB):
        """
        Importeaza toate rezervarile
        """
        try:
            file = open(rezDB, "r")
        except:
            file = open(rezDB, "w")
            file.write("")
            return []
        lista = []
        for line in file:
            line = line.strip("\n").split(" ")
            try:
                rez = Rezervare(int(line[0]), int(line[1]), int(line[2]), line[3], line[4])
                if rez.valid():
                    lista.append(rez)
            except:
                pass
        return lista
    
    def getFilme(self):
        """
        Returneaza toate filmele
        """
        return copy.deepcopy(self.filme)
    
    def getRezervari(self):
        """
        Returneaza toate rezervarile
        """
        return copy.deepcopy(self.rezervari)
    
    def getCarduri(self):
        """
        Returneaza toate cardurile
        """
        return copy.deepcopy(self.carduri)
    
    def setFilme(self, filme):
        """
        Seteaza lista de filme cu una data
        Date intrare: filme - lista de filme
        """
        self.filme = filme
        self.saveFilme()
    
    def setRezervari(self, rezervari):
        """
        Seteaza lista de rezervari cu una data
        Date intrare: rezervari - lista de rezervari
        """
        self.rezervari = rezervari
        self.saveRezervari()
    
    def setCarduri(self, carduri):
        """
        Seteaza lista de carduri cu una data
        Date intrare: carduri - lista de carduri
        """
        self.carduri = carduri
        self.saveCarduri()