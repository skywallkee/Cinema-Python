from Repository import Repository
from Service import Service
from Film import Film
from Card import Card
from Rezervare import Rezervare

class Test:
    def __init__(self):
        repo = Repository("TestFilmRepo.txt", "TestCardRepo.txt", "TestRezRepo.txt")
        serv = Service(repo)
        self.serv = serv
    
    def testeAdaugare(self):
        # Adaugare filme
        filme = self.serv.repository.getFilme()
        lungime = len(filme)
        film = Film(1, "Test1", 2019, 20.5, ["10:20", "20:00"])
        self.serv.adaugareFilm(film)
        filme = self.serv.repository.getFilme()
        assert(lungime < len(filme))
        assert(len(filme) == 1)

        # Adaugare carduri
        carduri = self.serv.repository.getCarduri()
        lungime = len(carduri)
        card = Card(1, "Test1N", "Test1P", 1, "1.1.1999", "1.1.2010", 0)
        self.serv.adaugareCard(card)
        carduri = self.serv.repository.getCarduri()
        assert(lungime < len(carduri))
        assert(len(carduri) == 1)

        # Adaugare rezervari
        rezervari = self.serv.repository.getRezervari()
        lungime = len(rezervari)
        rezervare = Rezervare(1, 1, 1, "1.1.2010", "10:20")
        self.serv.adaugareRez(rezervare)
        rezervare = Rezervare(2, 1, 1, "1.1.1999", "10:20")
        self.serv.adaugareRez(rezervare)
        rezervari = self.serv.repository.getRezervari()
        assert(lungime < len(rezervari))
        assert(len(rezervari) == 2)

    def testeModificare(self):
        # Modificare filme
        film = Film(1, "Test2", 2018, 21, ["11:20"])
        filme = self.serv.repository.getFilme()
        assert(filme[0].getID() == film.getID() and filme[0].getTitlu() != film.getTitlu())
        self.serv.modificareFilm(film)
        filme = self.serv.repository.getFilme()
        assert(filme[0].getID() == film.getID() and filme[0].getTitlu() == film.getTitlu())
        
        # Modificare carduri
        card = Card(1, "Test", "Test", 1, "1.1.1999", "1.1.2010", 10)
        carduri = self.serv.repository.getCarduri()
        assert(carduri[0].getID() == card.getID() and carduri[0].getNume() != card.getNume())
        self.serv.modificareCard(card)
        carduri = self.serv.repository.getCarduri()
        assert(carduri[0].getID() == card.getID() and carduri[0].getNume() == card.getNume())
        
        # Modificare rezervari
        rez = Rezervare(1, 1, 2, "1.1.2010", "10:20")
        rezervari = self.serv.repository.getRezervari()
        assert(rezervari[0].getID() == rez.getID() and rezervari[0].getIDC() != rez.getIDC())
        self.serv.modificareRez(rez)
        rezervari = self.serv.repository.getRezervari()
        assert(rezervari[0].getID() == rez.getID() and rezervari[0].getIDC() == rez.getIDC())

    def testePuncte(self):
        # Verificare puncte adaugate dupa rezervare noua
        carduri = self.serv.repository.getCarduri()
        assert(carduri[0].getPuncte() > 0)

        # Adaugare puncte clienti cu zi de nastere in interval
        punctaj = carduri[0].getPuncte()
        self.serv.addPointsInterval("1.1.1997", "1.1.1998", 10)
        carduri = self.serv.repository.getCarduri()
        assert(carduri[0].getPuncte() == punctaj)
        self.serv.addPointsInterval("1.1.1998", "1.1.2000", 10)
        carduri = self.serv.repository.getCarduri()
        assert(carduri[0].getPuncte() == punctaj + 10)

    def testeStergere(self):
        # Stergere rezervari din interval
        rezervari = self.serv.repository.getRezervari()
        assert(len(rezervari) == 2)
        self.serv.removeRezervariInterval("2.1.2010", "10.4.2100")
        rezervari = self.serv.repository.getRezervari()
        assert(len(rezervari) == 2)
        self.serv.removeRezervariInterval("1.1.2009", "1.1.2011")
        rezervari = self.serv.repository.getRezervari()
        assert(len(rezervari) == 1)

        # Stergere filme
        filme = self.serv.repository.getFilme()
        lungime = len(filme)
        for film in filme:
            self.serv.stergereFilm(film.getID())
        filme = self.serv.repository.getFilme()
        assert(lungime > len(filme))
        assert(len(filme) == 0)
        
        # Stergere carduri
        carduri = self.serv.repository.getCarduri()
        lungime = len(carduri)
        for card in carduri:
            self.serv.stergereCard(card.getID())
        carduri = self.serv.repository.getCarduri()
        assert(lungime > len(carduri))
        assert(len(carduri) == 0)
        
        # Stergere rezervari
        rezervari = self.serv.repository.getRezervari()
        lungime = len(rezervari)
        for rez in rezervari:
            self.serv.stergereRez(rez.getID())
        rezervari = self.serv.repository.getRezervari()
        assert(lungime > len(rezervari))
        assert(len(rezervari) == 0)

    def testeCautare(self):
        # Cautare filme
        filme = self.serv.filterFilme("Test")
        assert(len(filme) == 1)
        filme = self.serv.filterFilme("Asdf")
        assert(len(filme) == 0)
        filme = self.serv.filterFilme("2019")
        assert(len(filme) == 0)
        filme = self.serv.filterFilme("2018")
        assert(len(filme) == 1)

        # Cautare clienti
        clienti = self.serv.filterClienti("Test")
        assert(len(clienti) == 1)
        clienti = self.serv.filterClienti("Aasd")
        assert(len(clienti) == 0)
        clienti = self.serv.filterClienti("1")
        assert(len(clienti) == 1)
        clienti = self.serv.filterClienti("2")
        assert(len(clienti) == 0)

    def testeFiltre(self):
        # Filtru rezervari in interval
        filme = self.serv.filterFilmeInterval("11:00", "12:00")
        assert(len(filme) == 1)
        filme = self.serv.filterFilmeInterval("11:00", "11:20")
        assert(len(filme) == 1)
        filme = self.serv.filterFilmeInterval("11:20", "12:00")
        assert(len(filme) == 1)
        filme = self.serv.filterFilmeInterval("12:00", "22:00")
        assert(len(filme) == 0)

        # Filtru filme descrescator dupa rezervari
        film = Film(2, "Test1", 2019, 20.5, ["10:20", "20:00"])
        self.serv.adaugareFilm(film)
        filme = self.serv.filmeDescrescator()
        assert(filme[0].getID() == 1 and filme[1].getID() == 2)

        # Filtru carduri descrescator dupa puncte
        card = Card(2, "Test1N", "Test1P", 1, "1.1.1999", "1.1.2010", 100)
        self.serv.adaugareCard(card)
        carduri = self.serv.carduriDescrescator()
        assert(carduri[0].getID() == 2 and carduri[1].getID() == 1)

    def runTests(self):
        self.testeAdaugare()
        print("Test adaugare trecut!")
        self.testeModificare()
        print("Test modificare trecut!")
        self.testePuncte()
        print("Test puncte trecut!")
        self.testeCautare()
        print("Test cautare trecut!")
        self.testeFiltre()
        print("Test filtre trecut!")
        self.testeStergere()
        print("Test stergere trecut!")
        input("Apasati ENTER pentru a continua.")