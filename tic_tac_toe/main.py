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
            count = menu.choose_player_count()
            if count != 2:
                bot_type = menu.choose_difficulty()
            names = menu.choose_player_names(count)
            players = factory_players.create_players(count, names, bot_type)
            
        board = Board()
        game = Game(board, players, drawer, rules)
        game.start()
        next_action = menu.selection()


if __name__ == "__main__":
    main()