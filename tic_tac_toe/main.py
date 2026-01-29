from board import Board
from rules import Rules
from player import Player
from ui import Drawer
from game_engine import Game


def main():
    board = Board()
    rules = Rules()
    drawer = Drawer()

    p1 = Player('X', 'Player 1')
    p2 = Player('O', 'Player 2')

    game = Game(board, (p1, p2), drawer, rules)
    game.start()


if __name__ == "__main__":
    main()