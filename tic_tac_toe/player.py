class Player:
    def __init__(self, mark, name):
        self.mark = mark
        self.name = name

    def chose_position(self):
        pos = input("mark position")
        return pos