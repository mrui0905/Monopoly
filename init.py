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
        #send plasyer to jail
        pass

    curr_location = curr_player.location

    for _ in range(roll):
        curr_location = curr_location.next
        if curr_location == bd.Go:
            curr_player += 200

    if curr_location.set == 'Special':
        # case-by-case property
        pass
    elif not curr_location.owner:
        # prompt to buy
        pass
    else:
        #ADD: check for utilites
        owner = curr_location.owner
        if curr_location.whole_set:
            if curr_location.num_houses == 0:
                rent = curr_location.rent * 2
            elif curr_location.num_houses == 1:
                rent = curr_location.one_house
            elif curr_location.num_houses == 2:
                rent = curr_location.two_houses
            elif curr_location.num_houses == 3:
                rent = curr_location.three_houses
            elif curr_location.num_houses == 4:
                rent = curr_location.four_houses
            else:
                rent = curr_location.hotel
        else:
            rent = curr_location.rent
        if not curr_player.pay_to(owner, rent):
            # pay debts
            pass
    






    
    # build properties


    turn += 1
    turn = turn % game.player_count




    


