from board import Board
from rules import Rules
from player import HumanPlayer, BotPlayer
from ui import Drawer
from game_engine import Game

class Menu:
    def __init__(self):
        pass
    def choose_count_players(self):
        while True:
            count = input("1) players 1    2) players 2 ")
            try:
                count = int(count)
            except:
                print("Please enter a number between 1 and 2")
                continue
            if count == 1 or count == 2:
                return count

def main():
    board = Board()
    rules = Rules()
    drawer = Drawer()
    menu = Menu()

    count = menu.choose_count_players()

    if count == 2:
        p1 = HumanPlayer('X', 'Player 1')
        p2 = HumanPlayer('O', 'Player 2')
    else:
        p1 = HumanPlayer('X', 'Player 1')
        p2 = BotPlayer('O', 'Player 2')

    game = Game(board, (p1, p2), drawer, rules)
    game.start()


if __name__ == "__main__":
    main()