import board as bd

class Player:
    def __init__(self):
        self.location = bd.go
        self.money = 1500
        self.properties = set()
        self.jail_card = 0
        self.imprisoned = False
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

    def buy(self, property):
        self.money -= property.cost
        self.properties.add(property)
        property.owner = self
        if property.set == 'RR':
            self.rr += 1


    
        