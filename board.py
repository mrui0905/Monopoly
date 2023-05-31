import player as pl

class Board:
    def __init__(self, next, set, cost, rent, cost_of_house, one_house, two_houses, three_houses, four_houses, hotel):
        self.cost = cost
        self.next = next
        self.set = set
        self.owner = None
        self.unowned = True
        self.mortaged = False
        self.rent = rent
        self.cost_of_house = cost_of_house
        self.monopoly = False
        self.one_house = one_house
        self.two_houses = two_houses
        self.three_houses = three_houses
        self.four_houses = four_houses
        self.hotel = hotel

    def change_ownership(self, player):
        self.owner = player
        if not self.unowned:
            self.unowned = False

    def morgated(self):
        self.mortaged = True
    
    def un_mortaged(self):
        self.mortage = False

    def monopoly(self):
        self.monopoly = True

    def monopoly_break(self):
        self.monopoly = False
        

def create_board():
    Go = Board(None, 'Special')

    Mediterranean = Board(None, 'Brown', 60, 2, 50, 10, 30, 90, 160, 250)
    Go.next = Mediterranean

    Community_Chest_One = Board(None, 'Special')
    Mediterranean.next = Community_Chest_One

    Baltic = Board(None, 'Brown', 60, 4, 50, 8, 20, 60, 60, 180, 320, 450)
    Community_Chest_One.next = Baltic

    Income_Tax = Board(None, 'Special')
    Baltic.next = Income_Tax

    Reading = Board(None, 'RR', 200, 50)
    Income_Tax.next = Reading

    Oriental = Board(None, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
    Reading.next = Oriental

    Chance_One = Board(None, 'Special')
    Oriental.next = Chance_One

    Vermont = Board(None, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
    Chance_One.next = Vermont

    Connecticut = Board(None, 'Light Blue', 120, 8, 50, 40, 100, 300, 450, 600)
    Vermont.next = Connecticut

    Jail = Board(None, 'Special')
    Connecticut.next = Jail

    St_Charles = Board(None, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
    Jail.next = St_Charles

    Electric_Company = Board(None, 'Utility', 150)
    St_Charles.next = Electric_Company

    States = Board(None, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
    Electric_Company.next = States

    Virginia = Board(None, 'Purple', 160, 12, 100, 60, 180, 500, 700, 900)
    States.next = Virginia

    Pennsylvania = Board(None, 'RR', 200, 50)
    Virginia.next = Pennsylvania

    St_James = Board(None, 'Orange', 180, 14, 150, 70, 200, 550, 750, 950)
    Pennsylvania.next = St_James

    Community_Chest_Two = Board(None, "Special")
    St_James.next = Community_Chest_Two


