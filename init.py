import player as pl

class Game:
    def __init__(self, num):
        self.player_count = num
        self.players = {}
        for i in range(num):
            name_str = 'player_' + str(i)
            self.players[name_str] == pl()

