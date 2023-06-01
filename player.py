import board as bd

class Player:
    def __init__(self):
        self.location = bd.go
        self.money = 1500
        self.properties = set()
        self.jail_card = 0

    def pay_to(self, payee, amount):
        if amount > self.money:
            return False
        
        self.money -= amount
        payee.money += amount
        return True
    
        