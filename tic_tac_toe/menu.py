class Menu:
    def __init__(self):
        pass
    def choose_player_count(self):
        while True:
            count = input("1) players 1    2) players 2 ")
            try:
                count = int(count)
            except:
                print("Please enter a number between 1 and 2")
                continue
            if count == 1 or count == 2:
                return count
            
    def choose_difficulty(self):
        while True:
            count = input("1) Easy    2) Medium ")
            try:
                count = int(count)
            except:
                print("Please enter a number between 1 and 2")
                continue
            if count == 1 or count == 2:
                return count
            
    def choose_player_names(self, count):
        if count == 2:
            first_name = input("player1 name")
            second_name = input("player2 name")
            return (first_name,second_name)
        else:
            first_name = input("player1 name")
            return(first_name,)

    
    def selection(self):
        while True:
            next_action = input("1) Try again    2) Go to menu ")
            try:
                next_action = int(next_action)
            except:
                print("Please enter a number between 1 and 2")
                continue
            if next_action == 1 or next_action == 2:
                return next_action