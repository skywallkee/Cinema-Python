class Film:
    def __init__(self, idf, titlu, an, pret, program):
        self.id = idf
        self.titlu = titlu
        self.an = an
        self.pret = pret
        self.program = program

    def setID(self, idf):
        """
        Seteaza id-ul filmului cu idf
        Date intrare: idf - int
        """
        self.id = idf
    
    def setTitlu(self, titlu):
        """
        Seteaza titlul-ul filmului cu titlu
        Date intrare: titlu - string
        """
        self.titlu = titlu
    
    def setAn(self, an):
        """
        Seteaza an-ul filmului cu an
        Date intrare: an - string de forma dd.mm.yyyy
        """
        self.an = an
    
    def setPret(self, pret):
        """
        Seteaza pret-ul filmului cu pret
        Date intrare: pret - int
        """
        self.pret = pret

    def setProgram(self, program):
        """
        Seteaza program-ul filmului cu program
        Date intrare: program - lista de string-uri de forma hh:mm
        """
        self.program = program
    
    def getID(self):
        """
        Returneaza id-ul filmului
        Date iesire: id - int
        """
        return self.id
    
    def getTitlu(self):
        """
        Returneaza titlul filmului
        Date iesire: titlu - string
        """
        return self.titlu
    
    def getAn(self):
        """
        Returneaza an-ul filmului
        Date iesire: an - string de forma dd.mm.yyyy
        """
        return self.an
    
    def getPret(self):
        """
        Returneaza pret-ul filmului
        Date iesire: pret - int
        """
        return self.pret

    def getProgram(self):
        """
        Returneaza program-ul filmului
        Date iesire: program - lista de stringuri de forma hh:mm
        """
        return self.program
    
    def validProgram(self, program):
        """
        Verifica daca programul dat are ore de forma hh:mm
        Date intrare: program - lista de ore
        Date iesire: True daca are forma corecta, False altfel
        """
        try:
            for ora in program:
                ora, minute = ora.split(":")
            ora = int(ora)
            minute = int(minute)
            if ora >= 0 and ora <= 24 and minute >= 0 and minute < 60:
                return True
        except:
            return False
        return False

    def valid(self):
        """
        Verifica daca filmul este valid
        Date iesire: True daca e valid, False altfel
        """
        try:
            if self.getPret() > 0 and self.getAn() > 0 and self.validProgram(self.getProgram()):
                return True
        except:
            return False
        return False
