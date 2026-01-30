import random
from abc import ABC , abstractmethod

class Player(ABC):
    def __init__(self, mark, name):
        self.mark = mark
        self.name = name

    @abstractmethod
    def choose_position(self):
        pass

class HumanPlayer(Player):
     def choose_position(self):
        while True:
            pos = input("mark position")
            try:
                pos = int(pos)
            except:
                print("Please enter a number between 1 and 9")
                continue
            return pos
     
class BotPlayer(Player):
     def choose_position(self):
        pos = random.randint(1, 9)
        return pos
          