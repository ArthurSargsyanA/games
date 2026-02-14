class Game:
    def __init__(self, board, players, drawer, rules):
        self.board = board
        self.players = players
        self.drawer = drawer
        self.rules = rules
        self.current_player_index = 0
    
    def play_turn(self):
        is_valid = False
        while not is_valid:
            pos = self.players[self.current_player_index].choose_position(self.board, self.rules)
            if self.board.place_mark(pos, self.players[self.current_player_index].mark):
                is_valid = True
        # self.current_player_index = 0 if self.current_player_index else 1
        self.current_player_index = 1 - self.current_player_index
        self.drawer.draw_board(self.board)

    def start(self):
        self.drawer.draw_board(self.board)
        while True:
            self.play_turn()
            if self.rules.has_winner(self.board):
                print(f"congratuation {self.players[1 - self.current_player_index].name}")
                break
            elif self.rules.is_draw(self.board):
                print("draw")
                break