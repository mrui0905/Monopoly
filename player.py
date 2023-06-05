import board as bd

class Player:
    # Initializes every player
    def __init__(self):
        self.location = bd.go
        self.money = 1500
        self.properties = set()
        self.jail_card = 0
        self.imprisoned = False
        self.imprisoned_count = 0
        self.rr = 0

    # 'self' pays 'payee' 'amount' number of dollars. Returns True if transaction goes through, returns False if insufficient funds
    def pay_to(self, payee, amount):
        if amount > self.money:
            return False
        
        self.money -= amount
        payee.money += amount
        return True
    
    # Sends 'self' to jail
    def go_to_jail(self):
        self.location = bd.Jail
        self.imprisoned = True
        return

    # 'self' buys property. Assumes sufficient funds
    def buy(self, property):
        self.money -= property.cost
        self.properties.add(property)
        property.owner = self

        self.update_whole_set() # updates monopolies 'self' owns
        
        if property.set == 'RR':
            self.rr += 1
        return

    # Updates all the properties owned by 'self' to ensure all monopolies are accounted for
    def update_whole_set(self):
        master_list = {'Brown':2, 'Light Blue':3, 'Purple':3, 'Orange':3, 'Red':3, 'Yellow':3, 'Green':3, 'Dark Blue':2}
        player_list = {set:0 for set in master_list}

        # counts how many of every set 'self' has
        for property in self.properties:
            if property.set == 'RR':
                continue
            player_list[property.set] += 1

        for set in player_list:
            # if 'set' is a monopoly
            if player_list[set] == master_list[set]:
                for property in self.properties:
                    if property.set == set:
                        property.whole_set = True
            # if 'set' is not a monopoly
            else:
                for property in self.properties:
                    if property.set == set:
                        property.whole_set = False
        
        return


    # Declare 'self' bankrupt. Liquidates all assets and returns to bank or to debtor. Does NOT remove player from the game.
    def bankrupt(self, debtor='Bank'):
        # If 'self' is bankrupt by bank
        if debtor == 'Bank':
            for property in self.properties:
                property.owner = None
                property.unowned = True
                property.mortaged = False
                property.whole_set = False
                property.num_houses = 0
        # If 'self' is bankrip by another player, 'debtor'
        else:
            for property in self.properties:
                property.owner = debtor
                property.whole_set = False
                property.num_houses = 0
            debtor.update_whole_set() #updates debtor's monopolies to include new monopolies
            debtor.jail_card += self.jail_card
            debtor.money += self.money

        self.location = None
        self.money = 0
        self.properties.clear()
        self.jail_card = 0
        self.imprisoned = False
        self.imprisoned_count = 0
        self.rr = 0
        return


    # 'self' liqudates assets until 'self' has enough money to pay 'amount'
    def debt(self, amount):
        not_monopoly = set() # creates set of properities not in a monopoly (will include railroads)
        is_monopoly = set() # creates set of properties in a monopoly

        total_sets = ['Brown', 'Light Blue', 'Purple', 'Orange', 'Red', 'Yellow', 'Green', 'Dark Blue']

        for property in self.properties:
            if property.whole_set:
                is_monopoly.add(property)
            else:
                not_monopoly.add(property)
        
        lst_not_monopoly = sorted(not_monopoly, key = lambda x : x.cost) # list of non-monopoly properties sorted by cheapest to most expensive cost
        # list of lists of monopoly properties grouped by set. Every inner list is sorted by number of houses (largest first) then cost. Inner lists are then sorted by largest number of houses
        lst_is_monopoly = [sorted([property for property in is_monopoly if property.set == set], key = lambda x:(-x.houses, x.cost)) for set in total_sets]
        lst_is_monopoly.sort(key = lambda x:x[0].houses)

        i, j = 0, 0 #pointer that will traverse 'not_monopoly' and 'is_monopoly'

        while self.money < amount:
            # Non-monopoly assets are liquidated first
            if i < len(lst_not_monopoly):
                lst_not_monopoly[i].mortaged = True
                self.money += lst_not_monopoly[i].cost // 2
                i += 1
            elif j < len(lst_is_monopoly):
            # Monopoly assets are liquidated set by set, from most houses to least house until all properties are mortaged
                for k in range(lst_is_monopoly[j][0].houses + 1):
                    for property in lst_is_monopoly[j]:
                        if self.money > amount:
                            break
                        if property.num_houses > 0:
                            property.num_houses -=1
                            self.money += property.cost_of_house // 2
                        elif not property.mortaged:
                            property.mortaged = True
                            self.money += property.cost // 2
            else:
                break

        return self.money > amount






    
        