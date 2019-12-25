import datetime

class Service:
    def __init__(self, repo):
        self.repository = repo
    
    def filterFilme(self, filterOption):
        """
        Returneaza lista de filme ce contine cuvantul cheie filterOption in id, titlu, an, pret sau program
        Date intrare: filterOption - string
        Date iesire: result - lista de filme
        """
        filme = self.repository.getFilme()
        result = []
        for film in filme:
            try:
                if str(film.getID()) == filterOption or filterOption in film.getTitlu() or filterOption == str(film.getAn()) or filterOption == str(film.getPret()) or filterOption in film.getProgram():
                    result.append(film)
            except:
                pass
        return result
    
    def filterClienti(self, filterOption):
        """
        Returneaza lista de clienti ce contine cuvantul cheie filterOption in id, nume, prenume, cnp, data nastere, data inscriere, puncte
        Date intrare: filterOption - string
        Date iesire: result - lista de clienti
        """
        carduri = self.repository.getCarduri()
        result = []
        for card in carduri:
            try:
                if filterOption == str(card.getID()) or filterOption in card.getNume() or filterOption in card.getPrenume() or filterOption == str(card.getCNP()) or filterOption == card.getDataNastere() or filterOption == card.getDataInregistare() or filterOption == str(card.getPuncte()):
                    result.append(card)
            except:
                pass
        return result
    
    def filterFilmeInterval(self, inceput, sfarsit):
        """
        Returneaza lista de filme ce sunt difuzate intr-un interval orar dat
        Date intrare: inceput - string de forma hh:mm, sfarsit - string de forma hh:mm
        Date iesire: result - lista de filme din intervalul [inceput, sfarsit]
        """
        filme = self.repository.getFilme()
        result = []
        inceputora, inceputmin = inceput.split(":")
        sfarsitora, sfarsitmin = sfarsit.split(":")
        for film in filme:
            adaugat = False
            for ora in film.getProgram():
                ora, minut = ora.split(":")
                if adaugat == False:
                    if int(inceputora) < int(ora) and int(ora) < int(sfarsitora):
                        adaugat = True
                        result.append(film)
                    if int(inceputora) == int(ora) and int(inceputmin) <= int(minut):
                        if int(ora) < int(sfarsitora):
                            adaugat = True
                            result.append(film)
                        elif int(ora) == int(sfarsitora) and int(minut) <= int(sfarsitmin):
                            adaugat = True
                            result.append(film)
        return result

    def filmeDescrescator(self):
        """
        Returneaza lista de filme ordonate descrescator dupa numarul de rezervari
        Date iesire: result - lista de filme
        """
        filme = self.repository.getFilme()
        rezervari = self.repository.getRezervari()
        idFilme = {}
        for film in filme:
            if film.getID() not in idFilme:
                idFilme[film.getID()] = 0
        for rezervare in rezervari:
            if rezervare.getIDF() in idFilme:
                idFilme[rezervare.getIDF()]+= 1
        aparitii = idFilme.values()
        aparitii = sorted(idFilme, reverse = True, key=idFilme.get)
        result = []
        for idF in aparitii:
            for film in filme:
                if film.getID() == idF:
                    result.append(film)
                    break
        return result

    def carduriDescrescator(self):
        """
        Returneaza lista de carduri ordonata descrescator dupa punctaj
        Date iesire: result - lista de carduri
        """
        carduri = self.repository.getCarduri()
        result = sorted(carduri, key=lambda x: x.getPuncte(), reverse=True)
        return result
    
    def removeRezervariInterval(self, inceput, sfarsit):
        """
        Sterge toate rezervarile dintr-un interval dat
        Date intrare: inceput - string de forma dd.mm.yyyy, sfarsit - string de forma dd.mm.yyyy
        Date iesire: True daca s-a sters minim o rezervare, False altfel
        """
        rezervari = self.repository.getRezervari()
        inceput = datetime.datetime.strptime(inceput, '%d.%m.%Y')
        sfarsit = datetime.datetime.strptime(sfarsit, '%d.%m.%Y')
        result = []
        nr = 0
        for rez in rezervari:
            data = datetime.datetime.strptime(rez.getData(), '%d.%m.%Y')
            if not (inceput < data and data < sfarsit):
                result.append(rez)
            else:
                nr += 1
        self.repository.setRezervari(result)
        if nr > 0:
            return True
        return False
    
    def addPointsInterval(self, inceput, sfarsit, puncte):
        """
        Adauga un numar de puncte dat la toti clientii ce s-au nascut intr-un interval dat
        Date intrare: inceput - string de forma dd.mm.yyyy, sfarsit - string de forma dd.mm.yyyy, puncte - float
        Date iesire: True daca s-au adaugat puncte la vreun client, False altfel
        """
        carduri = self.repository.getCarduri()
        inceput = datetime.datetime.strptime(inceput, '%d.%m.%Y')
        sfarsit = datetime.datetime.strptime(sfarsit, '%d.%m.%Y')
        result = []
        nr = 0
        for card in carduri:
            nastere = datetime.datetime.strptime(card.getDataNastere(), '%d.%m.%Y')
            if inceput <= nastere and nastere <= sfarsit:
                nr += 1
                card.setPuncte(card.getPuncte() + puncte)
            result.append(card)
        self.repository.setCarduri(result)
        if nr > 0:
            return True
        return False
    
    def getFilmUniqueID(self):
        """
        Returneaza un id unic pentru filme
        Date iesire: idf - int
        """
        filme = self.repository.getFilme()
        idf = 1
        existing = True
        while existing:
            existing = False
            for film in filme:
                if idf == film.getID():
                    existing = True
                    idf += 1
        return idf
    
    def adaugareFilm(self, film):
        """
        Adauga un film in baza de date
        Date intrare: film - de tip Film
        """
        filme = self.repository.getFilme()
        filme.append(film)
        self.repository.setFilme(filme)
        return True
    
    def existingFilmID(self, idf):
        """
        Verifica daca un id dat este atribuit unui film
        Date intrare: idf - int
        Date iesire: True daca idf este id-ul unui film, False altfel
        """
        filme = self.repository.getFilme()
        for film in filme:
            if idf == film.getID():
                return True
        return False
    
    def modificareFilm(self, film):
        """
        Modifica filmul curent cu un film dat cu acelasi id
        Date intrare: film - de tip Film
        Date iesire: True daca s-a modificat vreun film, False altfel
        """
        filme = self.repository.getFilme()
        nr = 0
        for it in range(0, len(filme)):
            if filme[it].getID() == film.getID():
                nr += 1
                filme[it] = film
        self.repository.setFilme(filme)
        if nr > 0:
            return True
        return False
    
    def stergereFilm(self, idf):
        """
        Sterge filmul cu id-ul idf
        Date intrare: idf - int
        Date iesire: True daca s-a sters filmul, False altfel
        """
        filme = self.repository.getFilme()
        result = []
        nr = 0
        for film in filme:
            if film.getID() != idf:
                result.append(film)
            else:
                nr += 1
        self.repository.setFilme(result)
        if nr > 0:
            return True
        return False
    
    def getCardUniqueID(self):
        """
        Returneaza un id pentru card unic
        Date iesire: id - int
        """
        carduri = self.repository.getCarduri()
        idc = 1
        existing = True
        while existing:
            existing = False
            for card in carduri:
                if idc == card.getID():
                    existing = True
                    idc += 1
        return idc
    
    def existingCNP(self, cnp):
        """
        Verifica daca cnp-ul dat exista deja
        Date iesire: True daca cnp-ul se regaseste in baza de date, False altfel
        """
        carduri = self.repository.getCarduri()
        for card in carduri:
            if card.getCNP() == cnp:
                return True
        return False

    def adaugareCard(self, card):
        """
        Adauga un card dat la baza de date
        Date intrare: card - de tip Card
        """
        carduri = self.repository.getCarduri()
        carduri.append(card)
        self.repository.setCarduri(carduri)
        return True
    
    def existingCardID(self, idc):
        """
        Verifica daca idc este un id de card existent
        Date intrare: idc - int
        Date iesire: True daca idc este existent, False altfel
        """
        carduri = self.repository.getCarduri()
        for card in carduri:
            if idc == card.getID():
                return True
        return False
    
    def modificareCard(self, card):
        """
        Modifica un card cu un alt card dat cu acelasi id
        Date intrare: card - de tip Card
        Date iesire: True daca s-a modificat vreun card, False altfel
        """
        carduri = self.repository.getCarduri()
        nr = 0
        for it in range(0, len(carduri)):
            if carduri[it].getID() == card.getID():
                carduri[it] = card
                nr += 1
        self.repository.setCarduri(carduri)
        if nr > 0:
            return True
        return False
    
    def stergereCard(self, idc):
        """
        Sterge card-ul cu id-ul idc
        Date intrare: idc - int
        Date iesire: True daca s-a sters vreun card, False altfel
        """
        carduri = self.repository.getCarduri()
        result = []
        nr = 0
        for card in carduri:
            if card.getID() != idc:
                result.append(card)
            else:
                nr += 1
        self.repository.setCarduri(result)
        if nr > 0:
            return True
        return False
    
    def getRezUniqueID(self):
        """
        Returneaza un id unic pentru o rezervare
        Date iesire: id - int
        """
        rezervari = self.repository.getRezervari()
        idr = 1
        existing = True
        while existing:
            existing = False
            for rez in rezervari:
                if idr == rez.getID():
                    existing = True
                    idr += 1
        return idr
    
    def getFilmByID(self, idf):
        """
        Returneaza filmul cu id-ul idf
        Date intrare: idf - int
        Date iesire: film - de tip Film
        """
        filme = self.repository.getFilme()
        for film in filme:
            if film.getID() == idf:
                return film

    def adaugarePuncte(self, idc, puncte):
        """
        Adauga un numar de puncte dat clientului cu id-ul idc
        Date intrare: idc - int, puncte - float
        """
        carduri = self.repository.getCarduri()
        result = []
        for card in carduri:
            if card.getID() == idc:
                card.setPuncte(card.getPuncte() + puncte)
            result.append(card)
        self.repository.setCarduri(result)
        return True

    def adaugareRez(self, rez):
        """
        Adauga o rezervare in baza de date
        Date intrare: rez - de tip Rezervare
        """
        rezervari = self.repository.getRezervari()
        rezervari.append(rez)
        self.repository.setRezervari(rezervari)
        pret = self.getFilmByID(rez.getIDF()).getPret()
        puncte = pret*0.1
        self.adaugarePuncte(rez.getIDC(), puncte)
        return True
    
    def existingRezID(self, idr):
        """
        Verifica daca id-ul idr este un id exestent de Rezervare
        Date intrare: idr - int
        Date iesire: True daca idr exista, False altfel
        """
        rezervari = self.repository.getRezervari()
        for rez in rezervari:
            if idr == rez.getID():
                return True
        return False
    
    def modificareRez(self, rez):
        """
        Modifica doua rezervari cu acelasi id, unde una din rezervari este data
        Date intrare: rez - de tip Rezervare
        Date iesire: True daca s-a modificat vreo rezervare, False altfel
        """
        rezervari = self.repository.getRezervari()
        nr = 0
        for it in range(0, len(rezervari)):
            if rezervari[it].getID() == rez.getID():
                rezervari[it] = rez
                nr += 1
        self.repository.setRezervari(rezervari)
        if nr > 0:
            return True
        return False
    
    def stergereRez(self, idr):
        """
        Sterge rezervarea cu id-ul idr
        Date intrare: idr - int
        Date iesire: True daca s-a sters vreo rezervare, False altfel
        """
        rezervari = self.repository.getRezervari()
        result = []
        nr = 0
        for rez in rezervari:
            if rez.getID() != idr:
                result.append(rez)
            else:
                nr += 1
        self.repository.setRezervari(result)
        if nr > 0:
            return True
        return False
    
    def existingHourMovie(self, idf, ora):
        """
        Verifica daca ora data exista in filmul cu id-ul idf
        Date intrare: idf - int, ora - string de forma hh:mm
        Date iesire: True daca ora data este in programul filmului, False altfel
        """
        filme = self.repository.getFilme()
        for film in filme:
            if film.getID() == idf:
                if ora in film.getProgram():
                    return True
                else:
                    return False
        return False