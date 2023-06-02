import player as pl

# need to include total number of houses and hotels 
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
        self.whole_set = False
        self.one_house = one_house
        self.two_houses = two_houses
        self.three_houses = three_houses
        self.four_houses = four_houses
        self.hotel = hotel
        self.num_houses = 0

    def change_ownership(self, player):
        self.owner = player
        if not self.unowned:
            self.unowned = False


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

    Pennsylvania_RR = Board(None, 'RR', 200, 50)
    Virginia.next = Pennsylvania_RR

    St_James = Board(None, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
    Pennsylvania_RR.next = St_James

    Community_Chest_Two = Board(None, "Special")
    St_James.next = Community_Chest_Two

    Tennessee = Board(None, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
    Community_Chest_Two.next = Tennessee

    New_York = Board(None, 'Orange', 200, 16, 100, 80, 220, 600, 800, 1000)
    Tennessee.next = New_York

    Free_Parking = Board(None, 'Special')
    New_York.next = Free_Parking

    Kentucky = Board(None, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
    Free_Parking.next = Kentucky

    Chance_Two = Board(None, 'Special')
    Kentucky.next = Chance_Two

    Indiana = Board(None, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
    Chance_Two.next = Indiana

    Illinois = Board(None, 'Red', 240, 20, 150, 100, 300, 750, 925, 1100)
    Indiana.next = Illinois

    B_and_O = Board(None, 'RR", 200, 50')
    Illinois.next = B_and_O

    Atlantic = Board(None, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
    B_and_O.next = Atlantic

    Ventnor = Board(None, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
    Atlantic.next = Ventnor

    Water_Works = Board(None, "Utilites", 150)
    Ventnor.next = Water_Works

    Marvin_Gardens = Board(None, 'Yellow', 280, 24, 150, 120, 360, 850, 1025, 1200)
    Water_Works.next = Marvin_Gardens

    Go_To_Jail = Board(None, 'Special')
    Marvin_Gardens.next = Go_To_Jail

    Pacific = Board(None, 'Green', 300, 26, 200, 52, 130, 390, 900, 1100, 1275)
    Go_To_Jail.next = Pacific

    North_Carolina = Board(None, 'Green', 300, 26, 200, 52, 130, 390, 900, 1100, 1275)
    Pacific.next = North_Carolina

    Community_Chest_Three = Board(None, 'Special')
    North_Carolina.next = Community_Chest_Three

    Pennsylvania = Board(None, 'Green', 320, 28, 200, 150, 450, 1000, 1200, 1400)
    Community_Chest_Two.next = Pennsylvania

    Short_Line = Board(None, 'RR', 200, 50)
    Pennsylvania.next = Short_Line

    Chance_Three = Board(None, 'Special')
    Short_Line.next = Chance_Three

    Park_Place = Board(None, "Dark Blue", 350, 35, 200, 175, 500, 1100, 1300, 1500)
    Chance_Three.next = Park_Place

    Luxury_Tax = Board(None, 'Special')
    Park_Place.next = Luxury_Tax

    Boardwalk = Board(Go, 'Dark Blue', 400, 50, 200, 200, 600, 1400, 1700, 2000)
    Luxury_Tax.next = Boardwalk





