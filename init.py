import player as pl
import board as bd
import chance
import community_chest
import random

class Game:
    # Initializees game
    def __init__(self):
        self.player_count = self.input_num_players() # Number of players
        self.players_alive = self.player_count # Number of players alive, initially set to self.player_count, game ends with self.players_alive == 1

        self.players = set() # set of alive players
        self.dead_players = set() # set of dead players
        self.turn_order = [] # order of play

        self.mode = self.input_player_logic()

        self.hotels = 0 # total number of built hotels, max is 12
        self.houses = 0 # total number of built houses, max is 32
        self.total_turns = 0 # total number of played turns, used to terminate perpetutual games

        #Itialilize Chance and Community Chest
        self.ch = chance.Chance()
        self.cc = community_chest.Community_Chest()

        # Initalizes all 40 properties
        self.Go = bd.Board(None, 'Special')

        self.Mediterranean = bd.Board(None, 'Brown', 60, 2, 50, 10, 30, 90, 160, 250)
        self.Go.next = self.Mediterranean

        self.Community_Chest_One = bd.Board(None, 'Special')
        self.Mediterranean.next = self.Community_Chest_One

        self.Baltic = bd.Board(None, 'Brown', 60, 4, 50, 8, 20, 60, 60, 180, 320, 450)
        self.Community_Chest_One.next = self.Baltic

        self.Income_Tax = bd.Board(None, 'Special')
        self.Baltic.next = self.Income_Tax

        self.Reading = bd.Board(None, 'RR', 200, 50)
        self.Income_Tax.next = self.Reading

        self.Oriental = bd.Board(None, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
        self.Reading.next = self.Oriental

        self.Chance_One = bd.Board(None, 'Special')
        self.Oriental.next = self.Chance_One

        self.Vermont = bd.Board(None, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
        self.Chance_One.next = self.Vermont

        self.Connecticut = bd.Board(None, 'Light Blue', 120, 8, 50, 40, 100, 300, 450, 600)
        self.Vermont.next = self.Connecticut

        self.Jail = bd.Board(None, 'Special')
        self.Connecticut.next = self.Jail

        self.St_Charles = bd.Board(None, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
        self.Jail.next = self.St_Charles

        self.Electric_Company = bd.Board(None, 'Utility', 150)
        self.St_Charles.next = self.Electric_Company

        self.States = bd.Board(None, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
        self.Electric_Company.next = self.States

        self.Virginia = bd.Board(None, 'Purple', 160, 12, 100, 60, 180, 500, 700, 900)
        self.States.next = self.Virginia

        self.Pennsylvania_RR = bd.Board(None, 'RR', 200, 50)
        self.Virginia.next = self.Pennsylvania_RR

        self.St_James = bd.Board(None, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
        self.Pennsylvania_RR.next = self.St_James

        self.Community_Chest_Two = bd.Board(None, "Special")
        self.St_James.next = self.Community_Chest_Two

        self.Tennessee = bd.Board(None, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
        self.Community_Chest_Two.next = self.Tennessee

        self.New_York = bd.Board(None, 'Orange', 200, 16, 100, 80, 220, 600, 800, 1000)
        self.Tennessee.next = self.New_York

        self.Free_Parking = bd.Board(None, 'Special')
        self.New_York.next = self.Free_Parking

        self.Kentucky = bd.Board(None, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
        self.Free_Parking.next = self.Kentucky

        self.Chance_Two = bd.Board(None, 'Special')
        self.Kentucky.next = self.Chance_Two

        self.Indiana = bd.Board(None, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
        self.Chance_Two.next = self.Indiana

        self.Illinois = bd.Board(None, 'Red', 240, 20, 150, 100, 300, 750, 925, 1100)
        self.Indiana.next = self.Illinois

        self.B_and_O = bd.Board(None, 'RR", 200, 50')
        self.Illinois.next = self.B_and_O

        self.Atlantic = bd.Board(None, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
        self.B_and_O.next = self.Atlantic

        self.Ventnor = bd.Board(None, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
        self.Atlantic.next = self.Ventnor

        self.Water_Works = bd.Board(None, "Utilites", 150)
        self.Ventnor.next = self.Water_Works

        self.Marvin_Gardens = bd.Board(None, 'Yellow', 280, 24, 150, 120, 360, 850, 1025, 1200)
        self.Water_Works.next = self.Marvin_Gardens

        self.Go_To_Jail = bd.Board(None, 'Special')
        self.Marvin_Gardens.next = self.Go_To_Jail

        self.Pacific = bd.Board(None, 'Green', 300, 26, 200, 52, 130, 390, 900, 1100, 1275)
        self.Go_To_Jail.next = self.Pacific

        self.North_Carolina = bd.Board(None, 'Green', 300, 26, 200, 52, 130, 390, 900, 1100, 1275)
        self.Pacific.next = self.North_Carolina

        self.Community_Chest_Three = bd.Board(None, 'Special')
        self.North_Carolina.next = self.Community_Chest_Three

        self.Pennsylvania = bd.Board(None, 'Green', 320, 28, 200, 150, 450, 1000, 1200, 1400)
        self.Community_Chest_Two.next = self.Pennsylvania

        self.Short_Line = bd.Board(None, 'RR', 200, 50)
        self.Pennsylvania.next = self.Short_Line

        self.Chance_Three = bd.Board(None, 'Special')
        self.Short_Line.next = self.Chance_Three

        self.Park_Place = bd.Board(None, "Dark Blue", 350, 35, 200, 175, 500, 1100, 1300, 1500)
        self.Chance_Three.next = self.Park_Place

        self.Luxury_Tax = bd.Board(None, 'Special')
        self.Park_Place.next = self.Luxury_Tax

        self.Boardwalk = bd.Board(self.Go, 'Dark Blue', 400, 50, 200, 200, 600, 1400, 1700, 2000)
        self.Luxury_Tax.next = self.Boardwalk

        # Initalizes players
        player_one = pl.Player(self.Go, 1) # initializes first player
        player_two = pl.Player(self.Go, 2) # initializes second player
        self.players.add(player_one)
        self.players.add(player_two)
        self.turn_order.append(player_one)
        self.turn_order.append(player_two)

        if self.player_count > 2:
            player_three = pl.Player(self.Go, 3) # initializes third player
            self.players.add(player_three)
            self.turn_order.append(player_three)
        if self.player_count > 3:
            player_four = pl.Player(self.Go, 4) # initializes fourth player
            self.players.add(player_four)
            self.turn_order.append(player_four)


    # Prompts for number of players
    def input_num_players(self):
        num = input('Enter the number of players (2-4)')
        # Retries until user inputs valid number (2, 3, or 4)
        while type(num) != int or num < 2 or num > 4:
            num = input('Invalid Input! Please re-enter the number of players (2-4)')
        return num
    
    # Prompts for player logic
    def input_player_logic(self):
        possible = {0:'CPU Simulation'}
        print('Possible Modes are:')
        for k,v in possible:
            print('Select', k, 'for', v, 'mode')
        mode = input('Select a player mode: ')
        # Retries until user inputs valid mode
        while mode not in possible:
            mode = input('Invalid Input! Please re-enter the player mode')

        return mode


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
    
    def collect_from_all(self, player, amount):
        for p in self.players:
            if player is p:
                continue
            if not p.pay_to(player, amount):
                if not p.debt(50): 
                    self.dies(p, player)
                    continue
                p.pay_to(player, amount)

    def pay_to_bank(self, player, amount):
        if player.money < amount:
            if not player.debt(amount): 
                self.dies(player)
        if player not in self.dead_players:
            player.money -= amount
            return True
        return False 
    
    def community_chest(self, player):
        card = self.cc.draw()

        if card == 0:
            player.jail.card += 1
        if card == 1:
            player.location = self.Go
            player.money += 200
        if card == 2:
            player.money += 200
        if card == 3:
            self.pay_to_bank(player, 50)
        if card == 4:
            self.money += 50
        if card == 5:
            player.go_to_jail(self.jail)
        if card == 6:
            self.collect_from_all(player, 50)
        if card == 7:
            player.money += 100
        if card == 8:
            player.money += 20
        if card == 9:
            self.collect_from_all(player, 10)
        if card == 10:
            self.money += 100
        if card == 11:
            self.pay_to_bank(player, 50)
        if card == 12:
            self.pay_to_bank(player, 50)
        if card == 13:
            self.money += 25
        if card == 14:
            houses, hotels = 0, 0
            for property in player.properties:
                houses += property.num_houses
                if property.num_houses == 5:
                    houses -= 1
                    hotels += 1
            self.pay_to_bank(player, 40*houses + 115 * hotels)
        if card == 15:
            self.money += 10
        if card == 16:
            self.money += 100

        if player in self.dead_players or player.imprisoned:
            return False
        return True

    def chance(self, player):
        card = self.ch.draw()

        if card == 0:
            player.jail.card += 1
        if card == 1:
            player.location = self.Go
            player.money += 200
        if card == 2:
            while player.location != self.Illinois:
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if not self.land_on_location(player, self):
                return False
        if card == 3:
            while player.location != self.St_Charles:
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if not self.land_on_location(player, self):
                return False
        if card == 4:
            while player.location.set != 'Utility':
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if player.location.unowned:
                if player.money >= player.location.cost:
                    player.buy(player.location)
                    player.update_whole_set()

            else:
                rent = 10 * (random.randint(1,6) + random.randint(1,6))
                if not player.pay_to(player.location.owner, rent):
                    if not player.debt(rent): 
                        self.dies(player, player.location.owner)
                        return False
                    player.pay_to(player.location.owner, rent)
        if card == 5:
            while player.location.set != 'RR':
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if player.location.unowned:
                if player.money >= player.location.cost:
                    player.buy(player.location)
                    player.update_whole_set()

            else:
                rent = player.location.owner.rr * player.location.rent * 2
                if not player.pay_to(player.location.owner, rent):
                    if not player.debt(rent): 
                        self.dies(player, player.location.owner)
                        return False
                    player.pay_to(player.location.owner, rent)
        if card == 6:
            player.money += 50
        if card == 7:
            for _ in range(37):
                player.location = player.location.next

            if not self.land_on_location(player, self):
                return False
        if card == 8:
            player.go_to_jail(self.jail)
        if card == 9:
            houses, hotels = 0, 0
            for property in player.properties:
                houses += property.num_houses
                if property.num_houses == 5:
                    houses -= 1
                    hotels += 1
            self.pay_to_bank(player, 25*houses + 100 * hotels)
        if card == 10:
            while player.location != self.Reading:
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if not self.land_on_location(player, self):
                return False
        if card == 11:
            while player.location != self.Boardwalk:
                player.location = player.location.next

                if player.location is self.Go:
                    player.money += 200

            if not self.land_on_location(player, self):
                return False
        if card == 12:
            self.pay_to_bank(player, 50*(self.players_alive -1))
            for p in self.players:
                if player is p:
                    continue
                player.money += 50
        if card == 13:
            self.money += 150
        
        if player in self.dead_players or player.imprisoned:
            return False
        return True
    
    def end_turn(self):
        pass

    def land_on_location(self, player, game, roll=0):
    # 'player' lands on a location that is not ownable
        if player.location.set == 'Special':
            # player lands on Go, Free Parking, or Jail
            if player.location is game.Go or player.location is game.Free_Parking or player.location is game.Jail:
                pass
            # player lands on a Community Chest
            elif player.location is game.Community_Chest_One or player.location is game.Community_Chest_Two or player.location is game.Community_Chest_Three:
                if not game.community_chest(player):
                    return False
            # player lands on a Chance
            elif player.location is game.Chance_One or player.location is game.Chance_Two or player.location is game.Chance_Three:
                if not game.chance(player):
                    return False
            # player lands on Income Tax
            elif player.location is game.Income_Tax:
                if not game.pay_to_bank(player, 200):
                    return False
            # player lands on Luxury Tax
            elif player.location is game.Luxury_Tax:
                if not game.pay_to_bank(player, 100):
                    return False
            # player lands on Go To Jail
            else:
                player.go_to_jail()
                return False
        # 'player' lands on unowned property
        elif not player.location.owner:
            if player.money >= player.location.cost:
                player.buy(player.location)
                player.update_whole_set()
        # 'player' lands on an owned proprety
        else:
            # 'player' pays no rent if the property is mortaged
            if player.location.mortaged:
                pass
            # 'player' lands on a Utiliy
            elif player.location.set == 'Utilites':
                if player.location.whole_set:
                    rent = roll * 10
                else:
                    rent = roll * 4
            # 'player' lands on a Railroad
            elif player.location.set == 'RR':
                rent = player.location.owner.rr * player.location.rent
            # 'player' lands on a monopoly
            elif player.location.whole_set:
                if player.location.num_houses == 0:
                    rent = player.location.rent * 2
                elif player.location.num_houses == 1:
                    rent = player.location.one_house
                elif player.location.num_houses == 2:
                    rent = player.location.two_houses
                elif player.location.num_houses == 3:
                    rent = player.location.three_houses
                elif player.location.num_houses == 4:
                    rent = player.location.four_houses
                else:
                    rent = player.location.hotel
            # 'player' lands on an owned property that is not a monopoly
            else:
                rent = player.location.rent
            if not player.pay_to(player.location.owner, rent):
                if not player.debt(rent): 
                    game.dies(player, player.location.owner)
                    return False
                player.pay_to(player.location.owner, rent)

        return True
    

def main():
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
                curr_player.go_to_jail(game.jail)
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
                if curr_player.location == game.Go: # 'curr_player' receives $200 for passing go
                    curr_player += 200

            if not game.land_on_location(curr_player, game, roll):
                break
        
        # 'curr_player'' now has opporuinity to build unmortage properties and build houses/hotels
        if curr_player in game.players:
            game.end_turn(curr_player)

        # turn count is not updated for next player
        turn += 1
        turn = turn % game.player_count
        game.total_turns += 1

    winner = list(game.players)[0]
    print('Winner is Player', winner.number)
    print('Total number of turns: ', game.total_turns)
    return winner.number
    




            


