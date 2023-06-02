import player as pl
import board as bd
import random

class Game:
    def __init__(self):
        num = self.input_num_players()
        self.player_count = num
        self.players_alive = num

        self.players = set()
        self.dead_players = set()
        self.turn_order = []

        player_one = pl.Player()
        player_two = pl.Player()
        self.players.add(player_one)
        self.players.add(player_two)
        self.turn_order.append(player_one)
        self.turn_order.append(player_two)

        if num > 2:
            player_three = pl.Player()
            self.players.add(player_three)
            self.turn_order.append(player_three)
        if num > 3:
            player_four = pl.Player()
            self.players.add(player_four)
            self.turn_order.append(player_four)

    def input_num_players(self):
        num = input('Enter the number of players (2-4)')
        while type(num) != int or num < 2 or num > 4:
            num = input('Invalid Input! Please re-enter the number of players (2-4)')
        return num

        
    def dice_roll(self, reroll_count):
        a = random.randint(0, 6)
        b = random.randint(0, 6)
        sum = a + b
        double = False

        if a == b:
            double = True
            if reroll_count == 2:
                sum = -1
        
        return sum, double
    
    def determine_order_of_play(self):
        max = 0
        first_player_index = 0

        for player in range(4):
            val, _ = self.dice_roll(0)
            if val > max:
                max = val
                first_player_index = player

        return first_player_index
    

print('Welcome to Monopoly!')

game = Game()

turn = game.determine_order_of_play

while game.players_alive > 1:
    curr_player = game.turn_order[turn]

    if curr_player in game.dead_players:
        turn += 1
        turn = turn % game.player_count
        continue

    roll_count = 0
    roll, double = game.dice_roll(0)
    if roll == -1:
        curr_player.go_to_jail()
        double = False
        # build properties
        continue

    if curr_player.imprisoned:
        if not double:
            if curr_player.jail_card > 0:
                curr_player.jail_card -= 1
            else:
                if curr_player.money > 50:
                    curr_player.money -= 50
                else:
                    if curr_player.imprisoned_count == 2:
                        if not curr_player.debt(): 
                            game.dead_players.add(curr_player)
                            double = False
                            curr_player.bankrupt()
                        curr_player.money -= 50
                    else:
                        curr_player.imprisoned_count += 1
                        continue
        curr_player.imprisoned = False
        curr_player.imprisoned_count = 0

    

    for _ in range(roll):
        curr_player.location = curr_player.location.next
        if curr_player.location == bd.Go:
            curr_player += 200

    #check for mortage
    if curr_player.location.set == 'Special':
        if curr_player.location == bd.Go or curr_player.location == bd.Free_Parking or (curr_player.location == bd.Jail and not curr_player.imprisoned):
            continue
        if curr_player.location == bd.Community_Chest_One or curr_player.location == bd.Community_Chest_Two or curr_player.location == bd.Community_Chest_Three:
            #community_chest()
            pass
        if curr_player.location == bd.Chance_One or curr_player.location == bd.Chance_Two or curr_player.location == bd.Chance_Three:
            #chance()
            pass
        if curr_player.location == bd.Income_Tax:
            if curr_player.money < 200:
                # debt
                pass
            curr_player.money -= 200
        if curr_player.location == bd.Luxury_Tax:
            if curr_player.money < 100:
                # debt
                pass
            curr_player.money -= 100
    elif not curr_player.location.owner:
        if curr_player.money >= curr_player.location.cost:
            curr_player.buy(curr_player.location) # check for monopoly
    else:
        if curr_player.location.set == 'Utilites':
            if curr_player.location.whole_set:
                rent = roll * 10
            else:
                rent = roll * 4
        elif curr_player.location.set == 'RR':
            rent = curr_player.rr * curr_player.location.rent
        elif curr_player.location.whole_set:
            if curr_player.location.num_houses == 0:
                rent = curr_player.location.rent * 2
            elif curr_player.location.num_houses == 1:
                rent = curr_player.location.one_house
            elif curr_player.location.num_houses == 2:
                rent = curr_player.location.two_houses
            elif curr_player.location.num_houses == 3:
                rent = curr_player.location.three_houses
            elif curr_player.location.num_houses == 4:
                rent = curr_player.location.four_houses
            else:
                rent = curr_player.location.hotel
        else:
            rent = curr_player.location.rent
        if not curr_player.pay_to(curr_player.location.owner, rent):
            # debts
            pass
    






    
    # build properties

    if not double:
        turn += 1
    turn = turn % game.player_count




    


