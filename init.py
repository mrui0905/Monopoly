import player as pl
import board as bd
import random

class Game:
    # Initializees game
    def __init__(self):
        self.player_count = self.input_num_players() # Number of players
        self.players_alive = self.player_count # Number of players alive, initially set to self.player_count, game ends with self.players_alive == 1

        self.players = set() # set of alive players
        self.dead_players = set() # set of dead players
        self.turn_order = [] # order of play

        self.hotels = 0 # total number of built hotels, max is 12
        self.houses = 0 # total number of built houses, max is 32
        self.total_turns = 0 # total number of played turns, used to terminate perpetutual games

        player_one = pl.Player() # initializes first player
        player_two = pl.Player() # initializes second player
        self.players.add(player_one)
        self.players.add(player_two)
        self.turn_order.append(player_one)
        self.turn_order.append(player_two)

        if self.player_count > 2:
            player_three = pl.Player() # initializes third player
            self.players.add(player_three)
            self.turn_order.append(player_three)
        if self.player_count > 3:
            player_four = pl.Player() # initializes fourth player
            self.players.add(player_four)
            self.turn_order.append(player_four)

    # Prompts for number of players
    def input_num_players(self):
        num = input('Enter the number of players (2-4)')
        # Retries until user inputs valid number (2, 3, or 4)
        while type(num) != int or num < 2 or num > 4:
            num = input('Invalid Input! Please re-enter the number of players (2-4)')
        return num

    # Produces sum of two random integers from 1-6. Also returns boolean value 'double' which is True if the two dice values are equal.
    # Returns -1 if third consecutive double, 'self' is then sent to jail
    def dice_roll(self, reroll_count):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        sum = a + b
        double = False

        if a == b:
            double = True
            if reroll_count == 2:
                sum = -1
        
        return sum, double
    
    # In a standard game of monopoly, every player rolls a dice and the highest player starts first. In essence, all players are equally likely
    # to move first, thus this method simply randomly chooses one player to go first.
    def determine_order_of_play(self):
        return random.randint(0,3)
    
    # Removes player from the game and declares bankruptcy
    def dies(self, player, debtor):
        self.players_alive -= 1
        self.players.remove(player)
        self.dead_players.add(player)
        
        player.bankrupt(player, debtor)
        return
    
    def community_chest(self, player):
        pass

    def chance(self, player):
        pass
    
    def end_turn(self):
        pass
    

if __name__ == '__main__':
    print('Welcome to Monopoly!')

    game = Game() # creates game

    turn = game.determine_order_of_play() # determines player that goes first

    while game.players_alive > 1:
        curr_player = game.turn_order[turn]

        # checking if curr_player has been eliminated. If so, game continues onto next player
        if curr_player in game.dead_players: 
            turn += 1
            turn = turn % game.player_count
            continue
        
        # creates list 'rolls' which details the rolls 'curr_player' receives.
        double = True
        rolls = []
        while double and len(rolls) <= 3:
            roll, double = game.dice_roll(0)
            rolls.append(roll)

        for roll in rolls:
            # checks if 'curr_player' received 3 consecutive doubles. If so, 'curr_player' is sent to jail
            if roll == -1:
                curr_player.go_to_jail()
                break
            
            # checks if 'curr_player' begins their turn imprisoned.
            if curr_player.imprisoned:
                if len(rolls) == 1: # first roll is not a double
                    # 'curr_player' will first try to use a Get ouf of Jail Free Card
                    if curr_player.jail_card > 0:
                        curr_player.jail_card -= 1
                    # 'curr_player' will then, if able, pay $50 to leave jail
                    elif curr_player.money > 50:
                            curr_player.money -= 50
                    # if this is the third turn 'curr_player' is imprisoned, they are then forced to liquidate assets and pay $50 to leave jail, or declare bankruptcy
                    elif curr_player.imprisoned_count == 2:
                        if not curr_player.debt(50): # if 'curr_player' is unable to pay the $50
                            game.dies(curr_player)
                            break
                        curr_player.money -= 50
                    # 'curr_player" can not leave prison, but is not forced too either
                    else:
                        curr_player.imprisoned_count += 1
                        break
                curr_player.imprisoned = False
                curr_player.imprisoned_count = 0

            # moves 'curr_player" forward 'roll' locations
            for _ in range(roll):
                curr_player.location = curr_player.location.next
                if curr_player.location == bd.Go: # 'curr_player' receives $200 for passing go
                    curr_player += 200

            # ADD:check for mortage
            # 'curr_player' lands on a location that is not ownable
            if curr_player.location.set == 'Special':
                # curr_player lands on Go, Free Parking, or Jail
                if curr_player.location == bd.Go or curr_player.location == bd.Free_Parking or curr_player.location == bd.Jail:
                    continue
                # curr_player lands on a Community Chest
                elif curr_player.location == bd.Community_Chest_One or curr_player.location == bd.Community_Chest_Two or curr_player.location == bd.Community_Chest_Three:
                    game.community_chest(curr_player)
                    pass
                # curr_player lands on a Chance
                elif curr_player.location == bd.Chance_One or curr_player.location == bd.Chance_Two or curr_player.location == bd.Chance_Three:
                    game.chance(curr_player)
                    pass
                # curr_player lands on Income Tax
                elif curr_player.location == bd.Income_Tax:
                    if curr_player.money < 200:
                        if not curr_player.debt(200): 
                            game.dies(curr_player)
                            break
                    curr_player.money -= 200
                # curr_player lands on Luxury Tax
                elif curr_player.location == bd.Luxury_Tax:
                    if curr_player.money < 100:
                        if not curr_player.debt(100): 
                            game.dies(curr_player)
                            break
                    curr_player.money -= 100
                # curr_player lands on Go To Jail
                else:
                    curr_player.go_to_jail()
                    break
            # 'curr_player' lands on unowned property
            elif not curr_player.location.owner:
                if curr_player.money >= curr_player.location.cost:
                    curr_player.buy(curr_player.location)
                    curr_player.update_whole_set()
            # 'curr_player' lands on an owned proprety
            else:
                # 'curr_player' pays no rent if the property is mortaged
                if curr_player.location.mortaged:
                    continue
                # 'curr_player' lands on a Utiliy
                if curr_player.location.set == 'Utilites':
                    if curr_player.location.whole_set:
                        rent = roll * 10
                    else:
                        rent = roll * 4
                # 'curr_player' lands on a Railroad
                elif curr_player.location.set == 'RR':
                    rent = curr_player.location.owner.rr * curr_player.location.rent
                # 'curr_player' lands on a monopoly
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
                # 'curr_player' lands on an owned property that is not a monopoly
                else:
                    rent = curr_player.location.rent
                if not curr_player.pay_to(curr_player.location.owner, rent):
                    if not curr_player.debt(rent): 
                        game.dies(curr_player, curr_player.location.owner)
                    curr_player.pay_to(curr_player.location.owner, rent)
        
        # 'curr_player'' now has opporuinity to build unmortage properties and build houses/hotels
        game.end_turn(curr_player)

        # turn count is not updated for next player
        turn += 1
        turn = turn % game.player_count
        game.total_turns += 1

    winner = list(game.players)[0]
    print('Winner is: ', winner)
    print('Total number of turns: ', game.total_turns)
    




            


