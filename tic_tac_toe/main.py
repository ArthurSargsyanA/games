from board import Board
from rules import Rules
from player import FactoryPlayers
from ui import Drawer
from game_engine import Game
from menu import Menu


def main():
    rules = Rules()
    drawer = Drawer()
    menu = Menu()
    factory_players = FactoryPlayers()
    next_action = 2

    while True:
        if next_action == 2:
            bot_type = 0
            count = menu.get_valid_choice("1) players 1    2) players 2 ", 2)
            if count != 2:
                bot_type = menu.get_valid_choice("1) Easy    2) Medium    3) Hard ", 3)
                mark_type = menu.get_valid_choice("choose your mark 1) X    2) O ", 2)
            names = menu.choose_player_names(count)
            players = factory_players.create_players(count, names, bot_type, mark_type)
            
        board = Board()
        game = Game(board, players, drawer, rules)
        game.start()
        next_action = menu.get_valid_choice("1) Try again    2) Go to menu ", 2)


if __name__ == "__main__":
    main()