class Rezervare:
    def __init__(self, idr, id_film, id_card_client, data, ora):
        self.id = idr
        self.idF = id_film
        self.idC = id_card_client
        self.data = data
        self.ora = ora
    
    def setID(self, idr):
        """
        Seteaza id-ul rezervarii cu idr
        Date intrare: idr - int
        """
        self.id = idr
    
    def setIDF(self, idf):
        """
        Seteaza id-ul filmului cu idf
        Date intrare: idf - int
        """
        self.idF = idf
    
    def setIDC(self, idc):
        """
        Seteaza id-ul cardului cu idc
        Date intrare: idc - int
        """
        self.idC = idc
    
    def setData(self, data):
        """
        Seteaza data rezervarii cu data
        Date intrare: data - string de forma dd.mm.yyyy
        """
        self.data = data
    
    def setOra(self, ora):
        """
        Seteaza ora rezervarii cu ora
        Date intrare: ora - string de forma hh:mm
        """
        self.ora = ora
    
    def getID(self):
        """
        Returneaza id-ul rezervarii
        Date iesire: id - int
        """
        return self.id
    
    def getIDF(self):
        """
        Returneaza id-ul filmului
        Date iesire: idF - int
        """
        return self.idF
    
    def getIDC(self):
        """
        Returneaza id-ul cardului
        Date iesire: idC - int
        """
        return self.idC
    
    def getData(self):
        """
        Returneaza data rezervarii
        Date iesire: data - string de forma dd.mm.yyyy
        """
        return self.data
    
    def getOra(self):
        """
        Returneaza ora rezervarii
        Date iesire: ora - string de forma hh:mm
        """
        return self.ora
    
    def validData(self, data):
        """
        Verifica daca o data data este de forma dd.mm.yyyy
        Date intrare: data - string
        Date iesire: True daca e de forma corecta, False altfel
        """
        try:
            zi, luna, an = data.split(".")
            zi = int(zi)
            luna = int(luna)
            an = int(an)
            if zi >= 0 and zi <= 31 and luna >= 0 and luna < 12 and an >= 0:
                return True
        except:
            return False
    
    def validOra(self, ora):
        """
        Verifica daca o ora data este de forma hh:mm
        Date intrare: ora - string
        Date iesire: True daca e de forma corecta, False altfel
        """
        try:
            ora, minute = ora.split(":")
            ora = int(ora)
            minute = int(minute)
            if ora >= 0 and ora <= 24 and minute >= 0 and minute < 60:
                return True
        except:
            return False

    def valid(self):
        """
        Verifica daca cardul este valid
        Date iesire: True daca e valid, False altfel
        """
        if self.validOra(self.getOra()) and self.validData(self.getData()):
           return True
        return False