class Menu:
    def __init__(self):
        pass
    
    def choose_player_names(self, count):
        if count == 2:
            first_name = input("player1 name")
            second_name = input("player2 name")
            return (first_name,second_name)
        else:
            first_name = input("player1 name")
            return(first_name)

    def get_valid_choice(self, prompt, option_count):
        while True:
            answer = input(prompt)
            try:
                answer = int(answer)
            except ValueError:
                print(f"Please enter a number between 1 and {option_count}")
                continue
            if 1 <= answer <= option_count:
                return answer