import random
from abc import ABC , abstractmethod

class Player(ABC):
    def __init__(self, mark, name):
        self.mark = mark
        self.name = name

    @abstractmethod
    def choose_position(self, board, rules):
        pass

class HumanPlayer(Player):
     def choose_position(self, board, rules):
        while True:
            pos = input("mark position")
            try:
                pos = int(pos)
            except:
                print("Please enter a number between 1 and 9")
                continue
            return pos
     
class BotPlayer(Player):
     def __init__(self, mark, name, strategy):
        super().__init__(mark, name)
        self.strategy = strategy

     def choose_position(self, board, rules):
        return self.strategy.choose_move(board, self.mark, rules)
          
class BotStrategy(ABC):
    @abstractmethod
    def choose_move(self, board, mark, rules):
        pass

class EasyBotStrategy(BotStrategy):
    def choose_move(self, board, mark, rules):
        pos = random.randint(1, 9)
        return pos

class MediumBotStrategy(BotStrategy):
    def choose_move(self, board, mark, rules):
        empty = board.get_empty_positions()

        for pos in empty:
            board.place_mark(pos, mark)
            if rules.has_winner(board):
                board.remove_mark(pos)
                return pos
            board.remove_mark(pos)

        opponent = 'O' if mark == 'X' else 'X'

        for pos in empty:
            board.place_mark(pos, opponent)
            if rules.has_winner(board):
                board.remove_mark(pos)
                return pos
            board.remove_mark(pos)

        return random.choice(empty)

class FactoryPlayers:
    def __init__(self):
        pass

    def create_players(self, count, names, bot_type):
        if count == 2:
            p1 = HumanPlayer('X', names[0])
            p2 = HumanPlayer('O', names[1])
        else:
            if bot_type == 2:
                bot = MediumBotStrategy()
            else:
                bot = EasyBotStrategy()
            p1 = HumanPlayer('X', names[0])
            p2 = BotPlayer('O', 'Player 2', bot)
            
        return (p1,p2)

