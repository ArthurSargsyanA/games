class Board:
    def __init__(self):
        self.box = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def place_mark(self, pos, mark):
        try:
            pos = int(pos)
        except:
            print("write number")
            return False

        if pos < 10 and pos > 0:

            if  self.box[(pos - 1) // 3][(pos - 1) % 3] == " ":
                self.box[(pos - 1) // 3][(pos - 1) % 3] = mark
            else:
                return False

            return True
        return False
    

class Drawer:
    def draw_cell(self, board):
        for i in range(3):
            print(f"| {board.box[i][0]} | {board.box[i][1]} | {board.box[i][2]}")
            print("__________")


class Player:
    def __init__(self, mark, name):
        self.mark = mark
        self.name = name

    def chose_position(self):
        pos = input("mark position")
        return pos
    

class Rules:
    def _get_left_diagonal(self, board):
        return [board.box[i][i] for i in range(len(board.box))]
    
    def _get_right_diagonal(self, board):
        return [board.box[i][len(board.box)-1-i] for i in range(len(board.box))]
    
    def _is_winning_line(self, box):
        if len(set(box)) == 1 and box[0] != ' ':
            return True
        return False
    
    def _get_all_cols(self, board):
        size = len(board.box)
        return [
            [board.box[row][col] for row in range(size)]
            for col in range(size)
        ]

    def is_wins(self, board):
        for val in board.box:
            if self._is_winning_line(val):
                return True
            
        for val in self._get_all_cols(board):
            if self._is_winning_line(val):
                return True
            
        if self._is_winning_line(self._get_left_diagonal(board)):
            return True
        
        if self._is_winning_line(self._get_right_diagonal(board)):
            return True
        
        return False
    
    def is_draw(self, board):
        for val in board.box:
            if ' ' in val:
                return False
        return True



class Game:
    def __init__(self, board, players, drawer):
        self.board = board
        self.players = players
        self.play = 0
        self.drawer = drawer
    
    def play_turn(self):
        is_valid = False
        while not is_valid:
            pos = self.players[self.play].chose_position()
            if self.board.place_mark(pos, self.players[self.play].mark):
                is_valid = True
        self.play = 0 if self.play else 1
        print(" chooose_play" , self.board.box)
        self.drawer.draw_cell(self.board)
        
        
board = Board()
drawer = Drawer()
rules = Rules()
drawer.draw_cell(board)
pl1 = Player('x', 'ar')
pl2 = Player('o', 'lal')
game = Game(board, (pl1, pl2), drawer)
while not rules.is_wins(board):
    if rules.is_draw(board):
        print("draw")
        break
    game.play_turn()
