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
        empty = board.get_empty_positions()
        return random.choice(empty)


class MediumBotStrategy(BotStrategy):
    def choose_move(self, board, mark, rules):
        empty = board.get_empty_positions()

        for pos in empty:
            board.place_mark(pos, mark)
            if rules.get_winner(board):
                board.remove_mark(pos)
                return pos
            board.remove_mark(pos)

        opponent = 'O' if mark == 'X' else 'X'

        for pos in empty:
            board.place_mark(pos, opponent)
            if rules.get_winner(board):
                board.remove_mark(pos)
                return pos
            board.remove_mark(pos)

        return random.choice(empty)
    

class HardBotStrategy(BotStrategy):
    def minimax(self, board, is_maximizing, rules):
        if rules.get_winner(board) == 'X':
            return 1
        elif rules.get_winner(board) == 'O':
            return -1
        elif rules.is_draw(board):
            return 0
        
        empty = board.get_empty_positions()
        if is_maximizing:
            best_score = -float("inf")
            for pos in empty:
                board.place_mark(pos, 'X')
                score = self.minimax(board, not is_maximizing, rules)
                board.remove_mark(pos)
                best_score = max(score, best_score)

            return best_score

        else:
            best_score = float("inf")
            for pos in empty:
                board.place_mark(pos, 'O')
                score = self.minimax(board, not is_maximizing, rules)
                board.remove_mark(pos)
                best_score = min(score, best_score)

            return best_score

    def choose_move(self, board, mark, rules):
        best_move = -1

        if mark == 'X':
            best_score = -float("inf")
            for pos in board.get_empty_positions():
                board.place_mark(pos, 'X')
                score = self.minimax(board, False, rules)
                print(pos, score)
                board.remove_mark(pos)

                if score > best_score:
                    best_score = score
                    best_move = pos

        else:
            best_score = float("inf")
            for pos in board.get_empty_positions():
                board.place_mark(pos, 'O')
                score = self.minimax(board, True, rules)
                print(pos, score)
                board.remove_mark(pos)

                if score < best_score:
                    best_score = score
                    best_move = pos

        return best_move


class FactoryPlayers:
    def __init__(self):
        pass

    def create_players(self, count, names, bot_type, mark_type):
        if count == 2:
            p1 = HumanPlayer('X', names[0])
            p2 = HumanPlayer('O', names[1])
        else:
            if bot_type == 2:
                bot = MediumBotStrategy()
            elif bot_type == 3:
                bot = HardBotStrategy()
            else:
                bot = EasyBotStrategy()

            if mark_type == 1:
                p1 = HumanPlayer('X', names[0])
                p2 = BotPlayer('O', 'Player 2', bot)
            else:
                p2 = HumanPlayer('O', names[0])
                p1 = BotPlayer('X', 'Player 2', bot)
            
        return (p1,p2)
