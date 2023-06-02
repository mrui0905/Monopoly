import board as bd

class Player:
    def __init__(self):
        self.location = bd.go
        self.money = 1500
        self.properties = set()
        self.jail_card = 0
        self.imprisoned = False
        self.imprisoned_count = 0
        self.rr = 0

    def pay_to(self, payee, amount):
        if amount > self.money:
            return False
        
        self.money -= amount
        payee.money += amount
        return True
    
    def go_to_jail(self):
        self.location = bd.Jail
        self.imprisoned = True
        return

    def buy(self, property):
        self.money -= property.cost
        self.properties.add(property)
        property.owner = self
        if property.set == 'RR':
            self.rr += 1
        return

    def bankrupt(self, debtor='Bank'):
        if debtor == 'Bank':
            for property in self.properties:
                property.owner = None
                property.unowned = True
                property.mortaged = False
                property.whole_set = False
                property.num_houses = 0
        else:
            for property in self.properties:
                property.owner = debtor
                property.whole_set = False
                property.num_houses = 0
                # update whole_set attribute
            debtor.jail_card += self.jail_card
            debtor.money += self.money

        self.location = None
        self.money = 0
        self.properties = set()
        self.jail_card = 0
        self.imprisoned = False
        self.imprisoned_count = 0
        self.rr = 0
        return


    def debt(self, amount):
        not_monopoly = set()
        is_monopoly = set()

        for property in self.properties:
            if property.whole_set:
                is_monopoly.add(property)
            else:
                not_monopoly.add(property)
        
        lst_not_monopoly = sorted(not_monopoly, key = lambda x : x.cost)
        lst_is_monopoly = sorted(is_monopoly, key = lambda x : (x.num_houses, x.cost))

        i, j = 0, 0
        while self.money < amount:
            if i < len(lst_not_monopoly):
                lst_not_monopoly[i].mortaged = True
                self.money += lst_not_monopoly[i].cost // 2
            elif j < len(lst_is_monopoly):
                lst_is_monopoly[j].mortaged = True
                self.money += lst_is_monopoly[j].cost // 2
        
        #liquidate houses and hotels as well
        
        return self.money > amount






    
        