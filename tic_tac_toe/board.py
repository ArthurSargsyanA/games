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