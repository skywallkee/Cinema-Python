from Film import Film
from Card import Card
from Rezervare import Rezervare

class UI:
    def __init__(self, serv):
        self.service = serv
        self.menu = {
            "0": "Iesire",
            "1": "Cautare film",
            "2": "Cautare clienti",
            "3": "Afisare rezervari interval ora",
            "4": "Afisare filme descrescator dupa rezervari",
            "5": "Afisare carduri descrescator dupa puncte",
            "6": "Stergere rezervari din interval zile",
            "7": "Crestere puncte clienti cu zi de nastere in interval",
            "8": "Adaugare Film",
            "9": "Modificare Film",
            "10": "Stergere Film",
            "11": "Adaugare Card",
            "12": "Modificare Card",
            "13": "Stergere Card",
            "14": "Adaugare Rezervare",
            "15": "Modificare Rezervare",
            "16": "Stergere Rezervare"
        }
    
    def clear(self):
        print("\n"*100)

    def display(self):
        self.clear()
        for option in range(0, len(self.menu)):
            option = str(option)
            print(option + ". " + self.menu[option])

    def validOption(self, option):
        if option in self.menu or option == "-1":
            return True
        return False

    def getOption(self):
        option = "Invalid"
        while not self.validOption(option):
            option = input("Alegeti optiunea dorita: ")
        return option
    
    def validOra(self, ora):
        try:
            ora, minute = ora.split(":")
            ora = int(ora)
            minute = int(minute)
            if ora >= 0 and ora <= 23 and minute >= 0 and minute < 60:
                return True
        except:
            return False
        return False
    
    def validData(self, data):
        try:
            zi, luna, an = data.split(".")
            zi = int(zi)
            luna = int(luna)
            an = int(an)
            if zi >= 0 and zi <= 31 and luna >= 0 and luna < 12 and an >= 0:
                return True
        except:
            return False 
    
    def validPoints(self, points):
        try:
            points = int(points)
            if points >= 0:
                return True
        except:
            return False
        return False

    def validAn(self, an):
        try:
            an = int(an)
            if an > 0:
                return True
        except:
            return False
        return False

    def validPret(self, pret):
        try:
            pret = float(pret)
            if pret > 0:
                return True
        except:
            return False
        return False

    def requestFilm(self):
        idf = self.service.getFilmUniqueID()
        titlu = input("Dati titlul filmului: ")
        an = "invalid"
        while not self.validAn(an):
            an = input("Dati anul filmului: ")
        an = int(an)
        pret = "invalid"
        while not self.validPret(pret):
            pret = input("Dati pretul filmului: ")
        pret = float(pret)
        ora = "invalid"
        program = []
        while True:
            ora = input("Dati ora filmului (-1 pentru a opri): ")
            if ora == "-1":
                if len(program) == 0:
                    print("Trebuie sa ruleze filmul la cel putin o ora.")
                else:
                    break
            if self.validOra(ora):
                program.append(ora)
        film = Film(idf, titlu, an, pret, program)
        return film

    def validCNP(self, cnp, unique):
        try:
            cnp = int(cnp)
        except:
            return False
        if unique == True:
            if not self.service.existingCNP(cnp):
                return True
            return False
        else:
            return True

    def requestCard(self, unique):
        idc = self.service.getCardUniqueID()
        nume = input("Dati numele proprietarului: ")
        prenume = input("Dati prenumele proprietarului: ")
        cnp = "invalid"
        while not self.validCNP(cnp, unique):
            cnp = input("Dati cnp-ul proprietarului: ")
        cnp = int(cnp)
        dataNastere = "invalid"
        while not self.validData(dataNastere):
            dataNastere = input("Dati data de nastere a proprietarului: ")
        dataInregistrare = "invalid"
        while not self.validData(dataInregistrare):
            dataInregistrare = input("Dati data de inregistrare a proprietarului: ")
        puncte = 0
        card = Card(idc, nume, prenume, cnp, dataNastere, dataInregistrare, puncte)
        return card
    
    def validIDFilmRequest(self, idf):
        try:
            idf = int(idf)
        except:
            return False
        if self.service.existingFilmID(idf):
            return True
        return False

    def validIDCardRequest(self, idc):
        try:
            idc = int(idc)
        except:
            return False
        if self.service.existingCardID(idc):
            return True
        return False

    def requestRez(self):
        idr = self.service.getRezUniqueID()
        idf = "invalid"
        while not self.validIDFilmRequest(idf):
            idf = input("Dati id-ul filmului: ")
        idf = int(idf)
        idc = "invalid"
        while not self.validIDCardRequest(idc):
            idc = input("Dati id-ul cardului: ")
        idc = int(idc)
        data = "invalid"
        while not self.validData(data):
            data = input("Dati data filmului: ")
        ora = "invalid"
        while not self.validOra(ora):
            ora = input("Dati ora filmului (hh:mm): ")
            if self.validOra(ora):
                if not self.service.existingHourMovie(idf, ora):
                    print("Ora data nu e in program!")
                    ora = "invalid"
        rez = Rezervare(idr, idf, idc, data, ora)
        return rez

    def doOption(self, option):
        if option == "1":
            filterOption = input("Dati cheia pentru filtrare: ")
            results = self.service.filterFilme(filterOption)
            if len(results) == 0:
                print("Nu exista niciun film dupa cheia data.")
            else:
                print("Filmele care contin cheia " + filterOption + " sunt: ")
                for result in results:
                    print(result.getID(), result.getTitlu(), result.getAn(), result.getPret(), result.getProgram())
        elif option == "2":
            filterOption = input("Dati cheia pentru filtrare: ")
            results = self.service.filterClienti(filterOption)
            if len(results) == 0:
                print("Nu exista niciun client dupa cheia data.")
            else:
                print("Clientii care contin cheia " + filterOption + " sunt: ")
                for result in results:
                    print(result.getID(), result.getNume(), result.getPrenume(), result.getCNP(), result.getDataNastere(), result.getDataInregistrare(), result.getPuncte())
        elif option == "3":
            inceput = "invalid"
            sfarsit = "invalid"
            while not self.validOra(inceput):
                inceput = input("Dati ora de inceput interval: ")
            while not self.validOra(sfarsit):
                sfarsit = input("Dati ora sfarsit interval: ")
            results = self.service.filterFilmeInterval(inceput, sfarsit)
            print("Filmele care se deruleaza in intervalul [" + inceput + "; " + sfarsit + "] sunt: ")
            for result in results:
                print(result.getID(), result.getTitlu(), result.getAn(), result.getPret(), result.getProgram())
        elif option == "4":
            results = self.service.filmeDescrescator()
            print("Filme sortate descrescator dupa numarul de rezervari: ")
            for result in results:
                print(result.getID(), result.getTitlu(), result.getAn(), result.getPret(), result.getProgram())
        elif option == "5":
            results = self.service.carduriDescrescator()
            print("Carduri sortate descrescator dupa numarul de puncte: ")
            for result in results:
                print(result.getID(), result.getNume(), result.getPrenume(), result.getCNP(), result.getDataNastere(), result.getDataInregistrare(), result.getPuncte())
        elif option == "6":
            inceput = "invalid"
            sfarsit = "invalid"
            while not self.validData(inceput):
                inceput = input("Dati data de inceput interval: ")
            while not self.validData(sfarsit):
                sfarsit = input("Dati data sfarsit interval: ")
            if self.service.removeRezervariInterval(inceput, sfarsit) == True:
                print("Stergere realizata cu succes.")
            else:
                print("Nu exista rezervari in acel interval.")
        elif option == "7":
            inceput = "invalid"
            sfarsit = "invalid"
            punctaj = "invalid"
            while not self.validData(inceput):
                inceput = input("Dati data de inceput interval: ")
            while not self.validData(sfarsit):
                sfarsit = input("Dati data de sfarsit interval: ")
            while not self.validPoints(punctaj):
                punctaj = input("Dati numarul de puncte adaugate: ")
            if self.service.addPointsInterval(inceput, sfarsit, int(punctaj)) == True:
                print("Adaugare de puncte realizata cu succes.")
            else:
                print("Nu exista clienti cu zi de nastere in acel interval.")
        elif option == "8":
            film = self.requestFilm()
            if self.service.adaugareFilm(film) == True:
                print("Adaugare de film realizata cu succes.")
            else:
                print("Nu s-a putut adauga filmul.")
        elif option == "9":
            idf = "invalid"
            while not self.service.existingFilmID(idf):
                idf = input("Dati id-ul filmului: ")
                try:
                    idf = int(idf)
                except:
                    pass
            film = self.requestFilm()
            film.setID(idf)
            if self.service.modificareFilm(film) == True:
                print("Modificare realizata cu succes.")
            else:
                print("Nu exista filmul cu id-ul dat.")
        elif option == "10":
            idf = "invalid"
            while not self.service.existingFilmID(idf):
                idf = input("Dati id-ul filmului: ")
                try:
                    idf = int(idf)
                except:
                    pass
            if self.service.stergereFilm(idf) == True:
                print("Stergere realizata cu succes.")
            else:
                print("Nu exista filmul cu id-ul dat.")
        elif option == "11":
            uniqueCNP = True
            card = self.requestCard(uniqueCNP)
            if self.service.adaugareCard(card) == True:
                print("Adaugare de card realizata cu succes.")
            else:
                print("Nu s-a putut adauga cardul.")
        elif option == "12":
            idc = "invalid"
            while not self.service.existingCardID(idc):
                idc = input("Dati id-ul cardului: ")
                try:
                    idc = int(idc)
                except:
                    pass
            uniqueCNP = False
            card = self.requestCard(uniqueCNP)
            card.setID(idc)
            if self.service.modificareCard(card) == True:
                print("Modificare realizata cu succes.")
            else:
                print("Nu exista cardul cu id-ul dat.")
        elif option == "13":
            idc = "invalid"
            while not self.service.existingCardID(idc):
                idc = input("Dati id-ul cardului: ")
                try:
                    idc = int(idc)
                except:
                    pass
            if self.service.stergereCard(idc) == True:
                print("Stergere realizata cu succes.")
            else:
                print("Nu exista cardul cu id-ul dat.")
        elif option == "14":
            rez = self.requestRez()
            if self.service.adaugareRez(rez) == True:
                print("Adaugare de rezervare realizata cu succes.")
            else:
                print("Nu s-a putut adauga rezervarea.")
        elif option == "15":
            idr = "invalid"
            while not self.service.existingRezID(idr):
                idr = input("Dati id-ul rezervarii: ")
                try:
                    idr = int(idr)
                except:
                    pass
            rez = self.requestRez()
            rez.setID(idr)
            if self.service.modificareRez(rez) == True:
                print("Modificare realizata cu succes.")
            else:
                print("Nu exista rezervarea cu id-ul dat.")
        elif option == "16":
            idr = "invalid"
            while not self.service.existingRezID(idr):
                idr = input("Dati id-ul rezervarii: ")
                try:
                    idr = int(idr)
                except:
                    pass
            if self.service.stergereRez(idr) == True:
                print("Stergere realizata cu succes.")
            else:
                print("Nu exista rezervarea cu id-ul dat.")

        input("Pentru a continua apasati ENTER.")