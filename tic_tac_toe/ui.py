class Drawer:
    def draw_board(self, board):
        for i in range(3):
            print(f"| {board.box[i][0]} | {board.box[i][1]} | {board.box[i][2]}")
            print("__________")