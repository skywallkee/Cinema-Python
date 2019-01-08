class Card:
    def __init__(self, idc, nume, prenume, cnp, dataNastere, dataInregistrare, puncte):
        self.id = idc
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp
        self.dataNastere = dataNastere
        self.dataInregistrare = dataInregistrare
        self.puncte = puncte
    
    def setID(self, idc):
        """
        Seteaza id-ul cardului cu idc
        Date intrare: idc - int
        """
        self.id = idc
    
    def setNume(self, nume):
        """
        Seteaza numele proprietarului cu nume
        Date intrare: nume - string
        """
        self.nume = nume

    def setPrenume(self, prenume):
        """
        Seteaza prenumele proprietarului cu prenume
        Date intrare: prenume - string
        """
        self.prenume = prenume

    def setCNP(self, cnp):
        """
        Seteaza cnp-ul proprietarului cu cnp
        Date intrare: cnp - int
        """
        self.cnp = cnp
    
    def setDataNastere(self, data):
        """
        Seteaza data de nastere a proprietarului cu data
        Date intrare: data - string de forma dd.mm.yyyy
        """
        self.dataNastere = data
    
    def setDataInregistrare(self, data):
        """
        Seteaza data de inregistrare a proprietarului cu data
        Date intrare: data - string de forma dd.mm.yyyy
        """
        self.dataInregistrare = data

    def setPuncte(self, puncte):
        """
        Seteaza punctele proprietarului cu o valoare data
        Date intrare: puncte - float
        """
        self.puncte = puncte

    def getID(self):
        """
        Returneaza id-ul cardului
        Date iesire: id - int
        """
        return self.id

    def getNume(self):
        """
        Returneaza numele-ul proprietarului
        Date iesire: nume - string
        """
        return self.nume
    
    def getPrenume(self):
        """
        Returneaza prenumele-ul proprietarului
        Date iesire: prenume - string
        """
        return self.prenume
    
    def getCNP(self):
        """
        Returneaza cnp-ul proprietarului
        Date iesire: cnp - int
        """
        return self.cnp
    
    def getDataNastere(self):
        """
        Returneaza data de nastere a proprietarului
        Date iesire: dataNastere - string de forma dd.mm.yyyy
        """
        return self.dataNastere
    
    def getDataInregistrare(self):
        """
        Returneaza data de inregistrare a proprietarului
        Date iesire: dataNastere - string de forma dd.mm.yyyy
        """
        return self.dataInregistrare
    
    def getPuncte(self):
        """
        Returneaza punctele-ul cardului
        Date iesire: puncte - int
        """
        return self.puncte
    
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
        if self.validData(self.getDataInregistrare()) and self.validData(self.getDataNastere()) and self.getPuncte() >= 0:
            return True
        return False