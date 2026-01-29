class Game:
    def __init__(self, board, players, drawer, rules):
        self.board = board
        self.players = players
        self.drawer = drawer
        self.rules = rules
        self.play = 0
    
    def play_turn(self):
        is_valid = False
        while not is_valid:
            pos = self.players[self.play].chose_position()
            if self.board.place_mark(pos, self.players[self.play].mark):
                is_valid = True
        self.play = 0 if self.play else 1
        self.drawer.draw_cell(self.board)

    def start(self):
        self.drawer.draw_cell(self.board)
        while True:
            self.play_turn()
            if self.rules.is_wins(self.board):
                print(f"congratuation {self.players[1 - self.play].name}")
                break
            elif self.rules.is_draw(self.board):
                print("draw")
                break