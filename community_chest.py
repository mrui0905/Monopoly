import random

class Community_Chest:
    def __init__(self):
        # shuffled order of cards
        self.order = [i for i in range(17)] 
        random.shuffle(self.order)

        self.idx = 0 # next card index
        self.jail = False # True if Get out of Jail Free Card is in possession

    def draw(self):
        # Draws a card
        num = self.order[self.idx]

        self.idx += 1
        self.idx = self.idx % 17
        
        # Draws next card if Get out of Jail card is impossibly drawn
        if num == 0 and self.jail:
            num = self.order[self.idx]

            self.idx += 1
            self.idx = self.idx % 17

        return num

    

        

        
