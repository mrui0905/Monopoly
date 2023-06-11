import player as pl

class Board:
    # Initializes each location on the monopoly board
    def __init__(self, next, number, set, cost=0, rent=0, cost_of_house=0, one_house=0, two_houses=0, three_houses=0, four_houses=0, hotel=0):
        self.cost = cost # cost to buy location
        self.number = number # Number of property
        self.next = next # following location
        self.set = set # set each location belongs too: 'Special', 'Utility', 'Brown', 'Light Blue', 'Purple', 'Orange', 'Red', 'Yellow', 'Green', 'Dark Blue', 'RR'
        self.owner = None # player that owns location. None if self.unowned is True
        self.unowned = True # True if location is owned by a player
        self.mortaged = False # True if location is mortaged
        self.rent = rent # cost of rent
        self.cost_of_house = cost_of_house # cost to build one house/hotel
        self.whole_set = False # True if player owns a monopoly of a set. Does not apply to 'Special' and 'RR'
        self.one_house = one_house # cost of rent with one house
        self.two_houses = two_houses # cost of rent with two houses
        self.three_houses = three_houses # cost of rent with three houses
        self.four_houses = four_houses # cost of rent with four houses
        self.hotel = hotel # cost of rent with a hotel
        self.num_houses = 0 # number of houses/hotels. 5 if hotel

    def __lt__(self, other):
        return self
    
    def __gt__(self, other):
        return self

    # Transfer ownership of a property to player
    def change_ownership(self, player):
        self.owner = player
        if not self.unowned:
            self.unowned = False