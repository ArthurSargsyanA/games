class Board:
    def __init__(self):
        self.box = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def place_mark(self, pos, mark):
        if pos < 10 and pos > 0:

            if  self.box[(pos - 1) // 3][(pos - 1) % 3] == " ":
                self.box[(pos - 1) // 3][(pos - 1) % 3] = mark
            else:
                return False

            return True
        return False
    
    def get_empty_positions(self):
        empty = []
        for pos in range(1, 10):
            row = (pos - 1) // 3
            col = (pos - 1) % 3
            if self.box[row][col] == " ":
                empty.append(pos)
        return empty
    
    def remove_mark(self, pos):
        row = (pos - 1) // 3
        col = (pos - 1) % 3
        self.box[row][col] = " "