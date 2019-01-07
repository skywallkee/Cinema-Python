from UI import UI
from Service import Service
from Repository import Repository
from Test import Test

if __name__ == "__main__":
    repo = Repository("FilmRepo.txt", "CardRepo.txt", "RezRepo.txt")
    serv = Service(repo)
    ui = UI(serv)
    teste = Test()
    running = True
    while running:
        ui.display()
        option = ui.getOption()
        if option == "0":
            running = False
        elif option == "-1":
            teste.runTests()
        else:
            ui.doOption(option)