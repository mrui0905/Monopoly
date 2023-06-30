import player as pl
import board as bd
import chance
import community_chest
import random
import heapq as hq

name = {
    0:'Go',
    1:'Mediterranean',
    2:'Community Chance 1',
    3:'Baltic',
    4:'Income Tax',
    5:'Reading RR',
    6:'Oriental',
    7:'Chance 1',
    8:'Vermont',
    9:'Connecticut',
    10:'Jail',
    11:'St. Charles',
    12:'Electric Company',
    13:'States',
    14:'Virginia',
    15:'Pennsylvania RR',
    16:'St. James',
    17:'Community Chest 2',
    18:'Tennessee',
    19:'New York',
    20:'Free Parking',
    21:'Kentucky',
    22:'Chance 2',
    23:'Indiana',
    24:'Illinois',
    25:'B & O RR',
    26:'Atlantic',
    27:'Ventnor',
    28:'Water Works',
    29:'Marvin Gardens',
    30:'Go to Jail',
    31:'Pacific',
    32:'North Carolina',
    33:'Community Chest 3',
    34:'Pennsylvania',
    35:'Short Line RR',
    36:'Chance 3',
    37:'Park Place',
    38:'Luxury Tax',
    39:"Boardwalk"
}

class Game:
    # Initializees game
    def __init__(self, game_mode=None, player_modes=None):
        self.property_count = {n:0 for n in range(40)}

        self.player_count =  self.input_num_players(player_modes) # Number of players
        self.players_alive = self.player_count # Number of players alive, initially set to self.player_count, game ends with self.players_alive == 1

        self.players = set() # set of alive players
        self.dead_players = set() # set of dead players
        self.turn_order = [] # order of play

        self.mode = self.input_player_logic(game_mode)

        self.hotels = 0 # total number of built hotels, max is 12
        self.houses = 0 # total number of built houses, max is 32
        self.total_turns = 0 # total number of played turns, used to terminate perpetutual games

        #Itialilize Chance and Community Chest
        self.ch = chance.Chance()
        self.cc = community_chest.Community_Chest()

        # Initalizes all 40 properties
        self.Go = bd.Board(None, 0, 'Special')

        self.Mediterranean = bd.Board(None, 1, 'Brown', 60, 2, 50, 10, 30, 90, 160, 250)
        self.Go.next = self.Mediterranean

        self.Community_Chest_One = bd.Board(None, 2,  'Special')
        self.Mediterranean.next = self.Community_Chest_One

        self.Baltic = bd.Board(None, 3, 'Brown', 60, 4, 50, 20, 60, 180, 320, 450)
        self.Community_Chest_One.next = self.Baltic

        self.Income_Tax = bd.Board(None, 4, 'Special')
        self.Baltic.next = self.Income_Tax

        self.Reading = bd.Board(None, 5, 'RR', 200, 50)
        self.Income_Tax.next = self.Reading

        self.Oriental = bd.Board(None, 6, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
        self.Reading.next = self.Oriental

        self.Chance_One = bd.Board(None, 7, 'Special')
        self.Oriental.next = self.Chance_One

        self.Vermont = bd.Board(None, 8, 'Light Blue', 100, 6, 50, 30, 90, 270, 400, 550)
        self.Chance_One.next = self.Vermont

        self.Connecticut = bd.Board(None, 9, 'Light Blue', 120, 8, 50, 40, 100, 300, 450, 600)
        self.Vermont.next = self.Connecticut

        self.Jail = bd.Board(None, 10, 'Special')
        self.Connecticut.next = self.Jail

        self.St_Charles = bd.Board(None, 11, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
        self.Jail.next = self.St_Charles

        self.Electric_Company = bd.Board(None, 12, 'Utility', 150)
        self.St_Charles.next = self.Electric_Company

        self.States = bd.Board(None, 13, 'Purple', 140, 10, 100, 50, 150, 450, 625, 750)
        self.Electric_Company.next = self.States

        self.Virginia = bd.Board(None, 14, 'Purple', 160, 12, 100, 60, 180, 500, 700, 900)
        self.States.next = self.Virginia

        self.Pennsylvania_RR = bd.Board(None, 15, 'RR', 200, 50)
        self.Virginia.next = self.Pennsylvania_RR

        self.St_James = bd.Board(None, 16, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
        self.Pennsylvania_RR.next = self.St_James

        self.Community_Chest_Two = bd.Board(None, 17, "Special")
        self.St_James.next = self.Community_Chest_Two

        self.Tennessee = bd.Board(None, 18, 'Orange', 180, 14, 100, 70, 200, 550, 750, 950)
        self.Community_Chest_Two.next = self.Tennessee

        self.New_York = bd.Board(None, 19, 'Orange', 200, 16, 100, 80, 220, 600, 800, 1000)
        self.Tennessee.next = self.New_York

        self.Free_Parking = bd.Board(None, 20, 'Special')
        self.New_York.next = self.Free_Parking

        self.Kentucky = bd.Board(None, 21, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
        self.Free_Parking.next = self.Kentucky

        self.Chance_Two = bd.Board(None, 22, 'Special')
        self.Kentucky.next = self.Chance_Two

        self.Indiana = bd.Board(None, 23, 'Red', 220, 18, 150, 90, 250, 700, 875, 1050)
        self.Chance_Two.next = self.Indiana

        self.Illinois = bd.Board(None, 24, 'Red', 240, 20, 150, 100, 300, 750, 925, 1100)
        self.Indiana.next = self.Illinois

        self.B_and_O = bd.Board(None, 25, 'RR', 200, 50)
        self.Illinois.next = self.B_and_O

        self.Atlantic = bd.Board(None, 26, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
        self.B_and_O.next = self.Atlantic

        self.Ventnor = bd.Board(None, 27, 'Yellow', 260, 22, 150, 110, 330, 800, 975, 1150)
        self.Atlantic.next = self.Ventnor

        self.Water_Works = bd.Board(None, 28,  "Utility", 150)
        self.Ventnor.next = self.Water_Works

        self.Marvin_Gardens = bd.Board(None, 29, 'Yellow', 280, 24, 150, 120, 360, 850, 1025, 1200)
        self.Water_Works.next = self.Marvin_Gardens

        self.Go_To_Jail = bd.Board(None, 30, 'Special')
        self.Marvin_Gardens.next = self.Go_To_Jail

        self.Pacific = bd.Board(None, 31, 'Green', 300, 26, 200, 130, 390, 900, 1100, 1275)
        self.Go_To_Jail.next = self.Pacific

        self.North_Carolina = bd.Board(None, 32, 'Green', 300, 26, 200, 130, 390, 900, 1100, 1275)
        self.Pacific.next = self.North_Carolina

        self.Community_Chest_Three = bd.Board(None, 33, 'Special')
        self.North_Carolina.next = self.Community_Chest_Three

        self.Pennsylvania = bd.Board(None, 34, 'Green', 320, 28, 200, 150, 450, 1000, 1200, 1400)
        self.Community_Chest_Three.next = self.Pennsylvania

        self.Short_Line = bd.Board(None, 35, 'RR', 200, 50)
        self.Pennsylvania.next = self.Short_Line

        self.Chance_Three = bd.Board(None, 36, 'Special')
        self.Short_Line.next = self.Chance_Three

        self.Park_Place = bd.Board(None, 37, "Dark Blue", 350, 35, 200, 175, 500, 1100, 1300, 1500)
        self.Chance_Three.next = self.Park_Place

        self.Luxury_Tax = bd.Board(None, 38, 'Special')
        self.Park_Place.next = self.Luxury_Tax

        self.Boardwalk = bd.Board(self.Go, 39, 'Dark Blue', 400, 50, 200, 200, 600, 1400, 1700, 2000)
        self.Luxury_Tax.next = self.Boardwalk

        # Initalizes players
        if self.mode == 0:
            player_one = pl.Player(self.Go, 1, self.prompt_mode(player_modes, 1)) # initializes first player
        else:
            player_one = pl.Player(self.Go, 1, 0)
        player_two = pl.Player(self.Go, 2, self.prompt_mode(player_modes, 2)) # initializes second player
        self.players.add(player_one)
        self.players.add(player_two)
        self.turn_order.append(player_one)
        self.turn_order.append(player_two)

        if self.player_count > 2:
            player_three = pl.Player(self.Go, 3, self.prompt_mode(player_modes, 3)) # initializes third player
            self.players.add(player_three)
            self.turn_order.append(player_three)
        if self.player_count > 3:
            player_four = pl.Player(self.Go, 4, self.prompt_mode(player_modes, 4)) # initializes fourth player
            self.players.add(player_four)
            self.turn_order.append(player_four)

    # Prompts for number of players
    def input_num_players(self, player_modes):
        if player_modes:
            return len(player_modes)

        num = input('Enter the number of players (2-4): ')
        # Retries until user inputs valid number (2, 3, or 4)
        while num not in ['2','3','4']:
            num = input('Invalid Input! Please re-enter the number of players (2-4): ')
        return int(num)
    
    def prompt_mode(self, player_modes, player_number):
        if player_modes:
            return player_modes[player_number-1] if isinstance(player_modes[player_number-1], float) else 'Default'

        modes = ['Aggressive', 'Default', 'Conservative']

        print('Possible Modes: Aggressive, Default, Conservative')
        mode = input('Input player logic: ')

        while mode not in modes:
            mode = input('Not valid. Please enter again: ')
            
        return mode
    
    # Prompts for player logic
    def input_player_logic(self, game_mode=None):
        if game_mode is not None:
            return game_mode

        possible = {'0':'CPU Simulation', '1':'Player against CPU'}
        print('Possible Modes are:')
        for k,v in possible.items():
            print('Select', k, 'for', v, 'mode')
        mode = input('Select a player mode: ')
        # Retries until user inputs valid mode
        while mode not in possible:
            mode = input('Invalid Input! Please re-enter the player mode: ')

        return int(mode)

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
        return random.randint(0,self.player_count-1)
    
    # Removes player from the game and declares bankruptcy
    def dies(self, player, debtor='Bank', user=False):
        if user: print('Player ', str(player.number), ' has declared bankruptcy.')
        self.players_alive -= 1
        self.players.remove(player)
        self.dead_players.add(player)
        
        player.bankrupt(debtor)
        return
    
    # All players except 'player' pay 'player' 'amount'.
    def collect_from_all(self, player, amount):
        players = self.players.copy()
        for p in players:
            if player is p:
                continue
            if not p.pay_to(player, amount):
                if not p.debt(50): 
                    self.dies(p, player)
                    continue
                p.pay_to(player, amount)

    # 'player' pays 'amount' to the bank
    def pay_to_bank(self, player, amount):
        if player.money < amount:
            if not player.debt(amount): 
                self.dies(player)
        if player not in self.dead_players:
            player.money -= amount
            return True
        return False 
    
    # Condcuts communnity chest logic. Returns True if player is able to continue rolling (assuming double roll)
    def community_chest(self, player, user=False):
        card = self.cc.draw()

        if user: print("Community Chest!")
        #print('cc')
        #print(card)

        if card == 0: # Get of Jail Free Card
            if user: print("Get of Jail Free Card")
            player.jail_card.add('cc')
            self.cc.jail = True
        if card == 1: # Advance to Go
            if user: print("Advance to Go")
            player.location = self.Go
            player.money += 200
        if card == 2: # Bank Error
            if user: print("Bank Error")
            player.money += 200
        if card == 3: # Doctor's Fee
            if user: print("Doctor's Fee")
            self.pay_to_bank(player, 50)
        if card == 4: # Sale of Stock
            if user: print("Sale of Stock")
            player.money += 50
        if card == 5: # Go to Jail
            if user: print("Go to Jail")
            player.go_to_jail(self.Jail)
        if card == 6: # Grand Opera Night
            if user: print("Grand Opera Night")
            self.collect_from_all(player, 50)
        if card == 7: # Christmas
            if user: print("Christmas")
            player.money += 100
        if card == 8: # Income Tax Refund
            if user: print("Income Tax Refund")
            player.money += 20
        if card == 9: # Birthday
            if user: print("Birthday")
            self.collect_from_all(player, 10)
        if card == 10: # Life Insurance Matures
            if user: print("Life Insurance Matures")
            player.money += 100
        if card == 11: # Hospital Fees
            if user: print("Hospital Fees")
            self.pay_to_bank(player, 50)
        if card == 12: # School Fees
            if user: print("School Fees")
            self.pay_to_bank(player, 50)
        if card == 13: # Consultancy Fee
            if user: print("Consultancy Fee")
            player.money += 25
        if card == 14: # Street Repairs
            if user: print("Street Repairs")
            houses, hotels = 0, 0
            for property in player.properties:
                houses += property.num_houses
                if property.num_houses == 5:
                    houses -= 1
                    hotels += 1
            self.pay_to_bank(player, 40*houses + 115 * hotels)
        if card == 15: # Beauty Contest
            if user: print("Beauty Contest")
            player.money += 10
        if card == 16: # Inheritance
            if user: print("Inheritance")
            player.money += 100

        if player in self.dead_players or player.imprisoned:
            return False
        return True

    # Conducts chance logic. Returns True if player is able to continue rolling (assuming double roll)
    def chance(self, player, user=False):
        if user: print("Chance!")
        card = self.ch.draw()
        #print('chance')
        #print(card)

        if card == 0: # Get out of Jail Free
            if user: print("Get out of Jail Free")
            player.jail_card.add('chance')
            self.ch.jail = True
        if card == 1: # Advance to Go
            if user: print("Advance to Go")
            player.location = self.Go
            player.money += 200
        if card == 2: # Advance to Illinois
            if user: print("Advance to Illinois")
            if player.location.number > self.Illinois.number:
                player.money += 200
            player.location = self.Illinois

            if not self.land_on_location(player, user):
                return False
        if card == 3: #Advance to St. Charles
            if user: print("Advance to St. Charles")
            if player.location.number > self.St_Charles.number:
                player.money += 200
            player.location = self.St_Charles

            if not self.land_on_location(player, user):
                return False
        if card == 4: # Advance to nearest Utility.
            if user: print("Advance to nearest Utility")
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
        if card == 5: # Advance to nearest Railroad
            if user: print("Advance to nearest Railroad")
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
        if card == 6: # Bank Dividend
            if user: print("Bank Dividend")
            player.money += 50
        if card == 7: # Go back 3 spaces
            if user: print("Go back 3 spaces")
            for _ in range(37):
                player.location = player.location.next

            if not self.land_on_location(player, user):
                return False
        if card == 8: # Go to Jail
            if user: print("Go back Jail")
            player.go_to_jail(self.Jail)
        if card == 9: # General Repairs
            if user: print("General Repairs")
            houses, hotels = 0, 0
            for property in player.properties:
                houses += property.num_houses
                if property.num_houses == 5:
                    houses -= 1
                    hotels += 1
            self.pay_to_bank(player, 25*houses + 100 * hotels)
        if card == 10: # Advance to Reading Railroad
            if user: print("Advance to Reading Railroad")
            if player.location.number > self.Reading.number:
                player.money += 200
            player.location = self.Reading

            if not self.land_on_location(player, user):
                return False
        if card == 11: # Advance to Boardwalk
            if user: print("Advance to Boardwalk")
            if player.location.number > self.Boardwalk.number:
                player.money += 200
            player.location = self.Boardwalk

            if not self.land_on_location(player, user):
                return False
        if card == 12: # Chairman of the board
            if user: print("Chairman of the board")
            # Player first pays 50 per player to bank (in case player doesn't have enough), then bank pays to each player
            self.pay_to_bank(player, 50*(self.players_alive -1))
            for p in self.players:
                if player is p:
                    continue
                player.money += 50
        if card == 13: # Building matures
            if user: print("Building matures")
            player.money += 150
        
        if player in self.dead_players or player.imprisoned:
            return False
        return True
    
    # Conducts trades if suitable to all parties and keeps player above their limit
    def trade(self, player, limit, user=False):
        # Edge case: player has no properties
        if not player.properties:
            return

        # Ensure player sets are updated
        player.update_whole_set()

        # Check for how many sets 'player' is missing only one property from completing
        master_list = {'Brown':2, 'Light Blue':3, 'Purple':3, 'Orange':3, 'Red':3, 'Yellow':3, 'Green':3, 'Dark Blue':2, 'Utility':2}
        player_list = {set:0 for set in master_list}
        
        if user:
            while True:
                nums = [p.number for p in player.properties]
                print("Here is a list of all your properties:")
                for p in player.properties:
                    print(str(p.number) + ':', name[p.number])

                tp = input('Select a number to trade or -1 to skip: ')
                while tp != '-1' and int(tp) not in nums:
                    tp = input('Invalid input. Input again: ')

                if tp == '-1':
                    return
                
                print("Here is a list of all properties and their owners:")
                curr = self.Go

                possible_trades = []
                for i in range(40):
                    curr = curr.next
                    if curr.unowned: 
                        continue
                    if curr.owner.number == player.number:
                        curr = curr.next
                        continue

                    print(name[curr.number], '('+str(curr.number)+')', "Owner is Player", curr.owner.number)
                    possible_trades.append(curr.number)
                    curr = curr.next
                    
                other_property = input('Select a number to trade for or -1 to skip: ')
                while other_property != '-1' and int(other_property) not in possible_trades:
                    other_property = input('Invalid input. Input again: ')

                if other_property == '-1':
                    return

                while curr.number != int(other_property):
                    curr = curr.next

                traded_property = self.Go

                while traded_property.number != int(tp):
                    traded_property = traded_property.next
                

                # check if 'traded_property' will fill a set for other player
                other_count = 0
                for p in curr.owner.properties:
                    if p.set == traded_property.set:
                        other_count += 1

                # calculates 'cash' amount that player will also pay to complete trade
                if other_count + 1 == master_list[traded_property.set]:
                    cash = curr.cost - traded_property.cost
                else:
                    cash = 2 * curr.cost - traded_property.cost

                # if player doesn't have enough money, trade is prevented
                if player.money - cash < limit:
                    print("Trade partner depands too much money. Try a new trade!")
                    break
                
                # traded_property switches owner
                traded_property.owner = curr.owner

                player.properties.remove(traded_property)
                curr.owner.properties.add(traded_property)

                # money is exchanged
                player.money -= cash
                curr.owner.money += cash

                # curr switches owner
                curr.owner = player
                player.properties.add(curr)
                traded_property.owner.properties.remove(curr)

                print("You traded", name[traded_property.number], "and -$" + str(cash), "for", name[curr.number])

            return

        

        for property in player.properties:
            if property.whole_set:
                if property.set in player_list:
                    del player_list[property.set]
            elif property.set == 'RR':
                continue
            else:
                player_list[property.set] += 1

        # Sort sets into either missing one or missing two locations
        missing_one = set()
        missing_two = set()

        for k, v in player_list.items():
            if v == master_list[k] - 1:
                missing_one.add(k)
            if v == master_list[k] - 2:
                missing_two.add(k)

        missing_two_list = [p for p in player.properties if p.set in missing_two]

        missing_two_list.sort(key = lambda x:x.cost)

        curr = self.Go
        
        traded = False
        # Initiating possible trades 
        if missing_two_list and missing_one:
            for _ in range(40):
                if not missing_two_list:
                    break
                # Suitable property to be traded : 'curr'
                if curr.set in missing_one and not curr.unowned and curr.owner is not player:
                    traded_property = missing_two_list.pop() # property that will be traded for 'curr'

                    # check if 'traded_property' will fill a set for other player
                    other_count = 0
                    for p in curr.owner.properties:
                        if p.set == traded_property.set:
                            other_count += 1

                    # calculates 'cash' amount that player will also pay to complete trade
                    if other_count + 1 == master_list[traded_property.set]:
                        cash = curr.cost - traded_property.cost
                    else:
                        cash = 2 * curr.cost - traded_property.cost

                    # if player doesn't have enough money, trade is prevented
                    if player.money - cash < limit:
                        missing_two_list.append(traded_property)
                        continue

                    if self.mode == 1 and curr.owner.number == 1:
                        print("Player", player.number, "porposes to trade", name[traded_property.number], "and $" + str(cash) + " for", name[curr.number])
                        decide = input('Input 0 to accept trade or 1 to reject trade: ')
                        while int(decide) not in [0,1]:
                            decide = input('Invalid input. Input again: ')

                        if int(decide) == 1:
                            continue

                        print("Trade complete!")

                    # traded_property switches owner
                    traded_property.owner = curr.owner

                    player.properties.remove(traded_property)
                    curr.owner.properties.add(traded_property)

                    # money is exchanged
                    player.money -= cash
                    curr.owner.money += cash

                    # curr switches owner
                    curr.owner = player
                    player.properties.add(curr)
                    traded_property.owner.properties.remove(curr)

                    # tracks if trades occured
                    traded = True

                    # if player has no more tradable properties, end trade logic
                    if not missing_two_list:
                        break
                curr = curr.next
            
            if traded:
                player.update_whole_set()
        return

    # Conducts end of turn logic, including building on and and unmortaging properties
    def end_turn(self, player, user=False):
        # Calculates limit that player can't go below
        ratios = {'Default': 0.5,
                  'Aggressive':0.15,
                  'Conservative':0.85} # NEED to add more ratio options
        
        ratio = ratios[player.aggression] if player.aggression in ratios else player.aggression

        #limit = min(max(int(player.money * ratio), 400),1000)

        limit = int(player.money * ratio)

        # Player initiates trades
        self.trade(player, limit, user)

        not_monopoly = set() # creates set of properties not in a monopoly (will include railroads and utilites)
        is_monopoly = set() # creates set of properties in a monopoly

        # sorts 'player''s properties into 'not_monopoly' and 'monopoly' sets
        for property in player.properties:
            if property.whole_set and property.set != 'Utility':
                is_monopoly.add(property)
            else:
                not_monopoly.add(property)

        total_sets = ['Brown', 'Light Blue', 'Purple', 'Orange', 'Red', 'Yellow', 'Green', 'Dark Blue']

        # Create list of lists of monopolies, sorted by highest cost to lowest cost
        lst_is_monopoly = [sorted([property for property in is_monopoly if property.set == s], key = lambda x:(-x.cost)) for s in total_sets]

        ask = False
        # Unmortage as many properties as we can
        for s in lst_is_monopoly:
            for property in s:
                if property.mortaged:
                    if user: 
                        if not ask:
                            ask = True
                            user_mortage = input('You have mortaged propreties. Would you like to unmortage them? Input 0 for yes, 1 for no: ')
                            while user_mortage not in ['0', '1']:
                                user_mortage = input('Invalid input. Input again: ')

                            if user_mortage == '1':
                                break
                    
                    if not player.unmortage(property, limit):
                        break
        
        # Create list of lists of monopolies, sorted by most expensive monopoly to least
        lst_is_monopoly = [[property for property in is_monopoly if property.set == s] for s in total_sets]
        lst_is_monopoly = lst_is_monopoly[::-1]

        ask_houses = False
        # Purchas as many houses/hotels as possible
        for s in lst_is_monopoly:
            if not s:
                continue
            if user:
                if not ask_houses:
                    ask_houses = True
                    user_houses = input('You have monopolies. Would you like to build houses? Input 0 for yes, 1 for no: ')
                    while user_houses not in ['0', '1']:
                        user_houses = input('Invalid input. Input again: ')

                    if user_houses == '1':
                        break

            mortaged = False     
            hp = []

            # Check if set contains mortaged properties, continue onto next set if so
            for property in s:
                if property.mortaged:
                    mortaged = True
                    break
                hq.heappush(hp, (property.num_houses, property))
            if not mortaged:
                while hp:
                    n, p = hq.heappop(hp)

                    # Check if player is able to build more houses/hotels
                    if n < 4 and self.houses == 32:
                        continue
                    if n == 4 and self.hotels == 12:
                        continue

                    if not player.buy_house(property, limit):
                        break

                    if n != 4:
                        hq.heappush(hp, (n+1, p))
                        self.houses += 1
                    else:
                        self.hotels += 1
                        self.houses -= 4

        # Create list of properies not in a monopoly, or RR/Utility, sorted from highest to lowest cost
        lst_not_monopoly = sorted(not_monopoly, key = lambda x : -x.cost)

        for property in lst_not_monopoly:
            if property.mortaged:
                if user:
                    if ask:
                        if user_mortage == '1':
                            break
                    else:
                        ask = True
                        user_mortage = input('You have mortaged propreties. Would you like to unmortage them? Input 0 for yes, 1 for no: ')
                        while user_mortage not in ['0', '1']:
                            user_mortage = input('Invalid input. Input again: ')

                        if user_mortage == '1':
                            break
                if not player.unmortage(property, limit):
                    break
                        
    # Logic once player lands on a location after a roll. Returns True if player can roll again (assuming double roll)
    def land_on_location(self, player, roll=0, user=False):
        if user: print("You landed on ", name[player.location.number])
        # 'player' lands on a location that is not ownable
        if player.location.set == 'Special':
            # player lands on Go, Free Parking, or Jail
            if player.location is self.Go or player.location is self.Free_Parking or player.location is self.Jail:
                pass
            # player lands on a Community Chest
            elif player.location is self.Community_Chest_One or player.location is self.Community_Chest_Two or player.location is self.Community_Chest_Three:
                if not self.community_chest(player, user):
                    return False
            # player lands on a Chance
            elif player.location is self.Chance_One or player.location is self.Chance_Two or player.location is self.Chance_Three:
                if not self.chance(player, user):
                    return False
            # player lands on Income Tax
            elif player.location is self.Income_Tax:
                if user: print("Income tax, pay 200!")
                if not self.pay_to_bank(player, 200):
                    return False
            # player lands on Luxury Tax
            elif player.location is self.Luxury_Tax:
                if user: print("Luxury Tax, pay 100!")
                if not self.pay_to_bank(player, 100):
                    return False
            # player lands on Go To Jail
            else:
                if user: print("Go to Jail!")
                player.go_to_jail(self.Jail)
                return False
        # 'player' lands on unowned property
        elif not player.location.owner:
            if user:
                print("This property is unowned. It costs $" + str(player.location.cost) + ". Do you wish to buy?")
                select = input('Select 0 to buy, 1 to not buy: ')
                while int(select) not in [0, 1] or (int(select) == 0 and player.money < player.location.cost):
                    select = input('Invalid input. Input again: ')
            if user and select == '0':
                player.buy(player.location)
                player.update_whole_set()
            else:
                if player.money >= player.location.cost:
                    player.buy(player.location)
                    player.update_whole_set()
        # 'player' lands on own property
        elif player.location.owner is player:
            if user: "Your property!"
            pass
        # 'player' lands on an owned proprety
        else:
            # 'player' pays no rent if the property is mortaged
            if player.location.mortaged:
                rent = 0
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
                if user: print("Pay ", str(rent), " to Player ", str(player.location.owner.number))
                if not player.debt(rent): 
                    self.dies(player, player.location.owner)
                    return False
                player.pay_to(player.location.owner, rent)

        return True
    

def main(limit_turns, game_mode=None, player_modes=None):
    print('Welcome to Monopoly!')

    game = Game(game_mode, player_modes) # creates game

    turn = game.determine_order_of_play() # determines player that goes first

    while game.players_alive > 1 and game.total_turns < limit_turns:
        curr_player = game.turn_order[turn]
        
        # User == True refrers to single player mode (e.g. user inputs)
        if game.mode == 1 and curr_player.number == 1:
            user = True
        else:
            user = False
    
        if user:
            print("You have $", str(curr_player.money))
            print("You own these properties: ", ', '.join([name[p.number] for p in curr_player.properties]))

        #print(curr_player.location.number)

        # checking if curr_player has been eliminated. If so, game continues onto next player
        if curr_player in game.dead_players: 
            turn += 1
            turn = turn % game.player_count
            continue
        
        # creates list 'rolls' which details the rolls 'curr_player' receives.
        double = True
        rolls = []
        while double and len(rolls) <= 2:
            roll, double = game.dice_roll(len(rolls))
            rolls.append(roll)

        #print(rolls)

        for roll in rolls:
            if user: print("You rolled a ", str(roll))
            game.property_count[curr_player.location.number] += 1

            # checks if 'curr_player' received 3 consecutive doubles. If so, 'curr_player' is sent to jail
            if roll == -1:
                if user: print("You rolled three doubles in a row. Go to Jail!")
                curr_player.go_to_jail(game.Jail)
                break
            
            # checks if 'curr_player' begins their turn imprisoned.
            if curr_player.imprisoned:
                if user: print("You are currently inprisoned.")
                if len(rolls) == 1: # first roll is not a double
                    if user:
                        print('You have currently ', str(len(curr_player.jail_card)), 'Get of Jail Free Cards.')
                        select = input('Select 0 to use a Get out of Jail Free card, 1 to pay $50 to leave jail, or 2 to remain in jail: ')
                        while int(select) not in [0, 1, 2] or (select == '0' and str(len(curr_player.jail_card)) == 0) or curr_player.imprisoned_count == 2 and select == '2':
                            select = input('Invalid input. Please select again: ')

                        if int(select) == 0:
                            if 'cc' in curr_player.jail_card:
                                curr_player.jail_card.remove('cc')
                                game.cc.jail = False
                            else:
                                curr_player.jail_card.remove('chance')
                                game.ch.jail = False
                        elif int(select) == 1:
                            if not curr_player.debt(50): # if 'curr_player' is unable to pay the $50
                                game.dies(curr_player)
                                break
                            curr_player.money -= 50
                        elif int(select) == 2:
                            curr_player.imprisoned_count += 1
                            break
                    else:
                        # 'curr_player' will first try to use a Get ouf of Jail Free Card
                        if len(curr_player.jail_card) > 0:
                            if 'cc' in curr_player.jail_card:
                                curr_player.jail_card.remove('cc')
                                game.cc.jail = False
                            else:
                                curr_player.jail_card.remove('chance')
                                game.ch.jail = False
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
                    if user: print("You passed Go!")
                    curr_player.money += 200


            if not game.land_on_location(curr_player, roll, user):
                break
        
        # 'curr_player'' now has opporuinity to build unmortage properties and build houses/hotels
        if curr_player in game.players:
            game.end_turn(curr_player, user)
        elif user:
            print("You declared bankruptcy. Game over!")

        # turn count is not updated for next player
        turn += 1
        turn = turn % game.player_count
        game.total_turns += 1

    winner = sorted(game.players, key = lambda x:-x.money)[0]
    
    if game.mode == 1: print('Winner is Player', winner.number)
    #print('Total number of turns: ', game.total_turns)
    #for player in game.players:
        #print('Player ' + str(player.number) + ' had $' + str(player.money))
    #return game.property_count
    return winner.number
    
if __name__ == '__main__':
   main(250)



            


